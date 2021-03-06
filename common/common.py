"""
Package common defines types and utilities common to expression parsing,
checking, and interpretation

package common defines types common to parsing and other diagnostics.

package common defines types common to parsing and other diagnostics.

"""
# python wrapper for package github.com/google/cel-go/common within overall package common
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy build -output=common github.com/google/cel-go/common

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
import _common
os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from common import common
# and then refer to everything using common. prefix
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
			_common.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_common.IncRef(self.handle)
		else:
			self.handle = _common.Slice_Ptr_expr_Expr_CTor()
			_common.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_Ptr_expr_Expr.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_common.DecRef(self.handle)
	def __str__(self):
		s = 'common.Slice_Ptr_expr_Expr len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'common.Slice_Ptr_expr_Expr([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _common.Slice_Ptr_expr_Expr_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.Ptr_expr_Expr(handle=_common.Slice_Ptr_expr_Expr_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_common.Slice_Ptr_expr_Expr_set(self.handle, idx, value.handle)
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
			rv = _common.Slice_Ptr_expr_Expr_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_common.Slice_Ptr_expr_Expr_append(self.handle, value.handle)
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
			_common.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_common.IncRef(self.handle)
		else:
			self.handle = _common.Slice_Ptr_expr_Expr_CreateStruct_Entry_CTor()
			_common.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_Ptr_expr_Expr_CreateStruct_Entry.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_common.DecRef(self.handle)
	def __str__(self):
		s = 'common.Slice_Ptr_expr_Expr_CreateStruct_Entry len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'common.Slice_Ptr_expr_Expr_CreateStruct_Entry([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _common.Slice_Ptr_expr_Expr_CreateStruct_Entry_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return go.Ptr_expr_Expr_CreateStruct_Entry(handle=_common.Slice_Ptr_expr_Expr_CreateStruct_Entry_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_common.Slice_Ptr_expr_Expr_CreateStruct_Entry_set(self.handle, idx, value.handle)
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
			rv = _common.Slice_Ptr_expr_Expr_CreateStruct_Entry_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_common.Slice_Ptr_expr_Expr_CreateStruct_Entry_append(self.handle, value.handle)
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
			_common.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_common.IncRef(self.handle)
		else:
			self.handle = _common.Slice_common_Error_CTor()
			_common.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Iterable):
					raise TypeError('Slice_common_Error.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_common.DecRef(self.handle)
	def __str__(self):
		s = 'common.Slice_common_Error len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'common.Slice_common_Error([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _common.Slice_common_Error_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return Error(handle=_common.Slice_common_Error_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_common.Slice_common_Error_set(self.handle, idx, value.handle)
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
	def __next__(self):
		if self.index < len(self):
			rv = _common.Slice_common_Error_elem(self.handle, self.index)
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_common.Slice_common_Error_append(self.handle, value.handle)
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
			_common.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_common.IncRef(self.handle)
		else:
			self.handle = _common.Map_int64_Ptr_expr_Expr_CTor()
			_common.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Mapping):
					raise TypeError('Map_int64_Ptr_expr_Expr.__init__ takes a mapping as argument')
				for k, v in args[0].items():
					_common.Map_int64_Ptr_expr_Expr_set(self.handle, k, v)
	def __del__(self):
		_common.DecRef(self.handle)
	def __str__(self):
		s = 'common.Map_int64_Ptr_expr_Expr len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' {'
		if len(self) < 120:
			for k, v in self.items():
				s += str(k) + '=' + str(v) + ', '
		return s + '}'
	def __repr__(self):
		s = 'common.Map_int64_Ptr_expr_Expr({'
		for k, v in self.items():
			s += str(k) + '=' + str(v) + ', '
		return s + '})'
	def __len__(self):
		return _common.Map_int64_Ptr_expr_Expr_len(self.handle)
	def __getitem__(self, key):
		return go.Ptr_expr_Expr(handle=_common.Map_int64_Ptr_expr_Expr_elem(self.handle, key))
	def __setitem__(self, key, value):
		_common.Map_int64_Ptr_expr_Expr_set(self.handle, key, value.handle)
	def __delitem__(self, key):
		return _common.Map_int64_Ptr_expr_Expr_delete(self.handle, key)
	def keys(self):
		return go.Slice_int64(handle=_common.Map_int64_Ptr_expr_Expr_keys(self.handle))
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
		return _common.Map_int64_Ptr_expr_Expr_contains(self.handle, key)

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
			_common.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_common.IncRef(self.handle)
		else:
			self.handle = _common.Map_int64_int32_CTor()
			_common.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], collections.Mapping):
					raise TypeError('Map_int64_int32.__init__ takes a mapping as argument')
				for k, v in args[0].items():
					_common.Map_int64_int32_set(self.handle, k, v)
	def __del__(self):
		_common.DecRef(self.handle)
	def __str__(self):
		s = 'common.Map_int64_int32 len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' {'
		if len(self) < 120:
			for k, v in self.items():
				s += str(k) + '=' + str(v) + ', '
		return s + '}'
	def __repr__(self):
		s = 'common.Map_int64_int32({'
		for k, v in self.items():
			s += str(k) + '=' + str(v) + ', '
		return s + '})'
	def __len__(self):
		return _common.Map_int64_int32_len(self.handle)
	def __getitem__(self, key):
		return _common.Map_int64_int32_elem(self.handle, key)
	def __setitem__(self, key, value):
		_common.Map_int64_int32_set(self.handle, key, value)
	def __delitem__(self, key):
		return _common.Map_int64_int32_delete(self.handle, key)
	def keys(self):
		return go.Slice_int64(handle=_common.Map_int64_int32_keys(self.handle))
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
		return _common.Map_int64_int32_contains(self.handle, key)


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---
def NoLocation():
	"""
	NoLocation Gets Go Variable: common.NoLocation
	
	"""
	return SourceLocation(handle=_common.common_NoLocation())

def Set_NoLocation(value):
	"""
	Set_NoLocation Sets Go Variable: common.NoLocation
	
	"""
	if isinstance(value, go.GoClass):
		_common.common_Set_NoLocation(value.handle)
	else:
		_common.common_Set_NoLocation(value)



# ---- Interfaces ---

# Python type for interface common.Location
class Location(go.GoClass):
	"""Location interface to represent a location within Source.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_common.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_common.IncRef(self.handle)
		else:
			self.handle = 0
	def Column(self):
		"""Column() int"""
		return _common.common_Location_Column(self.handle)
	def Line(self):
		"""Line() int"""
		return _common.common_Location_Line(self.handle)

# Python type for interface common.Source
class Source(go.GoClass):
	"""Source interface for filter source contents.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_common.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_common.IncRef(self.handle)
		else:
			self.handle = 0
	def Content(self):
		"""Content() str"""
		return _common.common_Source_Content(self.handle)
	def Description(self):
		"""Description() str"""
		return _common.common_Source_Description(self.handle)
	def LineOffsets(self):
		"""LineOffsets() []int"""
		return go.Slice_int32(handle=_common.common_Source_LineOffsets(self.handle))
	def NewLocation(self, line, col):
		"""NewLocation(int line, int col) object"""
		return Location(handle=_common.common_Source_NewLocation(self.handle, line, col))


# ---- Structs ---

# Python type for struct common.Errors
class Errors(go.GoClass):
	"""Errors type which contains a list of errors observed during parsing.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_common.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_common.IncRef(self.handle)
		else:
			self.handle = _common.common_Errors_CTor()
			_common.IncRef(self.handle)
	def __del__(self):
		_common.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'common.Errors{'
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
		sv = 'common.Errors ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def GetErrors(self):
		"""GetErrors() []object
		
		GetErrors returns the list of observed errors.
		"""
		return Slice_common_Error(handle=_common.common_Errors_GetErrors(self.handle))
	def Append(self, errs):
		"""Append([]object errs) object
		
		Append takes an Errors object as input creates a new Errors object with the current and input
		errors.
		"""
		return Errors(handle=_common.common_Errors_Append(self.handle, errs.handle))
	def ToDisplayString(self):
		"""ToDisplayString() str
		
		ToDisplayString returns the error set to a newline delimited string.
		"""
		return _common.common_Errors_ToDisplayString(self.handle)

# Python type for struct common.SourceLocation
class SourceLocation(go.GoClass):
	"""SourceLocation helper type to manually construct a location.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_common.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_common.IncRef(self.handle)
		else:
			self.handle = _common.common_SourceLocation_CTor()
			_common.IncRef(self.handle)
	def __del__(self):
		_common.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'common.SourceLocation{'
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
		sv = 'common.SourceLocation ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def Line(self):
		"""Line() int
		
		Line returns the 1-based line of the location.
		"""
		return _common.common_SourceLocation_Line(self.handle)
	def Column(self):
		"""Column() int
		
		Column returns the 0-based column number of the location.
		"""
		return _common.common_SourceLocation_Column(self.handle)

# Python type for struct common.Error
class Error(go.GoClass):
	"""Error type which references a location within source and a message.\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_common.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_common.IncRef(self.handle)
		else:
			self.handle = _common.common_Error_CTor()
			_common.IncRef(self.handle)
			if  0 < len(args):
				self.Location = args[0]
			if "Location" in kwargs:
				self.Location = kwargs["Location"]
			if  1 < len(args):
				self.Message = args[1]
			if "Message" in kwargs:
				self.Message = kwargs["Message"]
	def __del__(self):
		_common.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'common.Error{'
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
		sv = 'common.Error ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def Location(self):
		return Location(handle=_common.common_Error_Location_Get(self.handle))
	@Location.setter
	def Location(self, value):
		if isinstance(value, go.GoClass):
			_common.common_Error_Location_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def Message(self):
		return _common.common_Error_Message_Get(self.handle)
	@Message.setter
	def Message(self, value):
		if isinstance(value, go.GoClass):
			_common.common_Error_Message_Set(self.handle, value.handle)
		else:
			_common.common_Error_Message_Set(self.handle, value)
	def ToDisplayString(self, source):
		"""ToDisplayString(object source) str
		
		ToDisplayString decorates the error message with the source location.
		"""
		return _common.common_Error_ToDisplayString(self.handle, source.handle)


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---
def NewErrors(source):
	"""NewErrors(object source) object
	
	NewErrors creates a new instance of the Errors type.
	"""
	return Errors(handle=_common.common_NewErrors(source.handle))


# ---- Functions ---
def NewInfoSource(info):
	"""NewInfoSource(object info) object"""
	return Source(handle=_common.common_NewInfoSource(info.handle))
def NewLocation(line, column):
	"""NewLocation(int line, int column) object"""
	return Location(handle=_common.common_NewLocation(line, column))
def NewStringSource(contents, description):
	"""NewStringSource(str contents, str description) object"""
	return Source(handle=_common.common_NewStringSource(contents, description))
def NewTextSource(text):
	"""NewTextSource(str text) object"""
	return Source(handle=_common.common_NewTextSource(text))


