"""
Package parser declares an expression parser with support for macro
expansion.

"""
# python wrapper for package github.com/google/cel-go/parser within overall package parser
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy build -output=parser github.com/google/cel-go/parser

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
import _parser
os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from parser import parser
# and then refer to everything using parser. prefix
# packages imported by this package listed below:

import go



# ---- Types ---

# Python type for slice []*expr.Expr
class Slice_Ptr_expr_Expr(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_parser.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_parser.IncRef(self.handle)
		else:
			self.handle = _parser.Slice_Ptr_expr_Expr_CTor()
			_parser.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_Ptr_expr_Expr.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_parser.DecRef(self.handle)
	def __str__(self):
		s = 'parser.Slice_Ptr_expr_Expr len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'parser.Slice_Ptr_expr_Expr([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _parser.Slice_Ptr_expr_Expr_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.Ptr_expr_Expr(handle=_parser.Slice_Ptr_expr_Expr_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_parser.Slice_Ptr_expr_Expr_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, collections.Iterable):
			raise TypeError('Slice_Ptr_expr_Expr.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = _parser.Slice_Ptr_expr_Expr_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_parser.Slice_Ptr_expr_Expr_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]

# Python type for slice []*expr.Expr_CreateStruct_Entry
class Slice_Ptr_expr_Expr_CreateStruct_Entry(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_parser.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_parser.IncRef(self.handle)
		else:
			self.handle = _parser.Slice_Ptr_expr_Expr_CreateStruct_Entry_CTor()
			_parser.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_Ptr_expr_Expr_CreateStruct_Entry.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_parser.DecRef(self.handle)
	def __str__(self):
		s = 'parser.Slice_Ptr_expr_Expr_CreateStruct_Entry len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'parser.Slice_Ptr_expr_Expr_CreateStruct_Entry([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _parser.Slice_Ptr_expr_Expr_CreateStruct_Entry_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.Ptr_expr_Expr_CreateStruct_Entry(handle=_parser.Slice_Ptr_expr_Expr_CreateStruct_Entry_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_parser.Slice_Ptr_expr_Expr_CreateStruct_Entry_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, collections.Iterable):
			raise TypeError('Slice_Ptr_expr_Expr_CreateStruct_Entry.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = _parser.Slice_Ptr_expr_Expr_CreateStruct_Entry_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_parser.Slice_Ptr_expr_Expr_CreateStruct_Entry_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]

# Python type for slice []parser.Macro
class Slice_parser_Macro(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_parser.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_parser.IncRef(self.handle)
		else:
			self.handle = _parser.Slice_parser_Macro_CTor()
			_parser.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_parser_Macro.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_parser.DecRef(self.handle)
	def __str__(self):
		s = 'parser.Slice_parser_Macro len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'parser.Slice_parser_Macro([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _parser.Slice_parser_Macro_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return Macro(handle=_parser.Slice_parser_Macro_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_parser.Slice_parser_Macro_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, collections.Iterable):
			raise TypeError('Slice_parser_Macro.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = _parser.Slice_parser_Macro_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_parser.Slice_parser_Macro_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]

# Python type for map map[int64]*expr.Expr
class Map_int64_Ptr_expr_Expr(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_parser.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_parser.IncRef(self.handle)
		else:
			self.handle = _parser.Map_int64_Ptr_expr_Expr_CTor()
			_parser.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Mapping):
					raise TypeError('Map_int64_Ptr_expr_Expr.__init__ takes a mapping as argument')
				for k, v in args[0].items():
					_parser.Map_int64_Ptr_expr_Expr_set(self.handle, k, v)
	def __del__(self):
		_parser.DecRef(self.handle)
	def __str__(self):
		s = 'parser.Map_int64_Ptr_expr_Expr len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' {'
		if len(self) < 120:
			for k, v in self.items():
				s += str(k) + '=' + str(v) + ', '
		return s + '}'
	def __repr__(self):
		s = 'parser.Map_int64_Ptr_expr_Expr({'
		for k, v in self.items():
			s += str(k) + '=' + str(v) + ', '
		return s + '})'
	def __len__(self):
		return _parser.Map_int64_Ptr_expr_Expr_len(self.handle)
	def __getitem__(self, key):
		return go.Ptr_expr_Expr(handle=_parser.Map_int64_Ptr_expr_Expr_elem(self.handle, key))
	def __setitem__(self, key, value):
		_parser.Map_int64_Ptr_expr_Expr_set(self.handle, key, value.handle)
	def __delitem__(self, key):
		return _parser.Map_int64_Ptr_expr_Expr_delete(self.handle, key)
	def keys(self):
		return go.Slice_int64(handle=_parser.Map_int64_Ptr_expr_Expr_keys(self.handle))
	def values(self):
		vls = []
		kys = self.keys()
		for k in kys:
			vls.append(self[k])
		return vls
	def items(self):
		vls = []
		kys = self.keys()
		for k in kys:
			vls.append((k, self[k]))
		return vls
	def __iter__(self):
		return iter(self.items())
	def __contains__(self, key):
		return _parser.Map_int64_Ptr_expr_Expr_contains(self.handle, key)

# Python type for map map[int64]int32
class Map_int64_int32(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_parser.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_parser.IncRef(self.handle)
		else:
			self.handle = _parser.Map_int64_int32_CTor()
			_parser.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Mapping):
					raise TypeError('Map_int64_int32.__init__ takes a mapping as argument')
				for k, v in args[0].items():
					_parser.Map_int64_int32_set(self.handle, k, v)
	def __del__(self):
		_parser.DecRef(self.handle)
	def __str__(self):
		s = 'parser.Map_int64_int32 len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' {'
		if len(self) < 120:
			for k, v in self.items():
				s += str(k) + '=' + str(v) + ', '
		return s + '}'
	def __repr__(self):
		s = 'parser.Map_int64_int32({'
		for k, v in self.items():
			s += str(k) + '=' + str(v) + ', '
		return s + '})'
	def __len__(self):
		return _parser.Map_int64_int32_len(self.handle)
	def __getitem__(self, key):
		return _parser.Map_int64_int32_elem(self.handle, key)
	def __setitem__(self, key, value):
		_parser.Map_int64_int32_set(self.handle, key, value)
	def __delitem__(self, key):
		return _parser.Map_int64_int32_delete(self.handle, key)
	def keys(self):
		return go.Slice_int64(handle=_parser.Map_int64_int32_keys(self.handle))
	def values(self):
		vls = []
		kys = self.keys()
		for k in kys:
			vls.append(self[k])
		return vls
	def items(self):
		vls = []
		kys = self.keys()
		for k in kys:
			vls.append((k, self[k]))
		return vls
	def __iter__(self):
		return iter(self.items())
	def __contains__(self, key):
		return _parser.Map_int64_int32_contains(self.handle, key)


#---- Constants from Go: Python can only ask that you please don't change these! ---
AccumulatorName = "__result__"


# ---- Global Variables: can only use functions to access ---
def AllMacros():
	"""
	AllMacros Gets Go Variable: parser.AllMacros
	
	"""
	return Slice_parser_Macro(handle=_parser.parser_AllMacros())

def Set_AllMacros(value):
	"""
	Set_AllMacros Sets Go Variable: parser.AllMacros
	
	"""
	if isinstance(value, go.GoClass):
		_parser.parser_Set_AllMacros(value.handle)
	else:
		_parser.parser_Set_AllMacros(value)

def NoMacros():
	"""
	NoMacros Gets Go Variable: parser.NoMacros
	
	"""
	return Slice_parser_Macro(handle=_parser.parser_NoMacros())

def Set_NoMacros(value):
	"""
	Set_NoMacros Sets Go Variable: parser.NoMacros
	
	"""
	if isinstance(value, go.GoClass):
		_parser.parser_Set_NoMacros(value.handle)
	else:
		_parser.parser_Set_NoMacros(value)



# ---- Interfaces ---

# Python type for interface parser.ExprHelper
class ExprHelper(go.GoClass):
	"""ExprHelper assists with the manipulation of proto-based Expr values in a manner which is\nconsistent with the source position and expression id generation code leveraged by both\nthe parser and type-checker.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_parser.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_parser.IncRef(self.handle)
		else:
			self.handle = 0
	def Fold(self, iterVar, iterRange, accuVar, accuInit, condition, step, result):
		"""Fold(str iterVar, object iterRange, str accuVar, object accuInit, object condition, object step, object result) object"""
		return go.Ptr_expr_Expr(handle=_parser.parser_ExprHelper_Fold(self.handle, iterVar, iterRange.handle, accuVar, accuInit.handle, condition.handle, step.handle, result.handle))
	def Ident(self, name):
		"""Ident(str name) object"""
		return go.Ptr_expr_Expr(handle=_parser.parser_ExprHelper_Ident(self.handle, name))
	def LiteralBool(self, value):
		"""LiteralBool(bool value) object"""
		return go.Ptr_expr_Expr(handle=_parser.parser_ExprHelper_LiteralBool(self.handle, value))
	def LiteralBytes(self, value):
		"""LiteralBytes([]int value) object"""
		return go.Ptr_expr_Expr(handle=_parser.parser_ExprHelper_LiteralBytes(self.handle, value.handle))
	def LiteralDouble(self, value):
		"""LiteralDouble(float value) object"""
		return go.Ptr_expr_Expr(handle=_parser.parser_ExprHelper_LiteralDouble(self.handle, value))
	def LiteralInt(self, value):
		"""LiteralInt(long value) object"""
		return go.Ptr_expr_Expr(handle=_parser.parser_ExprHelper_LiteralInt(self.handle, value))
	def LiteralString(self, value):
		"""LiteralString(str value) object"""
		return go.Ptr_expr_Expr(handle=_parser.parser_ExprHelper_LiteralString(self.handle, value))
	def LiteralUint(self, value):
		"""LiteralUint(long value) object"""
		return go.Ptr_expr_Expr(handle=_parser.parser_ExprHelper_LiteralUint(self.handle, value))
	def NewMapEntry(self, key, val):
		"""NewMapEntry(object key, object val) object"""
		return go.Ptr_expr_Expr_CreateStruct_Entry(handle=_parser.parser_ExprHelper_NewMapEntry(self.handle, key.handle, val.handle))
	def NewObjectFieldInit(self, field, init):
		"""NewObjectFieldInit(str field, object init) object"""
		return go.Ptr_expr_Expr_CreateStruct_Entry(handle=_parser.parser_ExprHelper_NewObjectFieldInit(self.handle, field, init.handle))
	def OffsetLocation(self, exprID):
		"""OffsetLocation(long exprID) object"""
		return go.common_Location(handle=_parser.parser_ExprHelper_OffsetLocation(self.handle, exprID))
	def PresenceTest(self, operand, field):
		"""PresenceTest(object operand, str field) object"""
		return go.Ptr_expr_Expr(handle=_parser.parser_ExprHelper_PresenceTest(self.handle, operand.handle, field))
	def Select(self, operand, field):
		"""Select(object operand, str field) object"""
		return go.Ptr_expr_Expr(handle=_parser.parser_ExprHelper_Select(self.handle, operand.handle, field))

# Python type for interface parser.Macro
class Macro(go.GoClass):
	"""Macro interface for describing the function signature to match and the MacroExpander to apply.\n\nNote: when a Macro should apply to multiple overloads (based on arg count) of a given function,\na Macro should be created per arg-count.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_parser.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_parser.IncRef(self.handle)
		else:
			self.handle = 0
	def ArgCount(self):
		"""ArgCount() int"""
		return _parser.parser_Macro_ArgCount(self.handle)
	def Function(self):
		"""Function() str"""
		return _parser.parser_Macro_Function(self.handle)
	def IsReceiverStyle(self):
		"""IsReceiverStyle() bool"""
		return _parser.parser_Macro_IsReceiverStyle(self.handle)
	def MacroKey(self):
		"""MacroKey() str"""
		return _parser.parser_Macro_MacroKey(self.handle)


# ---- Structs ---


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---


# ---- Functions ---
def Unparse(expr, info):
	"""Unparse(object expr, object info) str, str
	
	Unparse takes an input expression and source position information and generates a human-readable
	expression.
	
	Note, unparsing an AST will often generate the same expression as was originally parsed, but some
	formatting may be lost in translation, notably:
	
	- All quoted literals are doubled quoted.
	- Byte literals are represented as octal escapes (same as Google SQL).
	- Floating point values are converted to the small number of digits needed to represent the value.
	- Spacing around punctuation marks may be lost.
	- Parentheses will only be applied when they affect operator precedence.
	"""
	return _parser.parser_Unparse(expr.handle, info.handle)


