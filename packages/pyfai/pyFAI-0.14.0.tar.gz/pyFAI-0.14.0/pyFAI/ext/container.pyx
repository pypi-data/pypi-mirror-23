# -*- coding: utf-8 -*-
#
#    Project: Azimuthal integration
#             https://github.com/silx-kit/pyFAI 
#
#    Copyright 2013-2016 (C) European Synchrotron Radiation Facility, Grenoble, France
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#  .
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#  .
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

from __future__ import absolute_import, print_function, division, with_statement

__authors__ = ["Jerome Kieffer"]
__contact__ = "jerome.kieffer@esrf.eu"
__license__ = "MIT"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "19/06/2017"
__status__ = "development"
__doc__ = """Module containing Cython classes to build LUT"""

import numpy 
cimport numpy as cnp

cdef int SIZE = 10

cdef class Vector:
    cdef:
        readonly float[:] coef
        readonly int[:] idx
        readonly int size, allocated

    def __cinit__(self, int min_size=10):
        self.allocated = min_size
        self.coef = numpy.empty(self.allocated, dtype=numpy.float32)
        self.idx = numpy.empty(self.allocated, dtype=numpy.int32)
        self.size = 0

    def __dealloc__(self):
        self.coef = self.idx = None

    def __len__(self):
        return self.size

    def get_data(self):
        return numpy.asarray(self.idx[:self.size]), numpy.asarray(self.coef[:self.size])

    cpdef void append(self, int idx, float coef):
        cdef:
            int new_allocated 
            int[:] newidx
            float[:] newcoef
        if self.size >= self.allocated - 1:
                new_allocated = self.allocated * 2
                newcoef = numpy.empty(new_allocated, dtype=numpy.float32)
                newcoef[:self.size] = self.coef[:self.size]
                self.coef = newcoef
                newidx = numpy.empty(new_allocated, dtype=numpy.int32)
                newidx[:self.size] = self.idx[:self.size]
                self.idx = newidx
                self.allocated = new_allocated
        self.coef[self.size] = coef
        self.idx[self.size] = idx
        self.size = self.size + 1

cdef class ArrayLUT:
    cdef:
        readonly int size 
        readonly list lines
        
    def __cinit__(self, int nlines, min_size=10):
        cdef int i
        self.lines = [Vector(min_size=min_size) for i in range(nlines)]
        self.size = nlines
            
    def __dealloc__(self):
        while self.lines.__len__():
            self.lines.pop()
        self.lines = None
        
    def __len__(self):
        return len(self.lines)
    
    cpdef void append(self, int line, int col, float value):
        cdef: 
            Vector2 vector
        vector = self.lines[line]
        vector.append(col, value)

    def as_LUT(self):
        cdef:
            int i, max_size = 0
            int[:] local_idx
            float[:] local_coef
            lut_point[:, :] lut
            Vector2 vector
        for i in range(len(self.lines)):
            if len(self.lines[i]) > max_size:
                max_size = len(self.lines[i])
        lut = numpy.zeros((len(self.lines), max_size), dtype=dtype_lut)
        for i in range(len(self.lines)):
            vector = self.lines[i]
            local_idx, local_coef = vector.get_data()
            for j in range(len(vector)):
                lut[i, j] = lut_point(local_idx[j], local_coef[j])
        return numpy.asarray(lut, dtype=dtype_lut)

    def as_CSR(self):
        cdef:
            int i, val, start, end, total_size = 0 
            Vector2 vector
            lut_point[:, :] lut
            lut_point[:] data
            int[:] idptr, idx, local_idx
            float[:] coef, local_coef
        idptr = numpy.zeros(len(self.lines) + 1, dtype=numpy.int32)
        for i in range(len(self.lines)):
            total_size += len(self.lines[i])
            idptr[i + 1] = total_size
        coef = numpy.zeros(total_size, dtype=numpy.float32)
        idx = numpy.zeros(total_size, dtype=numpy.int32)
        for i in range(len(self.lines)):
            vector = self.lines[i]
            local_idx, local_coef = vector.get_data()
            start = idptr[i]
            end = start + len(vector)
            idx[start:end] = local_idx
            coef[start:end] = local_coef
        return numpy.asarray(idptr), numpy.asarray(idx), numpy.asarray(coef)
