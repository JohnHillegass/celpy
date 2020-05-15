"""
Package interpreter provides functions to evaluate parsed expressions with
the option to augment the evaluation with inputs and functions supplied at
evaluation time.

"""
# python wrapper for package github.com/google/cel-go/interpreter within overall package interpreter
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy build -output=interpreter github.com/google/cel-go/interpreter

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
import _interpreter
os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from interpreter import interpreter
# and then refer to everything using interpreter. prefix
# packages imported by this package listed below:

import go



# ---- Types ---

# Python type for slice []*interpreter.AttributePattern
class Slice_Ptr_interpreter_AttributePattern(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = _interpreter.Slice_Ptr_interpreter_AttributePattern_CTor()
			_interpreter.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_Ptr_interpreter_AttributePattern.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_interpreter.DecRef(self.handle)
	def __str__(self):
		s = 'interpreter.Slice_Ptr_interpreter_AttributePattern len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'interpreter.Slice_Ptr_interpreter_AttributePattern([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _interpreter.Slice_Ptr_interpreter_AttributePattern_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return AttributePattern(handle=_interpreter.Slice_Ptr_interpreter_AttributePattern_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_interpreter.Slice_Ptr_interpreter_AttributePattern_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, collections.Iterable):
			raise TypeError('Slice_Ptr_interpreter_AttributePattern.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = _interpreter.Slice_Ptr_interpreter_AttributePattern_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_interpreter.Slice_Ptr_interpreter_AttributePattern_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]

# Python type for slice []*interpreter.AttributeQualifierPattern
class Slice_Ptr_interpreter_AttributeQualifierPattern(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = _interpreter.Slice_Ptr_interpreter_AttributeQualifierPattern_CTor()
			_interpreter.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_Ptr_interpreter_AttributeQualifierPattern.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_interpreter.DecRef(self.handle)
	def __str__(self):
		s = 'interpreter.Slice_Ptr_interpreter_AttributeQualifierPattern len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'interpreter.Slice_Ptr_interpreter_AttributeQualifierPattern([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _interpreter.Slice_Ptr_interpreter_AttributeQualifierPattern_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return AttributeQualifierPattern(handle=_interpreter.Slice_Ptr_interpreter_AttributeQualifierPattern_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_interpreter.Slice_Ptr_interpreter_AttributeQualifierPattern_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, collections.Iterable):
			raise TypeError('Slice_Ptr_interpreter_AttributeQualifierPattern.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = _interpreter.Slice_Ptr_interpreter_AttributeQualifierPattern_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_interpreter.Slice_Ptr_interpreter_AttributeQualifierPattern_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]

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
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = _interpreter.Slice_Ptr_expr_Expr_CTor()
			_interpreter.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_Ptr_expr_Expr.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_interpreter.DecRef(self.handle)
	def __str__(self):
		s = 'interpreter.Slice_Ptr_expr_Expr len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'interpreter.Slice_Ptr_expr_Expr([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _interpreter.Slice_Ptr_expr_Expr_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.Ptr_expr_Expr(handle=_interpreter.Slice_Ptr_expr_Expr_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_interpreter.Slice_Ptr_expr_Expr_set(self.handle, idx, value.handle)
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
			rv = _interpreter.Slice_Ptr_expr_Expr_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_interpreter.Slice_Ptr_expr_Expr_append(self.handle, value.handle)
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
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = _interpreter.Slice_Ptr_expr_Expr_CreateStruct_Entry_CTor()
			_interpreter.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_Ptr_expr_Expr_CreateStruct_Entry.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_interpreter.DecRef(self.handle)
	def __str__(self):
		s = 'interpreter.Slice_Ptr_expr_Expr_CreateStruct_Entry len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'interpreter.Slice_Ptr_expr_Expr_CreateStruct_Entry([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _interpreter.Slice_Ptr_expr_Expr_CreateStruct_Entry_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.Ptr_expr_Expr_CreateStruct_Entry(handle=_interpreter.Slice_Ptr_expr_Expr_CreateStruct_Entry_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_interpreter.Slice_Ptr_expr_Expr_CreateStruct_Entry_set(self.handle, idx, value.handle)
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
			rv = _interpreter.Slice_Ptr_expr_Expr_CreateStruct_Entry_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_interpreter.Slice_Ptr_expr_Expr_CreateStruct_Entry_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]

# Python type for slice []*expr.Type
class Slice_Ptr_expr_Type(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = _interpreter.Slice_Ptr_expr_Type_CTor()
			_interpreter.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_Ptr_expr_Type.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_interpreter.DecRef(self.handle)
	def __str__(self):
		s = 'interpreter.Slice_Ptr_expr_Type len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'interpreter.Slice_Ptr_expr_Type([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _interpreter.Slice_Ptr_expr_Type_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.Ptr_expr_Type(handle=_interpreter.Slice_Ptr_expr_Type_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_interpreter.Slice_Ptr_expr_Type_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, collections.Iterable):
			raise TypeError('Slice_Ptr_expr_Type.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = _interpreter.Slice_Ptr_expr_Type_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_interpreter.Slice_Ptr_expr_Type_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---

# Python type for interface interpreter.Dispatcher
class Dispatcher(go.GoClass):
	"""Dispatcher resolves function calls to their appropriate overload.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = 0
	def OverloadIds(self):
		"""OverloadIds() []str"""
		return go.Slice_string(handle=_interpreter.interpreter_Dispatcher_OverloadIds(self.handle))

# Python type for interface interpreter.EvalState
class EvalState(go.GoClass):
	"""EvalState tracks the values associated with expression ids during execution.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = 0
	def IDs(self):
		"""IDs() []long"""
		return go.Slice_int64(handle=_interpreter.interpreter_EvalState_IDs(self.handle))
	def Reset(self, goRun=False):
		"""Reset() """
		_interpreter.interpreter_EvalState_Reset(self.handle, goRun)
	def SetValue(self, arg_0, arg_1, goRun=False):
		"""SetValue(long, object) """
		_interpreter.interpreter_EvalState_SetValue(self.handle, arg_0, arg_1.handle, goRun)

# Python type for interface interpreter.Interpretable
class Interpretable(go.GoClass):
	"""Interpretable can accept a given Activation and produce a value along with\nan accompanying EvalState which can be used to inspect whether additional\ndata might be necessary to complete the evaluation.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = 0
	def Eval(self, activation):
		"""Eval(object activation) object"""
		return go.ref_Val(handle=_interpreter.interpreter_Interpretable_Eval(self.handle, activation.handle))
	def ID(self):
		"""ID() long"""
		return _interpreter.interpreter_Interpretable_ID(self.handle)

# Python type for interface interpreter.NamespacedAttribute
class NamespacedAttribute(go.GoClass):
	"""NamespacedAttribute values are a variable within a namespace, and an optional set of qualifiers\nsuch as field, key, or index accesses.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = 0
	def AddQualifier(self, arg_0):
		"""AddQualifier(object) object, str"""
		return Attribute(handle=_interpreter.interpreter_NamespacedAttribute_AddQualifier(self.handle, arg_0.handle))
	def CandidateVariableNames(self):
		"""CandidateVariableNames() []str"""
		return go.Slice_string(handle=_interpreter.interpreter_NamespacedAttribute_CandidateVariableNames(self.handle))
	def HasQualifiers(self):
		"""HasQualifiers() bool"""
		return _interpreter.interpreter_NamespacedAttribute_HasQualifiers(self.handle)
	def ID(self):
		"""ID() long"""
		return _interpreter.interpreter_NamespacedAttribute_ID(self.handle)

# Python type for interface interpreter.PartialActivation
class PartialActivation(go.GoClass):
	"""PartialActivation extends the Activation interface with a set of UnknownAttributePatterns.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = 0
	def Parent(self):
		"""Parent() object"""
		return Activation(handle=_interpreter.interpreter_PartialActivation_Parent(self.handle))
	def UnknownAttributePatterns(self):
		"""UnknownAttributePatterns() []object"""
		return Slice_Ptr_interpreter_AttributePattern(handle=_interpreter.interpreter_PartialActivation_UnknownAttributePatterns(self.handle))

# Python type for interface interpreter.Qualifier
class Qualifier(go.GoClass):
	"""Qualifier marker interface for designating different qualifier values and where they appear\nwithin field selections and index call expressions (`_[_]`).\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = 0
	def ID(self):
		"""ID() long"""
		return _interpreter.interpreter_Qualifier_ID(self.handle)

# Python type for interface interpreter.AttributeFactory
class AttributeFactory(go.GoClass):
	"""AttributeFactory provides methods creating Attribute and Qualifier values.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = 0
	def ConditionalAttribute(self, id, expr, t, f):
		"""ConditionalAttribute(long id, object expr, object t, object f) object"""
		return Attribute(handle=_interpreter.interpreter_AttributeFactory_ConditionalAttribute(self.handle, id, expr.handle, t.handle, f.handle))
	def MaybeAttribute(self, id, name):
		"""MaybeAttribute(long id, str name) object"""
		return Attribute(handle=_interpreter.interpreter_AttributeFactory_MaybeAttribute(self.handle, id, name))
	def NewQualifier(self, objType, qualID, val):
		"""NewQualifier(object objType, long qualID, str val) object, str"""
		return Qualifier(handle=_interpreter.interpreter_AttributeFactory_NewQualifier(self.handle, objType.handle, qualID, val))
	def RelativeAttribute(self, id, operand):
		"""RelativeAttribute(long id, object operand) object"""
		return Attribute(handle=_interpreter.interpreter_AttributeFactory_RelativeAttribute(self.handle, id, operand.handle))

# Python type for interface interpreter.Attribute
class Attribute(go.GoClass):
	"""Attribute values are a variable or value with an optional set of qualifiers, such as field, key,\nor index accesses.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = 0
	def AddQualifier(self, arg_0):
		"""AddQualifier(object) object, str"""
		return Attribute(handle=_interpreter.interpreter_Attribute_AddQualifier(self.handle, arg_0.handle))
	def ID(self):
		"""ID() long"""
		return _interpreter.interpreter_Attribute_ID(self.handle)

# Python type for interface interpreter.Interpreter
class Interpreter(go.GoClass):
	"""Interpreter generates a new Interpretable from a checked or unchecked expression.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = 0

# Python type for interface interpreter.Activation
class Activation(go.GoClass):
	"""Activation used to resolve identifiers by name and references by id.\n\nAn Activation is the primary mechanism by which a caller supplies input into a CEL program.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = 0
	def Parent(self):
		"""Parent() object"""
		return Activation(handle=_interpreter.interpreter_Activation_Parent(self.handle))


# ---- Structs ---

# Python type for struct interpreter.AttributePattern
class AttributePattern(go.GoClass):
	"""AttributePattern represents a top-level variable with an optional set of qualifier patterns.\n\nWhen using a CEL expression within a container, e.g. a package or namespace, the variable name\nin the pattern must match the qualified name produced during the variable namespace resolution.\nFor example, if variable `c` appears in an expression whose container is `a.b`, the variable\nname supplied to the pattern must be `a.b.c`\n\nThe qualifier patterns for attribute matching must be one of the following:\n\n  - valid map key type: string, int, uint, bool\n  - wildcard (*)\n\nExamples:\n\n  1. ns.myvar[\"complex-value\"]\n  2. ns.myvar[\"complex-value\"][0]\n  3. ns.myvar[\"complex-value\"].*.name\n\nThe first example is simple: match an attribute where the variable is 'ns.myvar' with a\nfield access on 'complex-value'. The second example expands the match to indicate that only\na specific index `0` should match. And lastly, the third example matches any indexed access\nthat later selects the 'name' field.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = _interpreter.interpreter_AttributePattern_CTor()
			_interpreter.IncRef(self.handle)
	def __del__(self):
		_interpreter.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'interpreter.AttributePattern{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'interpreter.AttributePattern ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def QualString(self, pattern):
		"""QualString(str pattern) object
		
		QualString adds a string qualifier pattern to the AttributePattern. The string may be a valid
		identifier, or string map key including empty string.
		"""
		return AttributePattern(handle=_interpreter.interpreter_AttributePattern_QualString(self.handle, pattern))
	def QualInt(self, pattern):
		"""QualInt(long pattern) object
		
		QualInt adds an int qualifier pattern to the AttributePattern. The index may be either a map or
		list index.
		"""
		return AttributePattern(handle=_interpreter.interpreter_AttributePattern_QualInt(self.handle, pattern))
	def QualUint(self, pattern):
		"""QualUint(long pattern) object
		
		QualUint adds an uint qualifier pattern for a map index operation to the AttributePattern.
		"""
		return AttributePattern(handle=_interpreter.interpreter_AttributePattern_QualUint(self.handle, pattern))
	def QualBool(self, pattern):
		"""QualBool(bool pattern) object
		
		QualBool adds a bool qualifier pattern for a map index operation to the AttributePattern.
		"""
		return AttributePattern(handle=_interpreter.interpreter_AttributePattern_QualBool(self.handle, pattern))
	def Wildcard(self):
		"""Wildcard() object
		
		Wildcard adds a special sentinel qualifier pattern that will match any single qualifier.
		"""
		return AttributePattern(handle=_interpreter.interpreter_AttributePattern_Wildcard(self.handle))
	def VariableMatches(self, variable):
		"""VariableMatches(str variable) bool
		
		VariableMatches returns true if the fully qualified variable matches the AttributePattern
		fully qualified variable name.
		"""
		return _interpreter.interpreter_AttributePattern_VariableMatches(self.handle, variable)
	def QualifierPatterns(self):
		"""QualifierPatterns() []object
		
		QualifierPatterns returns the set of AttributeQualifierPattern values on the AttributePattern.
		"""
		return Slice_Ptr_interpreter_AttributeQualifierPattern(handle=_interpreter.interpreter_AttributePattern_QualifierPatterns(self.handle))

# Python type for struct interpreter.AttributeQualifierPattern
class AttributeQualifierPattern(go.GoClass):
	"""AttributeQualifierPattern holds a wilcard or valued qualifier pattern.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_interpreter.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_interpreter.IncRef(self.handle)
		else:
			self.handle = _interpreter.interpreter_AttributeQualifierPattern_CTor()
			_interpreter.IncRef(self.handle)
	def __del__(self):
		_interpreter.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'interpreter.AttributeQualifierPattern{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'interpreter.AttributeQualifierPattern ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def Matches(self, q):
		"""Matches(object q) bool
		
		Matches returns true if the qualifier pattern is a wildcard, or the Qualifier implements the
		qualifierValueEquator interface and its IsValueEqualTo returns true for the qualifier pattern.
		"""
		return _interpreter.interpreter_AttributeQualifierPattern_Matches(self.handle, q.handle)


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---
def NewAttributePattern(variable):
	"""NewAttributePattern(str variable) object
	
	NewAttributePattern produces a new mutable AttributePattern based on a variable name.
	"""
	return AttributePattern(handle=_interpreter.interpreter_NewAttributePattern(variable))


# ---- Functions ---
def NewDispatcher():
	"""NewDispatcher() object"""
	return Dispatcher(handle=_interpreter.interpreter_NewDispatcher())
def NewInterpreter(dispatcher, packager, provider, adapter, attrFactory):
	"""NewInterpreter(object dispatcher, object packager, object provider, object adapter, object attrFactory) object"""
	return Interpreter(handle=_interpreter.interpreter_NewInterpreter(dispatcher.handle, packager.handle, provider.handle, adapter.handle, attrFactory.handle))
def NewPartialAttributeFactory(pkg, adapter, provider):
	"""NewPartialAttributeFactory(object pkg, object adapter, object provider) object"""
	return AttributeFactory(handle=_interpreter.interpreter_NewPartialAttributeFactory(pkg.handle, adapter.handle, provider.handle))
def PruneAst(expr, state):
	"""PruneAst(object expr, object state) object
	
	PruneAst prunes the given AST based on the given EvalState and generates a new AST.
	Given AST is copied on write and a new AST is returned.
	Couple of typical use cases this interface would be:
	
	A)
	1) Evaluate expr with some unknowns,
	2) If result is unknown:
	  a) PruneAst
	  b) Goto 1
	Functional call results which are known would be effectively cached across
	iterations.
	
	B)
	1) Compile the expression (maybe via a service and maybe after checking a
	   compiled expression does not exists in local cache)
	2) Prepare the environment and the interpreter. Activation might be empty.
	3) Eval the expression. This might return unknown or error or a concrete
	   value.
	4) PruneAst
	4) Maybe cache the expression
	This is effectively constant folding the expression. How the environment is
	prepared in step 2 is flexible. For example, If the caller caches the
	compiled and constant folded expressions, but is not willing to constant
	fold(and thus cache results of) some external calls, then they can prepare
	the overloads accordingly.
	"""
	return go.Ptr_expr_Expr(handle=_interpreter.interpreter_PruneAst(expr.handle, state.handle))
def EmptyActivation():
	"""EmptyActivation() object"""
	return Activation(handle=_interpreter.interpreter_EmptyActivation())
def NewAttributeFactory(pkg, a, p):
	"""NewAttributeFactory(object pkg, object a, object p) object"""
	return AttributeFactory(handle=_interpreter.interpreter_NewAttributeFactory(pkg.handle, a.handle, p.handle))
def NewEvalState():
	"""NewEvalState() object"""
	return EvalState(handle=_interpreter.interpreter_NewEvalState())
def NewHierarchicalActivation(parent, child):
	"""NewHierarchicalActivation(object parent, object child) object"""
	return Activation(handle=_interpreter.interpreter_NewHierarchicalActivation(parent.handle, child.handle))
def NewStandardInterpreter(packager, provider, adapter, resolver):
	"""NewStandardInterpreter(object packager, object provider, object adapter, object resolver) object"""
	return Interpreter(handle=_interpreter.interpreter_NewStandardInterpreter(packager.handle, provider.handle, adapter.handle, resolver.handle))
def ExtendDispatcher(parent):
	"""ExtendDispatcher(object parent) object"""
	return Dispatcher(handle=_interpreter.interpreter_ExtendDispatcher(parent.handle))
def NewActivation(bindings):
	"""NewActivation(str bindings) object, str"""
	return Activation(handle=_interpreter.interpreter_NewActivation(bindings))


