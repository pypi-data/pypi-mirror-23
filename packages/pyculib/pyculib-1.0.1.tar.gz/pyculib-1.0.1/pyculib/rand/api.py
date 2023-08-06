import numpy as np
import time
from . import binding
from numba import cuda

class RNG(object):
    "cuRAND pseudo random number generator"
    def __init__(self, gen):
        self._gen = gen
        self.__stream = 0

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset):
        self.__offset = offset
        self._gen.set_offset(offset)

    @property
    def stream(self):
        '''Associate a CUDA stream to the generator object.
        All subsequent calls will use this stream.'''
        return self.__stream

    @stream.setter
    def stream(self, stream):
        self.__stream = stream
        self._gen.set_stream(stream)

    def _require_array(self, ary):
        if ary.ndim != 1:
            raise TypeError("Only accept 1-D array")
        if ary.strides[0] != ary.dtype.itemsize:
            raise TypeError("Only accept unit strided array")


class PRNG(RNG):
    '''cuRAND pseudo random number generator

    :param rndtype: Algorithm type.  All possible values are listed as
                    class attributes of this class, e.g. TEST, DEFAULT,
                    XORWOW, MRG32K3A, MTGP32.
    :param seed: Seed for the RNG.
    :param offset: Offset to the random number stream.
    :param stream: CUDA stream.

    Example:

    >>> from pyculib import rand
    >>> from numpy import empty
    >>> prng = rand.PRNG(rndtype=rand.PRNG.XORWOW)
    >>> r = empty(10)
    >>> prng.uniform(r)
    >>> r
    array([ ... ])
    '''

    TEST     = binding.CURAND_RNG_TEST
    DEFAULT  = binding.CURAND_RNG_PSEUDO_DEFAULT
    XORWOW   = binding.CURAND_RNG_PSEUDO_XORWOW
    MRG32K3A = binding.CURAND_RNG_PSEUDO_MRG32K3A
    MTGP32   = binding.CURAND_RNG_PSEUDO_MTGP32

    @cuda.require_context
    def __init__(self, rndtype=DEFAULT, seed=None, offset=None, stream=None):
        super(PRNG, self).__init__(binding.Generator(rndtype))
        self.rndtype = rndtype
        if seed is not None:
            self.seed = seed
        if offset is not None:
            self.offset = offset
        if stream is not None:
            self.stream = stream

    @property
    def seed(self):
        "Mutatable attribute for the seed for the RNG"
        return self.__seed

    @seed.setter
    def seed(self, seed):
        self.__seed = seed
        self._gen.set_pseudo_random_generator_seed(seed)

    def uniform(self, ary, size=None):
        '''Generate floating point random number sampled
           from a uniform distribution and fill into ary.

        :param ary: Numpy array or cuda device array.
        :param size: Number of samples. Default to array size.
        '''
        self._require_array(ary)
        size = size or ary.size
        dary, conv = cuda._auto_device(ary, stream=self.stream)
        self._gen.generate_uniform(dary, size)
        if conv:
            dary.copy_to_host(ary, stream=self.stream)

    def normal(self, ary, mean, sigma, size=None):
        '''Generate floating point random number sampled
        from a normal distribution and fill into ary.

        :param ary: Numpy array or cuda device array.
        :param mean: Center of the distribution.
        :param sigma: Standard deviation of the distribution.
        :param size: Number of samples. Default to array size.
        '''
        self._require_array(ary)
        size = size or ary.size
        dary, conv = cuda._auto_device(ary, stream=self.stream)
        self._gen.generate_normal(dary, size, mean, sigma)
        if conv:
            dary.copy_to_host(ary, stream=self.stream)


    def lognormal(self, ary, mean, sigma, size=None):
        '''Generate floating point random number sampled
           from a log-normal distribution and fill into ary.

        :param ary: Numpy array or cuda device array.
        :param mean: Center of the distribution.
        :param sigma: Standard deviation of the distribution.
        :param size: Number of samples. Default to array size.
        '''
        self._require_array(ary)
        size = size or ary.size
        dary, conv = cuda._auto_device(ary, stream=self.stream)
        self._gen.generate_log_normal(dary, size, mean, sigma)
        if conv:
            dary.copy_to_host(ary, stream=self.stream)

    def poisson(self, ary, lmbd, size=None):
        '''Generate floating point random number sampled
        from a poisson distribution and fill into ary.

        :param ary: Numpy array or cuda device array.
        :param lmbda: Lambda for the distribution.
        :param size: Number of samples. Default to array size.
        '''
        self._require_array(ary)
        size = size or ary.size
        dary, conv = cuda._auto_device(ary, stream=self.stream)
        self._gen.generate_poisson(dary, lmbd, size)
        if conv:
            dary.copy_to_host(ary, stream=self.stream)


class QRNG(RNG):
    '''cuRAND quasi random number generator

    :param rndtype: Algorithm type.
                    Also control output data type.
                    All possible values are listed as class
                    attributes of this class, e.g. TEST, DEFAULT, SOBOL32,
                    SCRAMBLED_SOBOL32, SOBOL64, SCRAMABLED_SOBOL64.
    :param ndim: Number of dimension for the QRNG.
    :param offset: Offset to the random number stream.
    :param stream: CUDA stream.
    '''


    TEST                = binding.CURAND_RNG_TEST
    DEFAULT             = binding.CURAND_RNG_QUASI_DEFAULT
    SOBOL32             = binding.CURAND_RNG_QUASI_SOBOL32
    SCRAMBLED_SOBOL32   = binding.CURAND_RNG_QUASI_SCRAMBLED_SOBOL32
    SOBOL64             = binding.CURAND_RNG_QUASI_SOBOL64
    SCRAMBLED_SOBOL64   = binding.CURAND_RNG_QUASI_SCRAMBLED_SOBOL64

    @cuda.require_context
    def __init__(self, rndtype=DEFAULT, ndim=None, offset=None, stream=None):
        super(QRNG, self).__init__(binding.Generator(rndtype))
        self.rndtype = rndtype
        if ndim is not None:
            self.ndim = ndim
        if offset is not None:
            self.offset = offset
        if stream is not None:
            self.stream = stream

    @property
    def ndim(self, ndim):
        '''Mutatable attribute for number of dimension for the QRNG.
        '''
        return self.__ndim

    @ndim.setter
    def ndim(self, ndim):
        self.__ndim = ndim
        self._gen.set_quasi_random_generator_dimensions(ndim)

    def generate(self, ary, size=None):
        """Generate quasi random number in ary.

        :param ary: Numpy array or cuda device array.

        :param size: Number of samples;
                     Default to array size.  Must be multiple of ndim.
        """
        self._require_array(ary)
        size = size or ary.size
        dary, conv = cuda._auto_device(ary, stream=self.stream)
        self._gen.generate(dary, size)
        if conv:
            dary.copy_to_host(ary, stream=self.stream)


#
# Top level function entry points.
#

_global_rng = {}

def _get_prng():
    key = 'prng'
    prng = _global_rng.get(key)
    if not prng:
        prng = PRNG()
        prng.seed = int(time.time())
        _global_rng[key] = prng
    return prng


def _get_qrng(bits):
    assert bits in (32, 64), "not 32 or 64 bit"
    key = 'qrng%d' % bits
    qrng = _global_rng.get(key)
    if not qrng:
        qrng = QRNG(rndtype=getattr(QRNG, 'SOBOL%d' % bits))
        _global_rng[key] = qrng
    return qrng

def uniform(size, dtype=np.float, device=False):
    '''Generate floating point random number sampled
    from a uniform distribution

    :param size: Number of samples.
    :param dtype: np.float32 or np.float64.
    :param device: Set to True to return a device array instead or numpy array.

    :returns: A numpy array or a device array.

    >>> from pyculib import rand
    >>> rand.uniform(size=10)
    array([...])

    .. seealso:: :py:meth:`pyculib.rand.PRNG.uniform`
    '''
    ary = np.empty(size, dtype=dtype)
    devary = cuda.to_device(ary, copy=False)
    prng = _get_prng()
    prng.uniform(devary, size)
    if device:
        return devary
    else:
        devary.copy_to_host(ary)
        return ary

def normal(mean, sigma, size, dtype=np.float, device=False):
    '''Generate floating point random number sampled
    from a normal distribution

    :param mean: Center point of the distribution.
    :param sigma: Standard deviation of the distribution.
    :param size: --- Number of samples.
    :param dtype: np.float32 or np.float64.
    :param device: Set to True to return a device array instead or ndarray.
    :returns: A numpy array or a device array.

    >>> from pyculib import rand
    >>> rand.normal(mean=0, sigma=1, size=10)
    array([...])

    .. seealso:: :py:meth:`pyculib.rand.PRNG.normal`

    '''
    ary = np.empty(size, dtype=dtype)
    devary = cuda.to_device(ary, copy=False)
    prng = _get_prng()
    prng.normal(devary, mean, sigma, size)
    if device:
        return devary
    else:
        devary.copy_to_host(ary)
        return ary

def lognormal(mean, sigma, size, dtype=np.float, device=False):
    '''Generate floating point random number sampled
    from a log-normal distribution.

    :param mean: Center point of the distribution.
    :param sigma: Standard deviation of the distribution.
    :param size: Number of samples.
    :param dtype: np.float32 or np.float64.
    :param device: set to True to return a device array instead or ndarray.
    :returns: A numpy array or a device array.

    >>> from pyculib import rand
    >>> rand.lognormal(mean=0, sigma=1, size=10)
    array([...])

    .. seealso:: :py:meth:`pyculib.rand.PRNG.lognormal`

    '''
    ary = np.empty(size, dtype=dtype)
    devary = cuda.to_device(ary, copy=False)
    prng = _get_prng()
    prng.lognormal(devary, mean, sigma, size)
    if device:
        return devary
    else:
        devary.copy_to_host(ary)
        return ary

def poisson(lmbd, size, device=False):
    '''Generate int32 random number sampled
    from a poisson distribution.

    :param lmbda: Lambda of the distribution.
    :param size:  Number of samples
    :param device: Set to True to return a device array instead or ndarray.
    :returns: A numpy array or a device array.

    >>> from pyculib import rand
    >>> rand.poisson(lmbd=1, size=10)
    array([...], dtype=uint32)

    .. seealso:: :py:meth:`pyculib.rand.PRNG.poisson`
    '''
    ary = np.empty(size, dtype=np.uint32)
    devary = cuda.to_device(ary, copy=False)
    prng = _get_prng()
    prng.poisson(devary, lmbd, size)
    if device:
        return devary
    else:
        devary.copy_to_host(ary)
        return ary

def quasi(size, bits=32, nd=1, device=False):
    '''Generate quasi random number using SOBOL{bits} RNG type.

    :param size: Number of samples.
    :param bits: Bit length of output element; e.g. 32 or 64.
    :param nd: Number of dimension .
    :param device: Set to True to return a device array instead or ndarray.
    :returns: A numpy array or a device array.

    >>> from pyculib import rand
    >>> rand.quasi(10)
    array([...], dtype=uint32)

    .. seealso:: :py:meth:`pyculib.rand.QRNG.generate`
    '''
    if bits == 64:
        dtype = np.uint64
    elif bits == 32:
        dtype = np.uint32
    else:
        raise ValueError("Only accept bits = 32 or 64")
    ary = np.empty(size, dtype=dtype)
    devary = cuda.to_device(ary, copy=False)
    qrng = _get_qrng(bits)
    qrng.ndim = nd
    qrng.generate(devary, size)
    if device:
        return devary
    else:
        devary.copy_to_host(ary)
        return ary
