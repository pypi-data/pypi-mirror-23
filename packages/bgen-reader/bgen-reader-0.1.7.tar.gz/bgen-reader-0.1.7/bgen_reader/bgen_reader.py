import errno
import os
import sys
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool

import dask
import dask.array as da
from dask.delayed import delayed
from numpy import sum as npy_sum
from numpy import arange, empty, float64, zeros
from pandas import DataFrame
from tqdm import tqdm

from ._ffi import ffi
from ._ffi.lib import (close_bgen, close_variant_genotype, free, get_ncombs,
                       get_nsamples, get_nvariants, open_bgen,
                       open_variant_genotype, read_samples,
                       read_variant_genotype, read_variants,
                       sample_ids_presence, string_duplicate)

dask.set_options(pool=ThreadPool(cpu_count()))

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

PY3 = sys.version_info >= (3, )


def _to_string(v):
    v = string_duplicate(v)
    return ffi.string(v.str, v.len).decode()


def _read_variants(bgenfile):
    indexing = ffi.new("VariantIndexing *[1]")
    nvariants = get_nvariants(bgenfile)
    variants = read_variants(bgenfile, indexing)

    data = dict(id=[], rsid=[], chrom=[], pos=[], nalleles=[])
    for i in range(nvariants):
        data['id'].append(_to_string(variants[i].id))
        data['rsid'].append(_to_string(variants[i].rsid))
        data['chrom'].append(_to_string(variants[i].chrom))

        data['pos'].append(variants[i].position)
        data['nalleles'].append(variants[i].nalleles)

    return (DataFrame(data=data), indexing)


def _read_samples(bgenfile):

    nsamples = get_nsamples(bgenfile)
    samples = read_samples(bgenfile)

    py_ids = []
    for i in range(nsamples):
        py_ids.append(_to_string(samples[i]))

    return DataFrame(data=dict(id=py_ids))


def _generate_samples(bgenfile):
    nsamples = get_nsamples(bgenfile)
    return DataFrame(data=dict(id=['sample_%d' % i for i in range(nsamples)]))


class ReadGenotypeVariant(object):
    def __init__(self, indexing):
        self._indexing = indexing

    def __call__(self, nsamples, nalleles, variant_idx, nvariants):

        ncombss = []
        variants = []

        for i in range(variant_idx, variant_idx + nvariants):
            vg = open_variant_genotype(self._indexing[0], i)

            ncombs = get_ncombs(vg)
            ncombss.append(ncombs)
            g = empty((nsamples, ncombs), dtype=float64)

            pg = ffi.cast("real *", g.ctypes.data)
            read_variant_genotype(self._indexing[0], vg, pg)

            close_variant_genotype(self._indexing[0], vg)

            variants.append(g)

        G = zeros((nvariants, nsamples, max(ncombss)), dtype=float64)

        for i in range(0, nvariants):
            G[i, :, :ncombss[i]] = variants[i]

        return G


def _read_genotype(indexing, nsamples, nvariants, nalleless, verbose):

    genotype = []
    rgv = ReadGenotypeVariant(indexing)

    step = min(25, nvariants)
    tqdm_kwds = dict(desc='Variant mapping', disable=not verbose)

    for i in tqdm(range(0, nvariants, step), **tqdm_kwds):
        size = min(step, nvariants - i)
        tup = nsamples, nalleless[i:i + size], i, size
        delayed_kwds = dict(pure=True, traverse=False)
        g = delayed(rgv, **delayed_kwds)(*tup)
        # TODO: THIS IS A HACK
        ncombs = 3
        g = da.from_delayed(g, (size, nsamples, ncombs), float64)
        genotype.append(g)

    return da.concatenate(genotype)


def read_bgen(filepath, verbose=True):
    r"""Read a given BGEN file.

    Args
    ----
    filepath : str
        A BGEN file path.
    verbose : bool
        ``True`` to show progress; ``False`` otherwise.

    Returns
    -------
    dict
        variants : Variant position, chromossomes, RSIDs, etc.
        samples : Sample identifications.
        genotype : Array of genotype references.
    """

    if PY3:
        try:
            filepath = filepath.encode()
        except AttributeError:
            pass

    if (not os.path.exists(filepath)):
        raise FileNotFoundError(errno.ENOENT,
                                os.strerror(errno.ENOENT), filepath)

    bgenfile = open_bgen(filepath)

    if sample_ids_presence(bgenfile) == 0:
        if verbose:
            print("Sample IDs are not present. I will generate fake ones.")
        samples = _generate_samples(bgenfile)
    else:
        samples = _read_samples(bgenfile)

    variants, indexing = _read_variants(bgenfile)
    nalleless = variants['nalleles'].values

    nsamples = samples.shape[0]
    nvariants = variants.shape[0]
    close_bgen(bgenfile)

    genotype = _read_genotype(indexing, nsamples, nvariants, nalleless,
                              verbose)

    return dict(variants=variants, samples=samples, genotype=genotype)


def convert_to_dosage(G, verbose=True):
    ncombs = G.shape[2]
    mult = da.arange(ncombs, chunks=ncombs, dtype=float64)
    return da.sum(mult * G, axis=2)
