"""
Package cel defines the top-level interface for the Common Expression Language (CEL).

CEL is a non-Turing complete expression language designed to parse, check, and evaluate
expressions against user-defined environments.

"""
# python wrapper for package github.com/google/cel-go/cel within overall package cel
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy pkg github.com/google/cel-go/cel

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
import _cel
os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from cel import cel
# and then refer to everything using cel. prefix
# packages imported by this package listed below:

from cel import go



# ---- Types ---

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
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = _cel.Slice_Ptr_interpreter_AttributeQualifierPattern_CTor()
			_cel.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_Ptr_interpreter_AttributeQualifierPattern.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_cel.DecRef(self.handle)
	def __str__(self):
		s = 'cel.Slice_Ptr_interpreter_AttributeQualifierPattern len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'cel.Slice_Ptr_interpreter_AttributeQualifierPattern([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _cel.Slice_Ptr_interpreter_AttributeQualifierPattern_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.Ptr_interpreter_AttributeQualifierPattern(handle=_cel.Slice_Ptr_interpreter_AttributeQualifierPattern_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_cel.Slice_Ptr_interpreter_AttributeQualifierPattern_set(self.handle, idx, value.handle)
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
	def next(self):
		if self.index < len(self):
			rv = _cel.Slice_Ptr_interpreter_AttributeQualifierPattern_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_cel.Slice_Ptr_interpreter_AttributeQualifierPattern_append(self.handle, value.handle)
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
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = _cel.Slice_Ptr_expr_Expr_CTor()
			_cel.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_Ptr_expr_Expr.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_cel.DecRef(self.handle)
	def __str__(self):
		s = 'cel.Slice_Ptr_expr_Expr len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'cel.Slice_Ptr_expr_Expr([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _cel.Slice_Ptr_expr_Expr_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.Ptr_expr_Expr(handle=_cel.Slice_Ptr_expr_Expr_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_cel.Slice_Ptr_expr_Expr_set(self.handle, idx, value.handle)
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
	def next(self):
		if self.index < len(self):
			rv = _cel.Slice_Ptr_expr_Expr_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_cel.Slice_Ptr_expr_Expr_append(self.handle, value.handle)
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
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = _cel.Slice_Ptr_expr_Expr_CreateStruct_Entry_CTor()
			_cel.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_Ptr_expr_Expr_CreateStruct_Entry.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_cel.DecRef(self.handle)
	def __str__(self):
		s = 'cel.Slice_Ptr_expr_Expr_CreateStruct_Entry len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'cel.Slice_Ptr_expr_Expr_CreateStruct_Entry([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _cel.Slice_Ptr_expr_Expr_CreateStruct_Entry_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.Ptr_expr_Expr_CreateStruct_Entry(handle=_cel.Slice_Ptr_expr_Expr_CreateStruct_Entry_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_cel.Slice_Ptr_expr_Expr_CreateStruct_Entry_set(self.handle, idx, value.handle)
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
	def next(self):
		if self.index < len(self):
			rv = _cel.Slice_Ptr_expr_Expr_CreateStruct_Entry_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_cel.Slice_Ptr_expr_Expr_CreateStruct_Entry_append(self.handle, value.handle)
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
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = _cel.Slice_Ptr_expr_Type_CTor()
			_cel.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_Ptr_expr_Type.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_cel.DecRef(self.handle)
	def __str__(self):
		s = 'cel.Slice_Ptr_expr_Type len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'cel.Slice_Ptr_expr_Type([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _cel.Slice_Ptr_expr_Type_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.Ptr_expr_Type(handle=_cel.Slice_Ptr_expr_Type_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_cel.Slice_Ptr_expr_Type_set(self.handle, idx, value.handle)
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
	def next(self):
		if self.index < len(self):
			rv = _cel.Slice_Ptr_expr_Type_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_cel.Slice_Ptr_expr_Type_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]

# Python type for slice []common.Error
class Slice_common_Error(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = _cel.Slice_common_Error_CTor()
			_cel.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_common_Error.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_cel.DecRef(self.handle)
	def __str__(self):
		s = 'cel.Slice_common_Error len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'cel.Slice_common_Error([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _cel.Slice_common_Error_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.common_Error(handle=_cel.Slice_common_Error_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_cel.Slice_common_Error_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, collections.Iterable):
			raise TypeError('Slice_common_Error.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def next(self):
		if self.index < len(self):
			rv = _cel.Slice_common_Error_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_cel.Slice_common_Error_append(self.handle, value.handle)
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
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = _cel.Map_int64_Ptr_expr_Expr_CTor()
			_cel.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Mapping):
					raise TypeError('Map_int64_Ptr_expr_Expr.__init__ takes a mapping as argument')
				for k, v in args[0].items():
					_cel.Map_int64_Ptr_expr_Expr_set(self.handle, k, v)
	def __del__(self):
		_cel.DecRef(self.handle)
	def __str__(self):
		s = 'cel.Map_int64_Ptr_expr_Expr len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' {'
		if len(self) < 120:
			for k, v in self.items():
				s += str(k) + '=' + str(v) + ', '
		return s + '}'
	def __repr__(self):
		s = 'cel.Map_int64_Ptr_expr_Expr({'
		for k, v in self.items():
			s += str(k) + '=' + str(v) + ', '
		return s + '})'
	def __len__(self):
		return _cel.Map_int64_Ptr_expr_Expr_len(self.handle)
	def __getitem__(self, key):
		return go.Ptr_expr_Expr(handle=_cel.Map_int64_Ptr_expr_Expr_elem(self.handle, key))
	def __setitem__(self, key, value):
		_cel.Map_int64_Ptr_expr_Expr_set(self.handle, key, value.handle)
	def __delitem__(self, key):
		return _cel.Map_int64_Ptr_expr_Expr_delete(self.handle, key)
	def keys(self):
		return go.Slice_int64(handle=_cel.Map_int64_Ptr_expr_Expr_keys(self.handle))
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
		return _cel.Map_int64_Ptr_expr_Expr_contains(self.handle, key)

# Python type for map map[int64]*expr.Reference
class Map_int64_Ptr_expr_Reference(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = _cel.Map_int64_Ptr_expr_Reference_CTor()
			_cel.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Mapping):
					raise TypeError('Map_int64_Ptr_expr_Reference.__init__ takes a mapping as argument')
				for k, v in args[0].items():
					_cel.Map_int64_Ptr_expr_Reference_set(self.handle, k, v)
	def __del__(self):
		_cel.DecRef(self.handle)
	def __str__(self):
		s = 'cel.Map_int64_Ptr_expr_Reference len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' {'
		if len(self) < 120:
			for k, v in self.items():
				s += str(k) + '=' + str(v) + ', '
		return s + '}'
	def __repr__(self):
		s = 'cel.Map_int64_Ptr_expr_Reference({'
		for k, v in self.items():
			s += str(k) + '=' + str(v) + ', '
		return s + '})'
	def __len__(self):
		return _cel.Map_int64_Ptr_expr_Reference_len(self.handle)
	def __getitem__(self, key):
		return go.Ptr_expr_Reference(handle=_cel.Map_int64_Ptr_expr_Reference_elem(self.handle, key))
	def __setitem__(self, key, value):
		_cel.Map_int64_Ptr_expr_Reference_set(self.handle, key, value.handle)
	def __delitem__(self, key):
		return _cel.Map_int64_Ptr_expr_Reference_delete(self.handle, key)
	def keys(self):
		return go.Slice_int64(handle=_cel.Map_int64_Ptr_expr_Reference_keys(self.handle))
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
		return _cel.Map_int64_Ptr_expr_Reference_contains(self.handle, key)

# Python type for map map[int64]*expr.Type
class Map_int64_Ptr_expr_Type(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = _cel.Map_int64_Ptr_expr_Type_CTor()
			_cel.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Mapping):
					raise TypeError('Map_int64_Ptr_expr_Type.__init__ takes a mapping as argument')
				for k, v in args[0].items():
					_cel.Map_int64_Ptr_expr_Type_set(self.handle, k, v)
	def __del__(self):
		_cel.DecRef(self.handle)
	def __str__(self):
		s = 'cel.Map_int64_Ptr_expr_Type len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' {'
		if len(self) < 120:
			for k, v in self.items():
				s += str(k) + '=' + str(v) + ', '
		return s + '}'
	def __repr__(self):
		s = 'cel.Map_int64_Ptr_expr_Type({'
		for k, v in self.items():
			s += str(k) + '=' + str(v) + ', '
		return s + '})'
	def __len__(self):
		return _cel.Map_int64_Ptr_expr_Type_len(self.handle)
	def __getitem__(self, key):
		return go.Ptr_expr_Type(handle=_cel.Map_int64_Ptr_expr_Type_elem(self.handle, key))
	def __setitem__(self, key, value):
		_cel.Map_int64_Ptr_expr_Type_set(self.handle, key, value.handle)
	def __delitem__(self, key):
		return _cel.Map_int64_Ptr_expr_Type_delete(self.handle, key)
	def keys(self):
		return go.Slice_int64(handle=_cel.Map_int64_Ptr_expr_Type_keys(self.handle))
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
		return _cel.Map_int64_Ptr_expr_Type_contains(self.handle, key)

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
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = _cel.Map_int64_int32_CTor()
			_cel.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Mapping):
					raise TypeError('Map_int64_int32.__init__ takes a mapping as argument')
				for k, v in args[0].items():
					_cel.Map_int64_int32_set(self.handle, k, v)
	def __del__(self):
		_cel.DecRef(self.handle)
	def __str__(self):
		s = 'cel.Map_int64_int32 len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' {'
		if len(self) < 120:
			for k, v in self.items():
				s += str(k) + '=' + str(v) + ', '
		return s + '}'
	def __repr__(self):
		s = 'cel.Map_int64_int32({'
		for k, v in self.items():
			s += str(k) + '=' + str(v) + ', '
		return s + '})'
	def __len__(self):
		return _cel.Map_int64_int32_len(self.handle)
	def __getitem__(self, key):
		return _cel.Map_int64_int32_elem(self.handle, key)
	def __setitem__(self, key, value):
		_cel.Map_int64_int32_set(self.handle, key, value)
	def __delitem__(self, key):
		return _cel.Map_int64_int32_delete(self.handle, key)
	def keys(self):
		return go.Slice_int64(handle=_cel.Map_int64_int32_keys(self.handle))
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
		return _cel.Map_int64_int32_contains(self.handle, key)


#---- Constants from Go: Python can only ask that you please don't change these! ---
FeatureDisableDynamicAggregateLiterals = 1
OptExhaustiveEval = 3
OptOptimize = 4
OptPartialEval = 8
OptTrackState = 1


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---

# Python type for interface cel.Program
class Program(go.GoClass):
	"""Program is an evaluable view of an Ast.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = 0

# Python type for interface cel.Source
class Source(go.GoClass):
	"""Source interface representing a user-provided expression.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = 0
	def Content(self):
		"""Content() str"""
		return _cel.cel_Source_Content(self.handle)
	def Description(self):
		"""Description() str"""
		return _cel.cel_Source_Description(self.handle)
	def LineOffsets(self):
		"""LineOffsets() []int"""
		return go.Slice_int32(handle=_cel.cel_Source_LineOffsets(self.handle))
	def NewLocation(self, line, col):
		"""NewLocation(int line, int col) object"""
		return go.common_Location(handle=_cel.cel_Source_NewLocation(self.handle, line, col))

# Python type for interface cel.Library
class Library(go.GoClass):
	"""Library provides a collection of EnvOption and ProgramOption values used to confiugre a CEL\nenvironment for a particular use case or with a related set of functionality.\n\nNote, the ProgramOption values provided by a library are expected to be static and not vary\nbetween calls to Env.Program(). If there is a need for such dynamic configuration, prefer to\nconfigure these options outside the Library and within the Env.Program() call directly.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = 0


# ---- Structs ---

# Python type for struct cel.EvalDetails
class EvalDetails(go.GoClass):
	"""EvalDetails holds additional information observed during the Eval() call.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = _cel.cel_EvalDetails_CTor()
			_cel.IncRef(self.handle)
	def __del__(self):
		_cel.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'cel.EvalDetails{'
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
		sv = 'cel.EvalDetails ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def State(self):
		"""State() object
		
		State of the evaluation, non-nil if the OptTrackState or OptExhaustiveEval is specified
		within EvalOptions.
		"""
		return go.interpreter_EvalState(handle=_cel.cel_EvalDetails_State(self.handle))

# Python type for struct cel.Issues
class Issues(go.GoClass):
	"""Issues defines methods for inspecting the error details of parse and check calls.\n\nNote: in the future, non-fatal warnings and notices may be inspectable via the Issues struct.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = _cel.cel_Issues_CTor()
			_cel.IncRef(self.handle)
	def __del__(self):
		_cel.DecRef(self.handle)
	def __str__(self):
		return self.String()
	
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'cel.Issues ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def Err(self):
		"""Err() str
		
		Err returns an error value if the issues list contains one or more errors.
		"""
		return _cel.cel_Issues_Err(self.handle)
	def Errors(self):
		"""Errors() []object
		
		Errors returns the collection of errors encountered in more granular detail.
		"""
		return Slice_common_Error(handle=_cel.cel_Issues_Errors(self.handle))
	def Append(self, other):
		"""Append(object other) object
		
		Append collects the issues from another Issues struct into a new Issues object.
		"""
		return Issues(handle=_cel.cel_Issues_Append(self.handle, other.handle))
	def String(self):
		"""String() str
		
		String converts the issues to a suitable display string.
		"""
		return _cel.cel_Issues_String(self.handle)

# Python type for struct cel.Ast
class Ast(go.GoClass):
	"""Ast representing the checked or unchecked expression, its source, and related metadata such as\nsource position information.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = _cel.cel_Ast_CTor()
			_cel.IncRef(self.handle)
	def __del__(self):
		_cel.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'cel.Ast{'
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
		sv = 'cel.Ast ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def Expr(self):
		"""Expr() object
		
		Expr returns the proto serializable instance of the parsed/checked expression.
		"""
		return go.Ptr_expr_Expr(handle=_cel.cel_Ast_Expr(self.handle))
	def IsChecked(self):
		"""IsChecked() bool
		
		IsChecked returns whether the Ast value has been successfully type-checked.
		"""
		return _cel.cel_Ast_IsChecked(self.handle)
	def SourceInfo(self):
		"""SourceInfo() object
		
		SourceInfo returns character offset and newling position information about expression elements.
		"""
		return go.Ptr_expr_SourceInfo(handle=_cel.cel_Ast_SourceInfo(self.handle))
	def ResultType(self):
		"""ResultType() object
		
		ResultType returns the output type of the expression if the Ast has been type-checked, else
		returns decls.Dyn as the parse step cannot infer the type.
		"""
		return go.Ptr_expr_Type(handle=_cel.cel_Ast_ResultType(self.handle))
	def Source(self):
		"""Source() object
		
		Source returns a view of the input used to create the Ast. This source may be complete or
		constructed from the SourceInfo.
		"""
		return Source(handle=_cel.cel_Ast_Source(self.handle))

# Python type for struct cel.Env
class Env(go.GoClass):
	"""Env encapsulates the context necessary to perform parsing, type checking, or generation of\nevaluable programs for different expressions.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_cel.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_cel.IncRef(self.handle)
		else:
			self.handle = _cel.cel_Env_CTor()
			_cel.IncRef(self.handle)
	def __del__(self):
		_cel.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'cel.Env{'
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
		sv = 'cel.Env ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def HasFeature(self, flag):
		"""HasFeature(int flag) bool
		
		HasFeature checks whether the environment enables the given feature
		flag, as enumerated in options.go.
		"""
		return _cel.cel_Env_HasFeature(self.handle, flag)
	def SetFeature(self, flag, goRun=False):
		"""SetFeature(int flag) 
		
		SetFeature sets the given feature flag, as enumerated in options.go.
		"""
		_cel.cel_Env_SetFeature(self.handle, flag, goRun)
	def TypeAdapter(self):
		"""TypeAdapter() object
		
		TypeAdapter returns the `ref.TypeAdapter` configured for the environment.
		"""
		return go.ref_TypeAdapter(handle=_cel.cel_Env_TypeAdapter(self.handle))
	def TypeProvider(self):
		"""TypeProvider() object
		
		TypeProvider returns the `ref.TypeProvider` configured for the environment.
		"""
		return go.ref_TypeProvider(handle=_cel.cel_Env_TypeProvider(self.handle))
	def UnknownVars(self):
		"""UnknownVars() object
		
		UnknownVars returns an interpreter.PartialActivation which marks all variables
		declared in the Env as unknown AttributePattern values.
		
		Note, the UnknownVars will behave the same as an interpreter.EmptyActivation
		unless the PartialAttributes option is provided as a ProgramOption.
		"""
		return go.interpreter_PartialActivation(handle=_cel.cel_Env_UnknownVars(self.handle))
	def ResidualAst(self, a, details):
		"""ResidualAst(object a, object details) object, str
		
		ResidualAst takes an Ast and its EvalDetails to produce a new Ast which only contains the
		attribute references which are unknown.
		
		Residual expressions are beneficial in a few scenarios:
		
		- Optimizing constant expression evaluations away.
		- Indexing and pruning expressions based on known input arguments.
		- Surfacing additional requirements that are needed in order to complete an evaluation.
		- Sharing the evaluation of an expression across multiple machines/nodes.
		
		For example, if an expression targets a 'resource' and 'request' attribute and the possible
		values for the resource are known, a PartialActivation could mark the 'request' as an unknown
		interpreter.AttributePattern and the resulting ResidualAst would be reduced to only the parts
		of the expression that reference the 'request'.
		
		Note, the expression ids within the residual AST generated through this method have no
		correlation to the expression ids of the original AST.
		
		See the PartialVars helper for how to construct a PartialActivation.
		
		TODO: Consider adding an option to generate a Program.Residual to avoid round-tripping to an
		Ast format and then Program again.
		"""
		return Ast(handle=_cel.cel_Env_ResidualAst(self.handle, a.handle, details.handle))


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---
def NewIssues(errs):
	"""NewIssues(object errs) object
	
	NewIssues returns an Issues struct from a common.Errors object.
	"""
	return Issues(handle=_cel.cel_NewIssues(errs.handle))
def ParsedExprToAst(parsedExpr):
	"""ParsedExprToAst(object parsedExpr) object
	
	ParsedExprToAst converts a parsed expression proto message to an Ast.
	"""
	return Ast(handle=_cel.cel_ParsedExprToAst(parsedExpr.handle))
def CheckedExprToAst(checkedExpr):
	"""CheckedExprToAst(object checkedExpr) object
	
	CheckedExprToAst converts a checked expression proto message to an Ast.
	"""
	return Ast(handle=_cel.cel_CheckedExprToAst(checkedExpr.handle))


# ---- Functions ---
def AstToString(a):
	"""AstToString(object a) str, str
	
	AstToString converts an Ast back to a string if possible.
	
	Note, the conversion may not be an exact replica of the original expression, but will produce
	a string that is semantically equivalent and whose textual representation is stable.
	"""
	return _cel.cel_AstToString(a.handle)
def AttributePattern(varName):
	"""AttributePattern(str varName) object
	
	AttributePattern returns an AttributePattern that matches a top-level variable. The pattern is
	mutable, and its methods support the specification of one or more qualifier patterns.
	
	For example, the AttributePattern(`a`).QualString(`b`) represents a variable access `a` with a
	string field or index qualification `b`. This pattern will match Attributes `a`, and `a.b`,
	but not `a.c`.
	
	When using a CEL expression within a container, e.g. a package or namespace, the variable name
	in the pattern must match the qualified name produced during the variable namespace resolution.
	For example, when variable `a` is declared within an expression whose container is `ns.app`, the
	fully qualified variable name may be `ns.app.a`, `ns.a`, or `a` per the CEL namespace resolution
	rules. Pick the fully qualified variable name that makes sense within the container as the
	AttributePattern `varName` argument.
	
	See the interpreter.AttributePattern and interpreter.AttributeQualifierPattern for more info
	about how to create and manipulate AttributePattern values.
	"""
	return go.Ptr_interpreter_AttributePattern(handle=_cel.cel_AttributePattern(varName))
def NoVars():
	"""NoVars() object
	
	NoVars returns an empty Activation.
	"""
	return go.interpreter_Activation(handle=_cel.cel_NoVars())
def AstToCheckedExpr(a):
	"""AstToCheckedExpr(object a) object, str
	
	AstToCheckedExpr converts an Ast to an protobuf CheckedExpr value.
	
	If the Ast.IsChecked() returns false, this conversion method will return an error.
	"""
	return go.Ptr_expr_CheckedExpr(handle=_cel.cel_AstToCheckedExpr(a.handle))
def AstToParsedExpr(a):
	"""AstToParsedExpr(object a) object, str
	
	AstToParsedExpr converts an Ast to an protobuf ParsedExpr value.
	"""
	return go.Ptr_expr_ParsedExpr(handle=_cel.cel_AstToParsedExpr(a.handle))


