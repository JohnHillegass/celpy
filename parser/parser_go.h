/* Code generated by cmd/cgo; DO NOT EDIT. */

/* package _/Users/johnhillegass/Desktop/py-cel/parser */


#line 1 "cgo-builtin-export-prolog"

#include <stddef.h> /* for ptrdiff_t below */

#ifndef GO_CGO_EXPORT_PROLOGUE_H
#define GO_CGO_EXPORT_PROLOGUE_H

#ifndef GO_CGO_GOSTRING_TYPEDEF
typedef struct { const char *p; ptrdiff_t n; } _GoString_;
#endif

#endif

/* Start of preamble from import "C" comments.  */


#line 9 "parser.go"





// #define Py_LIMITED_API // need full API for PyRun*
#include <Python.h>
typedef uint8_t bool;
// static inline is trick for avoiding need for extra .c file
// the following are used for build value -- switch on reflect.Kind
// or the types equivalent
static inline PyObject* gopy_build_bool(uint8_t val) {
	return Py_BuildValue("b", val);
}
static inline PyObject* gopy_build_int64(int64_t val) {
	return Py_BuildValue("k", val);
}
static inline PyObject* gopy_build_uint64(uint64_t val) {
	return Py_BuildValue("K", val);
}
static inline PyObject* gopy_build_float64(double val) {
	return Py_BuildValue("d", val);
}
static inline PyObject* gopy_build_string(const char* val) {
	return Py_BuildValue("s", val);
}
static inline void gopy_decref(PyObject* obj) { // macro
	Py_XDECREF(obj);
}
static inline void gopy_incref(PyObject* obj) { // macro
	Py_XINCREF(obj);
}
static inline int gopy_method_check(PyObject* obj) { // macro
	return PyMethod_Check(obj);
}
static inline void gopy_err_handle() {
	if(PyErr_Occurred() != NULL) {
		PyErr_Print();
	}
}


#line 1 "cgo-generated-wrapper"


/* End of preamble from import "C" comments.  */


/* Start of boilerplate cgo prologue.  */
#line 1 "cgo-gcc-export-header-prolog"

#ifndef GO_CGO_PROLOGUE_H
#define GO_CGO_PROLOGUE_H

typedef signed char GoInt8;
typedef unsigned char GoUint8;
typedef short GoInt16;
typedef unsigned short GoUint16;
typedef int GoInt32;
typedef unsigned int GoUint32;
typedef long long GoInt64;
typedef unsigned long long GoUint64;
typedef GoInt64 GoInt;
typedef GoUint64 GoUint;
typedef __SIZE_TYPE__ GoUintptr;
typedef float GoFloat32;
typedef double GoFloat64;
typedef float _Complex GoComplex64;
typedef double _Complex GoComplex128;

/*
  static assertion to make sure the file is being used on architecture
  at least with matching size of GoInt.
*/
typedef char _check_for_64_bit_pointer_matching_GoInt[sizeof(void*)==64/8 ? 1:-1];

#ifndef GO_CGO_GOSTRING_TYPEDEF
typedef _GoString_ GoString;
#endif
typedef void *GoMap;
typedef void *GoChan;
typedef struct { void *t; void *v; } GoInterface;
typedef struct { void *data; GoInt len; GoInt cap; } GoSlice;

#endif

/* End of boilerplate cgo prologue.  */

#ifdef __cplusplus
extern "C" {
#endif


extern void GoPyInit();

// DecRef decrements the reference count for the specified handle
// and deletes it it goes to zero.

extern void DecRef(long long int p0);

// IncRef increments the reference count for the specified handle.

extern void IncRef(long long int p0);

// NumHandles returns the number of handles currently in use.

extern GoInt NumHandles();

// --- wrapping slice: []bool ---

extern long long int Slice_bool_CTor();

extern GoInt Slice_bool_len(long long int p0);

extern char Slice_bool_elem(long long int p0, GoInt p1);

extern void Slice_bool_set(long long int p0, GoInt p1, char p2);

extern void Slice_bool_append(long long int p0, char p1);

// --- wrapping slice: []byte ---

extern long long int Slice_byte_CTor();

extern GoInt Slice_byte_len(long long int p0);

extern char Slice_byte_elem(long long int p0, GoInt p1);

extern void Slice_byte_set(long long int p0, GoInt p1, char p2);

extern void Slice_byte_append(long long int p0, char p1);

// --- wrapping slice: []float32 ---

extern long long int Slice_float32_CTor();

extern GoInt Slice_float32_len(long long int p0);

extern float Slice_float32_elem(long long int p0, GoInt p1);

extern void Slice_float32_set(long long int p0, GoInt p1, float p2);

extern void Slice_float32_append(long long int p0, float p1);

// --- wrapping slice: []float64 ---

extern long long int Slice_float64_CTor();

extern GoInt Slice_float64_len(long long int p0);

extern double Slice_float64_elem(long long int p0, GoInt p1);

extern void Slice_float64_set(long long int p0, GoInt p1, double p2);

extern void Slice_float64_append(long long int p0, double p1);

// --- wrapping slice: []int ---

extern long long int Slice_int_CTor();

extern GoInt Slice_int_len(long long int p0);

extern long long int Slice_int_elem(long long int p0, GoInt p1);

extern void Slice_int_set(long long int p0, GoInt p1, long long int p2);

extern void Slice_int_append(long long int p0, long long int p1);

// --- wrapping slice: []int16 ---

extern long long int Slice_int16_CTor();

extern GoInt Slice_int16_len(long long int p0);

extern short Slice_int16_elem(long long int p0, GoInt p1);

extern void Slice_int16_set(long long int p0, GoInt p1, short p2);

extern void Slice_int16_append(long long int p0, short p1);

// --- wrapping slice: []int32 ---

extern long long int Slice_int32_CTor();

extern GoInt Slice_int32_len(long long int p0);

extern long int Slice_int32_elem(long long int p0, GoInt p1);

extern void Slice_int32_set(long long int p0, GoInt p1, long int p2);

extern void Slice_int32_append(long long int p0, long int p1);

// --- wrapping slice: []int64 ---

extern long long int Slice_int64_CTor();

extern GoInt Slice_int64_len(long long int p0);

extern long long int Slice_int64_elem(long long int p0, GoInt p1);

extern void Slice_int64_set(long long int p0, GoInt p1, long long int p2);

extern void Slice_int64_append(long long int p0, long long int p1);

// --- wrapping slice: []int8 ---

extern long long int Slice_int8_CTor();

extern GoInt Slice_int8_len(long long int p0);

extern char Slice_int8_elem(long long int p0, GoInt p1);

extern void Slice_int8_set(long long int p0, GoInt p1, char p2);

extern void Slice_int8_append(long long int p0, char p1);

// --- wrapping slice: []rune ---

extern long long int Slice_rune_CTor();

extern GoInt Slice_rune_len(long long int p0);

extern long int Slice_rune_elem(long long int p0, GoInt p1);

extern void Slice_rune_set(long long int p0, GoInt p1, long int p2);

extern void Slice_rune_append(long long int p0, long int p1);

// --- wrapping slice: []string ---

extern long long int Slice_string_CTor();

extern GoInt Slice_string_len(long long int p0);

extern char* Slice_string_elem(long long int p0, GoInt p1);

extern void Slice_string_set(long long int p0, GoInt p1, char* p2);

extern void Slice_string_append(long long int p0, char* p1);

// --- wrapping slice: []uint ---

extern long long int Slice_uint_CTor();

extern GoInt Slice_uint_len(long long int p0);

extern long long unsigned int Slice_uint_elem(long long int p0, GoInt p1);

extern void Slice_uint_set(long long int p0, GoInt p1, long long unsigned int p2);

extern void Slice_uint_append(long long int p0, long long unsigned int p1);

// --- wrapping slice: []uint16 ---

extern long long int Slice_uint16_CTor();

extern GoInt Slice_uint16_len(long long int p0);

extern unsigned short Slice_uint16_elem(long long int p0, GoInt p1);

extern void Slice_uint16_set(long long int p0, GoInt p1, unsigned short p2);

extern void Slice_uint16_append(long long int p0, unsigned short p1);

// --- wrapping slice: []uint32 ---

extern long long int Slice_uint32_CTor();

extern GoInt Slice_uint32_len(long long int p0);

extern long unsigned int Slice_uint32_elem(long long int p0, GoInt p1);

extern void Slice_uint32_set(long long int p0, GoInt p1, long unsigned int p2);

extern void Slice_uint32_append(long long int p0, long unsigned int p1);

// --- wrapping slice: []uint64 ---

extern long long int Slice_uint64_CTor();

extern GoInt Slice_uint64_len(long long int p0);

extern long long unsigned int Slice_uint64_elem(long long int p0, GoInt p1);

extern void Slice_uint64_set(long long int p0, GoInt p1, long long unsigned int p2);

extern void Slice_uint64_append(long long int p0, long long unsigned int p1);

// --- wrapping slice: []uint8 ---

extern long long int Slice_uint8_CTor();

extern GoInt Slice_uint8_len(long long int p0);

extern unsigned char Slice_uint8_elem(long long int p0, GoInt p1);

extern void Slice_uint8_set(long long int p0, GoInt p1, unsigned char p2);

extern void Slice_uint8_append(long long int p0, unsigned char p1);

// --- wrapping slice: []*expr.Expr ---

extern long long int Slice_Ptr_expr_Expr_CTor();

extern GoInt Slice_Ptr_expr_Expr_len(long long int p0);

extern long long int Slice_Ptr_expr_Expr_elem(long long int p0, GoInt p1);

extern void Slice_Ptr_expr_Expr_set(long long int p0, GoInt p1, long long int p2);

extern void Slice_Ptr_expr_Expr_append(long long int p0, long long int p1);

// --- wrapping slice: []*expr.Expr_CreateStruct_Entry ---

extern long long int Slice_Ptr_expr_Expr_CreateStruct_Entry_CTor();

extern GoInt Slice_Ptr_expr_Expr_CreateStruct_Entry_len(long long int p0);

extern long long int Slice_Ptr_expr_Expr_CreateStruct_Entry_elem(long long int p0, GoInt p1);

extern void Slice_Ptr_expr_Expr_CreateStruct_Entry_set(long long int p0, GoInt p1, long long int p2);

extern void Slice_Ptr_expr_Expr_CreateStruct_Entry_append(long long int p0, long long int p1);

// --- wrapping slice: []parser.Macro ---

extern long long int Slice_parser_Macro_CTor();

extern GoInt Slice_parser_Macro_len(long long int p0);

extern long long int Slice_parser_Macro_elem(long long int p0, GoInt p1);

extern void Slice_parser_Macro_set(long long int p0, GoInt p1, long long int p2);

extern void Slice_parser_Macro_append(long long int p0, long long int p1);

// --- wrapping map: map[int64]*expr.Expr ---

extern long long int Map_int64_Ptr_expr_Expr_CTor();

extern GoInt Map_int64_Ptr_expr_Expr_len(long long int p0);

extern long long int Map_int64_Ptr_expr_Expr_elem(long long int p0, long long int p1);

extern char Map_int64_Ptr_expr_Expr_contains(long long int p0, long long int p1);

extern void Map_int64_Ptr_expr_Expr_set(long long int p0, long long int p1, long long int p2);

extern void Map_int64_Ptr_expr_Expr_delete(long long int p0, long long int p1);

extern long long int Map_int64_Ptr_expr_Expr_keys(long long int p0);

// --- wrapping map: map[int64]int32 ---

extern long long int Map_int64_int32_CTor();

extern GoInt Map_int64_int32_len(long long int p0);

extern long int Map_int64_int32_elem(long long int p0, long long int p1);

extern char Map_int64_int32_contains(long long int p0, long long int p1);

extern void Map_int64_int32_set(long long int p0, long long int p1, long int p2);

extern void Map_int64_int32_delete(long long int p0, long long int p1);

extern long long int Map_int64_int32_keys(long long int p0);

// ---- Global Variables: can only use functions to access ---

extern long long int parser_AllMacros();

extern void parser_Set_AllMacros(long long int p0);

extern long long int parser_NoMacros();

extern void parser_Set_NoMacros(long long int p0);

extern long long int parser_ExprHelper_Fold(long long int p0, char* p1, long long int p2, char* p3, long long int p4, long long int p5, long long int p6, long long int p7);

extern long long int parser_ExprHelper_Ident(long long int p0, char* p1);

extern long long int parser_ExprHelper_LiteralBool(long long int p0, char p1);

extern long long int parser_ExprHelper_LiteralBytes(long long int p0, long long int p1);

extern long long int parser_ExprHelper_LiteralDouble(long long int p0, double p1);

extern long long int parser_ExprHelper_LiteralInt(long long int p0, long long int p1);

extern long long int parser_ExprHelper_LiteralString(long long int p0, char* p1);

extern long long int parser_ExprHelper_LiteralUint(long long int p0, long long unsigned int p1);

extern long long int parser_ExprHelper_NewMapEntry(long long int p0, long long int p1, long long int p2);

extern long long int parser_ExprHelper_NewObjectFieldInit(long long int p0, char* p1, long long int p2);

extern long long int parser_ExprHelper_OffsetLocation(long long int p0, long long int p1);

extern long long int parser_ExprHelper_PresenceTest(long long int p0, long long int p1, char* p2);

extern long long int parser_ExprHelper_Select(long long int p0, long long int p1, char* p2);

extern long long int parser_Macro_ArgCount(long long int p0);

extern char* parser_Macro_Function(long long int p0);

extern char parser_Macro_IsReceiverStyle(long long int p0);

extern char* parser_Macro_MacroKey(long long int p0);

extern char* parser_Unparse(long long int p0, long long int p1);

#ifdef __cplusplus
}
#endif
