from __future__ import print_function, absolute_import
import numpy as np
import scipy.sparse
import unittest
from .base import CUDATestCase


class TestCuSparseLevel1(CUDATestCase):
    def setUp(self):
        from pyculib.sparse import Sparse
        self.cus = Sparse()

    def tearDown(self):
        del self.cus

    def generic_test_axpyi(self, dtype):
        alpha = 2
        xval = np.arange(5, dtype=dtype) + 1
        xind = np.arange(xval.size, dtype='int32') * 2
        y = np.zeros(shape=xval.size * 2, dtype=xval.dtype)
        self.cus.axpyi(alpha, xval, xind, y)
        self.assertTrue(np.allclose(y[xind], (xval * 2)))

    def test_Saxpyi(self):
        self.generic_test_axpyi(dtype=np.float32)

    def test_Daxpyi(self):
        self.generic_test_axpyi(dtype=np.float64)

    def test_Caxpyi(self):
        self.generic_test_axpyi(dtype=np.complex64)

    def test_Zaxpyi(self):
        self.generic_test_axpyi(dtype=np.complex128)

    def generic_test_doti(self, dtype):
        xval = np.arange(5, dtype=dtype) + 1
        xind = np.arange(xval.size, dtype='int32') * 2
        y = np.ones(shape=xval.size * 2, dtype=xval.dtype)
        result = self.cus.doti(xval, xind, y)
        self.assertTrue(result)

    def test_Sdoti(self):
        self.generic_test_doti(dtype=np.float32)

    def test_Zdoti(self):
        self.generic_test_doti(dtype=np.complex128)

    def generic_test_dotci(self, dtype):
        xval = np.arange(5, dtype=dtype) + 1
        xind = np.arange(xval.size, dtype='int32') * 2
        y = np.ones(shape=xval.size * 2, dtype=xval.dtype)
        result = self.cus.dotci(xval, xind, y)
        self.assertTrue(result)

    def test_Zdotci(self):
        self.generic_test_dotci(dtype=np.complex128)

    def generic_test_gthr(self, dtype):
        xval = np.arange(5, dtype=dtype) + 1
        xind = np.arange(xval.size, dtype='int32') * 2
        y = np.ones(shape=xval.size * 2, dtype=xval.dtype)
        self.cus.gthr(y, xval, xind)
        self.assertTrue(np.all(xval == 1))

    def test_Sgthr(self):
        self.generic_test_gthr(dtype=np.float32)

    def test_Cgthr(self):
        self.generic_test_gthr(dtype=np.complex64)

    def generic_test_gthrz(self, dtype):
        xval = np.arange(5, dtype=dtype) + 1
        xind = np.arange(xval.size, dtype='int32') * 2
        y = np.ones(shape=xval.size * 2, dtype=xval.dtype)
        self.cus.gthrz(y, xval, xind)
        self.assertTrue(np.all(xval == 1))
        self.assertTrue(np.all(y[xind] == 0))

    def test_Dgthr(self):
        self.generic_test_gthrz(dtype=np.float64)

    def test_Zgthr(self):
        self.generic_test_gthrz(dtype=np.complex128)

    def generic_test_roti(self, dtype):
        xval = np.arange(5, dtype=dtype) + 1
        xind = np.arange(xval.size, dtype='int32') * 2
        y = np.ones(shape=xval.size * 2, dtype=xval.dtype)
        c = .2
        s = .3
        oldxval = xval.copy()
        oldy = y.copy()
        self.cus.roti(xval, xind, y, c, s)
        self.assertFalse(np.all(oldxval == xval))
        self.assertFalse(np.all(oldy == y))

    def test_Sroti(self):
        self.generic_test_roti(dtype=np.float32)

    def test_Droti(self):
        self.generic_test_roti(dtype=np.float64)

    def generic_test_sctr(self, dtype):
        xval = np.arange(5, dtype=dtype) + 1
        xind = np.arange(xval.size, dtype='int32') * 2
        y = np.ones(shape=xval.size * 2, dtype=xval.dtype)
        oldy = y.copy()
        self.cus.sctr(xval, xind, y)
        self.assertFalse(np.all(oldy == y))

    def test_Ssctr(self):
        self.generic_test_sctr(dtype=np.float32)

    def test_Csctr(self):
        self.generic_test_sctr(dtype=np.complex64)


class TestCuSparseMatrixOp(CUDATestCase):
    def test_bsr_matrix(self):
        from pyculib.sparse import bsr_matrix
        row = np.array([0, 0, 1, 2, 2, 2])
        col = np.array([0, 2, 2, 0, 1, 2])
        data = np.array([1, 2, 3, 4, 5, 6])
        expect = scipy.sparse.bsr_matrix((data, (row, col)), shape=(3, 3))
        mat = bsr_matrix((data, (row, col)), shape=(3, 3))
        host = mat.copy_to_host()
        self.assertTrue(np.all(host.indices == expect.indices))
        self.assertTrue(np.all(host.indptr == expect.indptr))
        self.assertTrue(np.all(host.data == expect.data))

    def test_matdescr(self):
        from pyculib.sparse import Sparse
        sparse = Sparse()
        md = sparse.matdescr()
        md.diagtype = 'N'
        md.fillmode = 'L'
        md.indexbase = 0
        md.matrixtype = 'G'

        self.assertEqual('N', md.diagtype)
        self.assertEqual('L', md.fillmode)
        self.assertEqual(0, md.indexbase)
        self.assertEqual('G', md.matrixtype)
        del md


class TestCuSparseLevel2(CUDATestCase):
    def setUp(self):
        from pyculib.sparse import Sparse
        self.cus = Sparse()

    def generic_test_bsrmv(self, dtype):
        from pyculib.sparse import bsr_matrix

        row = np.array([0, 0, 1, 2, 2, 2])
        col = np.array([0, 2, 2, 0, 1, 2])
        data = np.array([1, 2, 3, 4, 5, 6], dtype=dtype)

        bsrmat = bsr_matrix((data, (row, col)), shape=(3, 3))
        x = np.ones(3, dtype=dtype)
        y = np.ones(3, dtype=dtype)
        oldy = y.copy()

        alpha = 1
        beta = 1
        descr = self.cus.matdescr()
        self.cus.bsrmv_matrix('C', 'N', alpha, descr, bsrmat, x, beta, y)

        self.assertFalse(np.all(y == oldy))

    def test_Sbsrmv(self):
        dtype = np.float32
        self.generic_test_bsrmv(dtype=dtype)

    def test_Cbsrmv(self):
        dtype = np.complex64
        self.generic_test_bsrmv(dtype=dtype)

    def test_Sbsrxmv(self):
        """
        Just exercise the codepath
        """
        dtype = np.float32
        alpha = 0
        beta = 0
        descr = self.cus.matdescr()
        bsrVal = np.zeros(10, dtype=dtype)
        bsrMaskPtr = np.zeros(10, dtype=np.int32)
        bsrRowPtr = np.zeros(10, dtype=np.int32)
        bsrEndPtr = np.zeros(10, dtype=np.int32)
        bsrColInd = np.zeros(10, dtype=np.int32)
        blockDim = 1
        x = np.zeros(10, dtype=dtype)
        y = np.zeros(10, dtype=dtype)
        self.cus.bsrxmv('C', 'N', 1, 1, 1, 1, alpha, descr, bsrVal,
                        bsrMaskPtr, bsrRowPtr, bsrEndPtr, bsrColInd,
                        blockDim, x, beta, y)

    def test_Scsrmv(self):
        """
        Just exercise the codepath
        """
        dtype = np.float32
        alpha = 0
        beta = 0
        descr = self.cus.matdescr()
        csrVal = np.zeros(10, dtype=dtype)
        csrColInd = np.zeros(10, dtype=np.int32)
        csrRowPtr = np.zeros(10, dtype=np.int32)
        x = np.zeros(10, dtype=dtype)
        y = np.zeros(10, dtype=dtype)
        trans = 'N'
        m = 1
        n = 1
        nnz = 1
        self.cus.csrmv(trans, m, n, nnz, alpha, descr, csrVal, csrRowPtr,
                       csrColInd, x, beta, y)

    def test_Scsrmv(self):
        """
        Just exercise the codepath
        """
        dtype = np.float32

        descr = self.cus.matdescr()
        csrVal = np.zeros(10, dtype=dtype)
        csrColInd = np.zeros(10, dtype=np.int32)
        csrRowPtr = np.zeros(10, dtype=np.int32)
        trans = 'N'
        m = 1
        nnz = 1
        info = self.cus.csrsv_analysis(trans, m, nnz, descr, csrVal,
                                       csrRowPtr, csrColInd)

        alpha = 1.0
        x = np.zeros(10, dtype=dtype)
        y = np.zeros(10, dtype=dtype)
        self.cus.csrsv_solve(trans, m, alpha, descr, csrVal, csrRowPtr,
                             csrColInd, info, x, y)


class TestCuSparseLevel3(CUDATestCase):
    def setUp(self):
        from pyculib.sparse import Sparse
        self.cus = Sparse()

    def test_Scsrmm(self):
        """
        Just exercise the codepath
        """
        dtype = np.float32

        descrA = self.cus.matdescr()
        B = C = csrValA = np.zeros(10, dtype=dtype)
        csrColIndA = np.zeros(10, dtype=np.int32)
        csrRowPtrA = np.zeros(10, dtype=np.int32)
        ldb = 1
        ldc = 1
        m = 1
        n = 1
        k = 1
        nnz = 1
        alpha = 1
        beta = 1
        transA = 'N'
        self.cus.csrmm(transA, m, n, k, nnz, alpha, descrA, csrValA,
                       csrRowPtrA, csrColIndA, B, ldb, beta, C, ldc)

    def test_Ccsrmm(self):
        """
        Just exercise the codepath
        """
        dtype = np.complex64

        descrA = self.cus.matdescr()
        B = C = csrValA = np.zeros(10, dtype=dtype)
        csrColIndA = np.zeros(10, dtype=np.int32)
        csrRowPtrA = np.zeros(10, dtype=np.int32)
        ldb = 1
        ldc = 1
        m = 1
        n = 1
        k = 1
        nnz = 1
        alpha = 1
        beta = 1
        transA = transB = 'N'
        self.cus.csrmm2(transA, transB, m, n, k, nnz, alpha, descrA,
                        csrValA,
                        csrRowPtrA, csrColIndA, B, ldb, beta, C, ldc)

    def test_Scsrsm(self):
        """
        Just exercise the codepath
        """
        dtype = np.float32

        descrA = self.cus.matdescr()
        X = Y = csrValA = np.zeros(10, dtype=dtype)
        csrColIndA = np.zeros(10, dtype=np.int32)
        csrRowPtrA = np.zeros(10, dtype=np.int32)
        m = 1
        n = 1
        nnz = 1
        transA = 'N'
        info = self.cus.csrsm_analysis(transA, m, nnz, descrA, csrValA,
                                       csrRowPtrA, csrColIndA)
        alpha = 1
        ldx = 1
        ldy = 1
        self.cus.csrsm_solve(transA, m, n, alpha, descrA, csrValA,
                             csrRowPtrA, csrColIndA, info, X, ldx, Y, ldy)


class TestCuSparseExtra(CUDATestCase):
    def setUp(self):
        from pyculib.sparse import Sparse
        self.cus = Sparse()

    def test_XcsrgeamNnz(self):
        """
        Just exercise the codepath
        """
        m = n = 1
        nnzA = 1
        nnzB = 1
        descrA = descrB = descrC = self.cus.matdescr()
        csrColIndA = csrColIndB = np.zeros(10, dtype=np.int32)
        csrRowPtrA = csrRowPtrB = csrRowPtrC = np.zeros(10, dtype=np.int32)
        nnzC = self.cus.XcsrgeamNnz(m, n, descrA, nnzA, csrRowPtrA, csrColIndA,
                                    descrB, nnzB, csrRowPtrB, csrColIndB,
                                    descrC,
                                    csrRowPtrC)
        self.assertTrue(isinstance(nnzC, int))

    def test_Scsrgeam(self):
        """
        Just exercise the codepath
        """
        dtype = np.float32
        m = n = 1
        nnzA = 1
        nnzB = 1
        alpha = beta = 1
        csrValA = csrValB = csrValC = np.zeros(10, dtype=dtype)
        descrA = descrB = descrC = self.cus.matdescr()
        csrColIndA = csrColIndB = csrColIndC = np.zeros(10, dtype=np.int32)
        csrRowPtrA = csrRowPtrB = csrRowPtrC = np.zeros(10, dtype=np.int32)
        self.cus.csrgeam(m, n, alpha, descrA, nnzA, csrValA, csrRowPtrA,
                         csrColIndA, beta, descrB, nnzB, csrValB,
                         csrRowPtrB, csrColIndB, descrC, csrValC,
                         csrRowPtrC, csrColIndC)


    def test_XcsrgemmNnz(self):
        """
        Just exercise the codepath
        """
        m = n = k = 1
        nnzA = 1
        nnzB = 1
        descrA = descrB = descrC = self.cus.matdescr()
        csrColIndA = csrColIndB = np.zeros(10, dtype=np.int32)
        csrRowPtrA = csrRowPtrB = csrRowPtrC = np.zeros(10, dtype=np.int32)
        transA = transB = 'N'
        nnzC = self.cus.XcsrgemmNnz(transA, transB, m, n, k, descrA, nnzA,
                                    csrRowPtrA,
                                    csrColIndA, descrB, nnzB, csrRowPtrB,
                                    csrColIndB, descrC,
                                    csrRowPtrC)
        self.assertTrue(isinstance(nnzC, int))

    def test_Scsrgemm(self):
        """
        Just exercise the codepath
        """
        dtype = np.float32
        m = n = k = 0
        transA = transB = 'N'
        nnzA = 0
        nnzB = 0
        csrValA = csrValB = csrValC = np.zeros(10, dtype=dtype)
        descrA = descrB = descrC = self.cus.matdescr()
        csrColIndA = csrColIndB = csrColIndC = np.zeros(10, dtype=np.int32)
        csrRowPtrA = csrRowPtrB = csrRowPtrC = np.zeros(10, dtype=np.int32)
        self.cus.csrgemm(transA, transB, m, n, k, descrA, nnzA, csrValA,
                         csrRowPtrA, csrColIndA, descrB, nnzB, csrValB,
                         csrRowPtrB,
                         csrColIndB, descrC, csrValC, csrRowPtrC, csrColIndC)

    def test_csrgemm_ez(self):
        from pyculib.sparse import CudaSparseMatrix
        from scipy.sparse import csr_matrix

        def random_square_csr_matrix(N):
            X = np.random.random((N, N))
            X[X > 0.7] = 0
            return csr_matrix(X)

        a = random_square_csr_matrix(10)
        b = random_square_csr_matrix(10)
        a_cuda = CudaSparseMatrix().from_host_matrix(a)
        b_cuda = CudaSparseMatrix().from_host_matrix(b)
        c_cuda = self.cus.csrgemm_ez(a, b)
        c_host = c_cuda.copy_to_host()
        c_gold = a * b
        # Conversion to dense necessary because Scipy and cuSPARSE order their
        # indices differently
        np.testing.assert_allclose(c_gold.toarray(), c_host.toarray())


class TestCuSparsePreconditioners(CUDATestCase):
    def setUp(self):
        from pyculib.sparse import Sparse
        self.cus = Sparse()

    def test_Scsric0(self):
        """
        Just exercise the codepath
        """
        dtype = np.float32

        m = n = 3
        trans = 'N'

        sary = scipy.sparse.rand(m, n, 0.75, format='csr', dtype=dtype)
        nnz = sary.nnz
        csrValM = sary.data
        csrRowPtrA = sary.indptr
        csrColIndA = sary.indices

        descr = self.cus.matdescr(matrixtype='S')
        info = self.cus.csrsv_analysis(trans, m, nnz, descr, csrValM,
                                       csrRowPtrA, csrColIndA)
        self.cus.csric0(trans, m, descr, csrValM, csrRowPtrA,
                        csrColIndA, info)

    def test_Scsrilu0(self):
        """
        Just exercise the codepath
        """
        dtype = np.float32

        m = n = 3
        trans = 'N'

        sary = scipy.sparse.rand(m, n, 0.75, format='csr', dtype=dtype)
        csrValM = sary.data
        csrRowPtrA = sary.indptr
        csrColIndA = sary.indices

        descr = self.cus.matdescr()
        info = self.cus.api.solve_analysis_info()
        self.cus.csrilu0(trans, m, descr, csrValM, csrRowPtrA,
                         csrColIndA, info)

    def test_Sgtsv(self):
        """
        Just exercise the codepath
        """
        dtype = np.float32

        m = 4
        n = 3
        ldb = m
        dl = np.asarray([3] * 8, dtype=dtype)
        d = np.asarray([1] * 9, dtype=dtype)
        du = np.asarray([4] * 8, dtype=dtype)
        B = np.ones((m, n), dtype=dtype, order='F')
        Bcopy = B.copy()
        self.cus.gtsv(m, n, dl, d, du, B, ldb)
        self.assertTrue(not np.all(B == Bcopy))

    def test_Sgtsv_nopivot(self):
        """
        Just exercise the codepath
        """
        dtype = np.float32

        m = 4
        n = 3
        ldb = m
        dl = np.asarray([3] * 8, dtype=dtype)
        d = np.asarray([1] * 9, dtype=dtype)
        du = np.asarray([4] * 8, dtype=dtype)
        B = np.ones((m, n), dtype=dtype, order='F')
        Bcopy = B.copy()
        self.cus.gtsv_nopivot(m, n, dl, d, du, B, ldb)
        self.assertTrue(not np.all(B == Bcopy))

    def test_SgtsvStridedBatch(self):
        """
        Just exercise the codepath
        """
        dtype = np.float32

        batchCount = 1
        batchStride = 4

        m = 4
        n = 3
        dl = np.asarray([3] * 8, dtype=dtype)
        d = np.asarray([1] * 9, dtype=dtype)
        du = np.asarray([4] * 8, dtype=dtype)
        x = np.ones((m, n), dtype=dtype, order='F')
        xcopy = x.copy()
        self.cus.gtsvStridedBatch(m, dl, d, du, x, batchCount, batchStride)
        self.assertTrue(not np.all(x == xcopy))


class TestCuSparseFormatConversion(CUDATestCase):
    """
    These test can corrupt the CUDA context making the remaining test fails
    """

    def setUp(self):
        from pyculib.sparse import Sparse
        self.cus = Sparse()

    def tearDown(self):
        del self.cus

    def test_Sbsr2csr(self):
        dtype = np.dtype('float32')

        dirA = 'C'
        mb = nb = 0
        descrA = self.cus.matdescr()
        descrC = self.cus.matdescr()
        bsrValA = csrValC = np.zeros(10, dtype=dtype)
        bsrRowPtrA = bsrColIndA = np.zeros(10, dtype=np.int32)
        csrRowPtrC = csrColIndC = np.zeros(10, dtype=np.int32)
        blockDim = 1
        self.cus.bsr2csr(dirA, mb, nb, descrA, bsrValA, bsrRowPtrA,
                         bsrColIndA, blockDim, descrC, csrValC,
                         csrRowPtrC, csrColIndC)

    def test_Xcoo2csr(self):
        nnz = 1
        m = 1
        csrRowPtr = np.zeros(20, dtype=np.int32)
        cooRowInd = np.zeros(20, dtype=np.int32)
        self.cus.Xcoo2csr(cooRowInd, nnz, m, csrRowPtr)

    def test_Scsc2dense(self):
        m = n = 1
        lda = 1
        descrA = self.cus.matdescr()
        cscValA = np.zeros(10, dtype=np.float32)
        cscRowIndA = cscColPtrA = A = np.zeros(10, dtype=np.int32)
        self.cus.csc2dense(m, n, descrA, cscValA, cscRowIndA, cscColPtrA, A,
                           lda)

    def test_Xcsr2bsrNnz(self):
        dirA = 'C'
        m = n = 1
        blockDim = 1
        descrC = descrA = self.cus.matdescr()
        bsrRowPtrC = csrRowPtrA = csrColIndA = np.zeros(10, dtype=np.int32)
        self.cus.Xcsr2bsrNnz(dirA, m, n, descrA, csrRowPtrA, csrColIndA,
                             blockDim, descrC, bsrRowPtrC)

    def test_Scsr2bsr(self):
        dtype = np.float32

        dirA = 'C'
        m = n = 1
        blockDim = 1
        descrC = descrA = self.cus.matdescr()
        csrValA = bsrColIndC = bsrValC = np.zeros(10, dtype=dtype)
        bsrRowPtrC = csrRowPtrA = csrColIndA = np.zeros(10, dtype=np.int32)
        self.cus.csr2bsr(dirA, m, n, descrA, csrValA, csrRowPtrA, csrColIndA,
                         blockDim, descrC, bsrValC, bsrRowPtrC, bsrColIndC)

    def test_Xcsr2coo(self):
        nnz = m = 1
        csrRowPtr = cooRowInd = np.zeros(10, dtype=np.int32)
        self.cus.Xcsr2coo(csrRowPtr, nnz, m, cooRowInd)

    def test_Scsr2csc(self):
        dtype = np.float32
        m = n = nnz = 1
        csrVal = cscVal = np.zeros(10, dtype=dtype)
        csrRowPtr = csrColInd = np.zeros(10, dtype=np.int32)
        cscRowInd = cscColPtr = np.zeros(10, dtype=np.int32)
        copyValues = 'N'
        self.cus.csr2csc(m, n, nnz, csrVal, csrRowPtr, csrColInd, cscVal,
                         cscRowInd, cscColPtr, copyValues)

    def test_Scsr2dense(self):
        dtype = np.float32

        m = n = 1
        lda = 1
        descrA = self.cus.matdescr()
        A = csrValA = np.zeros(10, dtype=dtype)
        csrRowPtrA = csrColIndA = np.zeros(10, np.int32)
        self.cus.csr2dense(m, n, descrA, csrValA, csrRowPtrA, csrColIndA, A,
                           lda)

    def test_Sdense2csc(self):
        dtype = np.float32
        
        m = n = 2
        lda = m
        nnzPerCol = np.ones(n, np.int32) * 2
        descrA = self.cus.matdescr()
        A = np.ones(n, dtype=dtype)
        cscValA = np.zeros(10, dtype=dtype)
        cscRowIndA = np.zeros(10, np.int32)
        cscColPtrA = np.zeros(10, np.int32)

        self.cus.dense2csc(m, n, descrA, A, lda, nnzPerCol, cscValA,
                           cscRowIndA, cscColPtrA)

    def test_Sdense2csr(self):
        dtype = np.float32

        m = n = 2
        lda = m
        nnzPerRow = np.ones(n, np.int32) * 2
        descrA = self.cus.matdescr()
        A = np.ones(10, dtype=dtype)
        csrValA = np.zeros(10, dtype=dtype)
        csrRowPtrA = csrColIndA = np.zeros(10, np.int32)
        self.cus.dense2csr(m, n, descrA, A, lda, nnzPerRow, csrValA,
                           csrRowPtrA, csrColIndA)

    def test_Snnz(self):
        dtype = np.float32
        dirA = 'C'
        m = n = 2
        lda = m
        descrA = self.cus.matdescr()
        A = np.ones(10, dtype=dtype)
        nnzPerRowColumn = np.zeros(10, np.int32)
        self.cus.nnz(dirA, m, n, descrA, A, lda, nnzPerRowColumn)


def test():
    import sys
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    mod = sys.modules[__name__]
    for name in dir(mod):
        if name.startswith('Test'):
            test_class = getattr(mod, name)
            tests = loader.loadTestsFromTestCase(test_class)
            suite.addTests(tests)
    runner = unittest.runner.TextTestRunner()
    return runner.run(suite)

test_cases = (TestCuSparseLevel1, TestCuSparseMatrixOp, TestCuSparseLevel2,
              TestCuSparseLevel3, TestCuSparseExtra,
              TestCuSparsePreconditioners, TestCuSparseFormatConversion)


if __name__ == '__main__':
    unittest.main()
