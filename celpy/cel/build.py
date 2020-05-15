# python build stubs for package cel
# File is generated by gopy. Do not edit.
# gopy pkg github.com/google/cel-go/cel

from pybindgen import retval, param, Module
import sys

mod = Module('_cel')
mod.add_include('"cel_go.h"')
mod.add_function('GoPyInit', None, [])
mod.add_function('DecRef', None, [param('int64_t', 'handle')])
mod.add_function('IncRef', None, [param('int64_t', 'handle')])
mod.add_function('NumHandles', retval('int'), [])
mod.add_function('Slice_bool_CTor', retval('int64_t'), [])
mod.add_function('Slice_bool_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_bool_elem', retval('bool'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_bool_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('bool', 'value')])
mod.add_function('Slice_bool_append', None, [param('int64_t', 'handle'), param('bool', 'value')])
mod.add_function('Slice_byte_CTor', retval('int64_t'), [])
mod.add_function('Slice_byte_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_byte_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_byte_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Slice_byte_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('Slice_float32_CTor', retval('int64_t'), [])
mod.add_function('Slice_float32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_float32_elem', retval('float'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_float32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('float', 'value')])
mod.add_function('Slice_float32_append', None, [param('int64_t', 'handle'), param('float', 'value')])
mod.add_function('Slice_float64_CTor', retval('int64_t'), [])
mod.add_function('Slice_float64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_float64_elem', retval('double'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_float64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('double', 'value')])
mod.add_function('Slice_float64_append', None, [param('int64_t', 'handle'), param('double', 'value')])
mod.add_function('Slice_int_CTor', retval('int64_t'), [])
mod.add_function('Slice_int_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_int_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_int16_CTor', retval('int64_t'), [])
mod.add_function('Slice_int16_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int16_elem', retval('int16_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int16_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int16_t', 'value')])
mod.add_function('Slice_int16_append', None, [param('int64_t', 'handle'), param('int16_t', 'value')])
mod.add_function('Slice_int32_CTor', retval('int64_t'), [])
mod.add_function('Slice_int32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int32_elem', retval('int32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int32_t', 'value')])
mod.add_function('Slice_int32_append', None, [param('int64_t', 'handle'), param('int32_t', 'value')])
mod.add_function('Slice_int64_CTor', retval('int64_t'), [])
mod.add_function('Slice_int64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int64_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_int64_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_int8_CTor', retval('int64_t'), [])
mod.add_function('Slice_int8_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int8_elem', retval('int8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int8_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int8_t', 'value')])
mod.add_function('Slice_int8_append', None, [param('int64_t', 'handle'), param('int8_t', 'value')])
mod.add_function('Slice_rune_CTor', retval('int64_t'), [])
mod.add_function('Slice_rune_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_rune_elem', retval('int32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_rune_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int32_t', 'value')])
mod.add_function('Slice_rune_append', None, [param('int64_t', 'handle'), param('int32_t', 'value')])
mod.add_function('Slice_string_CTor', retval('int64_t'), [])
mod.add_function('Slice_string_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_string_elem', retval('char*'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_string_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('char*', 'value')])
mod.add_function('Slice_string_append', None, [param('int64_t', 'handle'), param('char*', 'value')])
mod.add_function('Slice_uint_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint_elem', retval('uint64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint64_t', 'value')])
mod.add_function('Slice_uint_append', None, [param('int64_t', 'handle'), param('uint64_t', 'value')])
mod.add_function('Slice_uint16_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint16_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint16_elem', retval('uint16_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint16_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint16_t', 'value')])
mod.add_function('Slice_uint16_append', None, [param('int64_t', 'handle'), param('uint16_t', 'value')])
mod.add_function('Slice_uint32_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint32_elem', retval('uint32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint32_t', 'value')])
mod.add_function('Slice_uint32_append', None, [param('int64_t', 'handle'), param('uint32_t', 'value')])
mod.add_function('Slice_uint64_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint64_elem', retval('uint64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint64_t', 'value')])
mod.add_function('Slice_uint64_append', None, [param('int64_t', 'handle'), param('uint64_t', 'value')])
mod.add_function('Slice_uint8_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint8_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint8_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint8_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Slice_uint8_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('Slice_Ptr_interpreter_AttributeQualifierPattern_CTor', retval('int64_t'), [])
mod.add_function('Slice_Ptr_interpreter_AttributeQualifierPattern_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_Ptr_interpreter_AttributeQualifierPattern_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_Ptr_interpreter_AttributeQualifierPattern_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_Ptr_interpreter_AttributeQualifierPattern_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_Ptr_expr_Expr_CTor', retval('int64_t'), [])
mod.add_function('Slice_Ptr_expr_Expr_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_Ptr_expr_Expr_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_Ptr_expr_Expr_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_Ptr_expr_Expr_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_Ptr_expr_Expr_CreateStruct_Entry_CTor', retval('int64_t'), [])
mod.add_function('Slice_Ptr_expr_Expr_CreateStruct_Entry_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_Ptr_expr_Expr_CreateStruct_Entry_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_Ptr_expr_Expr_CreateStruct_Entry_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_Ptr_expr_Expr_CreateStruct_Entry_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_Ptr_expr_Type_CTor', retval('int64_t'), [])
mod.add_function('Slice_Ptr_expr_Type_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_Ptr_expr_Type_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_Ptr_expr_Type_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_Ptr_expr_Type_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_common_Error_CTor', retval('int64_t'), [])
mod.add_function('Slice_common_Error_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_common_Error_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_common_Error_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_common_Error_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Map_int64_Ptr_expr_Expr_CTor', retval('int64_t'), [])
mod.add_function('Map_int64_Ptr_expr_Expr_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Map_int64_Ptr_expr_Expr_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int64_t', '_ky')])
mod.add_function('Map_int64_Ptr_expr_Expr_contains', retval('bool'), [param('int64_t', 'handle'), param('int64_t', '_ky')])
mod.add_function('Map_int64_Ptr_expr_Expr_set', None, [param('int64_t', 'handle'), param('int64_t', 'key'), param('int64_t', 'value')])
mod.add_function('Map_int64_Ptr_expr_Expr_delete', None, [param('int64_t', 'handle'), param('int64_t', '_ky')])
mod.add_function('Map_int64_Ptr_expr_Expr_keys', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('Map_int64_Ptr_expr_Reference_CTor', retval('int64_t'), [])
mod.add_function('Map_int64_Ptr_expr_Reference_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Map_int64_Ptr_expr_Reference_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int64_t', '_ky')])
mod.add_function('Map_int64_Ptr_expr_Reference_contains', retval('bool'), [param('int64_t', 'handle'), param('int64_t', '_ky')])
mod.add_function('Map_int64_Ptr_expr_Reference_set', None, [param('int64_t', 'handle'), param('int64_t', 'key'), param('int64_t', 'value')])
mod.add_function('Map_int64_Ptr_expr_Reference_delete', None, [param('int64_t', 'handle'), param('int64_t', '_ky')])
mod.add_function('Map_int64_Ptr_expr_Reference_keys', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('Map_int64_Ptr_expr_Type_CTor', retval('int64_t'), [])
mod.add_function('Map_int64_Ptr_expr_Type_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Map_int64_Ptr_expr_Type_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int64_t', '_ky')])
mod.add_function('Map_int64_Ptr_expr_Type_contains', retval('bool'), [param('int64_t', 'handle'), param('int64_t', '_ky')])
mod.add_function('Map_int64_Ptr_expr_Type_set', None, [param('int64_t', 'handle'), param('int64_t', 'key'), param('int64_t', 'value')])
mod.add_function('Map_int64_Ptr_expr_Type_delete', None, [param('int64_t', 'handle'), param('int64_t', '_ky')])
mod.add_function('Map_int64_Ptr_expr_Type_keys', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('Map_int64_int32_CTor', retval('int64_t'), [])
mod.add_function('Map_int64_int32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Map_int64_int32_elem', retval('int32_t'), [param('int64_t', 'handle'), param('int64_t', '_ky')])
mod.add_function('Map_int64_int32_contains', retval('bool'), [param('int64_t', 'handle'), param('int64_t', '_ky')])
mod.add_function('Map_int64_int32_set', None, [param('int64_t', 'handle'), param('int64_t', 'key'), param('int32_t', 'value')])
mod.add_function('Map_int64_int32_delete', None, [param('int64_t', 'handle'), param('int64_t', '_ky')])
mod.add_function('Map_int64_int32_keys', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('cel_Source_Content', retval('char*'), [param('int64_t', '_handle')])
mod.add_function('cel_Source_Description', retval('char*'), [param('int64_t', '_handle')])
mod.add_function('cel_Source_LineOffsets', retval('int64_t'), [param('int64_t', '_handle')])
mod.add_function('cel_Source_NewLocation', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'line'), param('int64_t', 'col')])
mod.add_function('cel_EvalDetails_CTor', retval('int64_t'), [])
mod.add_function('cel_EvalDetails_State', retval('int64_t'), [param('int64_t', '_handle')])
mod.add_function('cel_Issues_CTor', retval('int64_t'), [])
mod.add_function('cel_Issues_Err', retval('char*'), [param('int64_t', '_handle')])
mod.add_function('cel_Issues_Errors', retval('int64_t'), [param('int64_t', '_handle')])
mod.add_function('cel_Issues_Append', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'other')])
mod.add_function('cel_Issues_String', retval('char*'), [param('int64_t', '_handle')])
mod.add_function('cel_Ast_CTor', retval('int64_t'), [])
mod.add_function('cel_Ast_Expr', retval('int64_t'), [param('int64_t', '_handle')])
mod.add_function('cel_Ast_IsChecked', retval('bool'), [param('int64_t', '_handle')])
mod.add_function('cel_Ast_SourceInfo', retval('int64_t'), [param('int64_t', '_handle')])
mod.add_function('cel_Ast_ResultType', retval('int64_t'), [param('int64_t', '_handle')])
mod.add_function('cel_Ast_Source', retval('int64_t'), [param('int64_t', '_handle')])
mod.add_function('cel_Env_CTor', retval('int64_t'), [])
mod.add_function('cel_Env_HasFeature', retval('bool'), [param('int64_t', '_handle'), param('int64_t', 'flag')])
mod.add_function('cel_Env_SetFeature', None, [param('int64_t', '_handle'), param('int64_t', 'flag'), param('bool', 'goRun')])
mod.add_function('cel_Env_TypeAdapter', retval('int64_t'), [param('int64_t', '_handle')])
mod.add_function('cel_Env_TypeProvider', retval('int64_t'), [param('int64_t', '_handle')])
mod.add_function('cel_Env_UnknownVars', retval('int64_t'), [param('int64_t', '_handle')])
mod.add_function('cel_Env_ResidualAst', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'a'), param('int64_t', 'details')])
mod.add_function('cel_NewIssues', retval('int64_t'), [param('int64_t', 'errs')])
mod.add_function('cel_ParsedExprToAst', retval('int64_t'), [param('int64_t', 'parsedExpr')])
mod.add_function('cel_CheckedExprToAst', retval('int64_t'), [param('int64_t', 'checkedExpr')])
mod.add_function('cel_AstToString', retval('char*'), [param('int64_t', 'a')])
mod.add_function('cel_AttributePattern', retval('int64_t'), [param('char*', 'varName')])
mod.add_function('cel_NoVars', retval('int64_t'), [])
mod.add_function('cel_AstToCheckedExpr', retval('int64_t'), [param('int64_t', 'a')])
mod.add_function('cel_AstToParsedExpr', retval('int64_t'), [param('int64_t', 'a')])

mod.generate(open('cel.c', 'w'))
