/* *********************************************************************/
/**
* Copyright (c) 2017 Mimer Information Technology
*
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in all
* copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
* SOFTWARE.
*
* See license for more details.
 */
/* *********************************************************************/

#include "mimmicroapi.h"
#include "Python.h"

#define BUFLEN 128

static PyObject* mimerBeginStatementC(PyObject* self, PyObject* args);
static PyObject* mimerEndStatement(PyObject* self, PyObject* args);
static PyObject* mimerOpenCursor(PyObject* self, PyObject* args);
static PyObject* mimerCloseCursor(PyObject* self, PyObject* args);
static PyObject* mimerExecuteStatementC(PyObject* self, PyObject* args);
static PyObject* mimerExecute(PyObject* self, PyObject* args);
static PyObject* mimerParameterCount(PyObject* self, PyObject* args);
static PyObject* mimerParameterType(PyObject* self, PyObject* args);
static PyObject* mimerColumnCount(PyObject* self, PyObject* args);
static PyObject* mimerFetch(PyObject* self, PyObject* args);
static PyObject* mimerGetInt32(PyObject* self, PyObject* args);
static PyObject* mimerGetInt64(PyObject* self, PyObject* args);
static PyObject* mimerColumnType(PyObject* self, PyObject* args);
static PyObject* mimerGetStringC(PyObject* self, PyObject* args);
static PyObject* mimerGetDouble(PyObject* self, PyObject* args);
static PyObject* mimerSetInt32(PyObject* self, PyObject* args);
static PyObject* mimerSetInt64(PyObject* self, PyObject* args);
static PyObject* mimerSetDouble(PyObject* self, PyObject* args);
static PyObject* mimerSetStringC(PyObject* self, PyObject* args);
static PyObject* mimerGetErrorC(PyObject* self, PyObject* args);
static PyObject* mimerSetBlobData(PyObject* self, PyObject* args);
static PyObject* mimerGetBlobData(PyObject* self, PyObject* args);
static PyObject* mimerSetNclobDataC(PyObject* self, PyObject* args);
static PyObject* mimerGetNclobDataC(PyObject* self, PyObject* args);
static PyObject* mimerSetBinary(PyObject* self, PyObject* args);
static PyObject* mimerSetBoolean(PyObject* self, PyObject* args);
static PyObject* mimerGetBoolean(PyObject* self, PyObject* args);
static PyObject* mimerSetNull(PyObject* self, PyObject* args);
static PyObject* mimerColumnNameC(PyObject* self, PyObject* args);
static PyObject* mimerGetBinary(PyObject* self, PyObject* args);
