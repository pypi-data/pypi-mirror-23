#!/usr/bin/env python

###############################################################################
# Copyright 2017 - Climate Research Division
#                  Environment and Climate Change Canada
#
# This file is part of the "fstd2nc" package.
#
# "fstd2nc" is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "fstd2nc" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with "fstd2nc".  If not, see <http://www.gnu.org/licenses/>.
###############################################################################


"""
Functionality for converting between FSTD and netCDF files.
"""

__version__ = "0.20170712.1"

# Enable multi-language support.
from gettext import gettext as _
import gettext
from os import path, environ
try:
  import fstd2nc_locale
  gettext.bindtextdomain('fstd2nc', path.dirname(fstd2nc_locale.__file__))
  del fstd2nc_locale
except ImportError: pass
gettext.textdomain('fstd2nc')
# Check for special CMCLNG environment variable
if environ.get('CMCLNG') == 'francais':
  environ['LANGUAGE'] = 'fr_CA'
del gettext, path, environ

# Check for rpnpy package.
try:
  import rpnpy
except ImportError:
  try:
    # If not available in a standard location, check if it's bundled.
    import fstd2nc_deps
  except ImportError:
    pass

# How to handle warning messages.
# E.g., can either pass them through warnings.warn, or simply print them.
def warn (msg):
  print (_("Warning: %s")%msg)

# Override default dtype for "binary" data.
# The one example I've seen has "float32" data encoded in it.
# https://wiki.cmc.ec.gc.ca/wiki/Talk:Python-RPN/2.0/examples#Plot_GIOPS_Forecast_Data_with_Basemap
def dtype_fst2numpy (datyp, nbits=None):
  from rpnpy.librmn.fstd98 import dtype_fst2numpy
  if datyp == 0:
    warn (_("Raw binary records detected.  The values may not be properly decoded if you're opening on a different platform."))
    datyp = 5
  return dtype_fst2numpy(datyp,nbits)


# Helper classes for lazy-array evaluation.

# Common base class for all the numpy-like arrays defined below.
class _Array_Base (object):
  # Set some common attributes for the object.
  def __init__ (self, shape, dtype):
    from functools import reduce
    # Expected shape and type of the array.
    self.shape = tuple(map(int,shape))
    self.ndim = len(self.shape)
    self.size = reduce(int.__mul__, self.shape, 1)
    self.dtype = dtype

# Data from a record.
# Has a 'shape' like a numpy array, but values aren't loaded from file until
# the array is sliced, or passed through np.asarray().
class _Record_Array (_Array_Base):
  def __init__ (self, fstdfile, params):
    shape = (params['ni'],params['nj'],params['nk'])
    dtype = dtype_fst2numpy(params['datyp'], params['nbits'])
    _Array_Base.__init__(self, shape, dtype)
    # Keep a reference to the file so it doesn't get closed until after this
    # object is destroyed.
    # Otherwise, the key will become invalid.
    self._fstdfile = fstdfile
    self._key = params['key']
  def __getitem__ (self, key):
    return self.__array__().__getitem__(key)
  def __array__ (self):
    # Adapted from rpnpy.librmn.fstd98.fstluk
    import ctypes as _ct
    import numpy as _np
    from rpnpy.librmn import proto as _rp
    from rpnpy.librmn.fstd98 import FSTDError
    import numpy.ctypeslib as _npc
    (cni, cnj, cnk) = (_ct.c_int(), _ct.c_int(), _ct.c_int())
    data = _np.empty(self.shape, dtype=self.dtype, order='FORTRAN')
    _rp.c_fstluk.argtypes = (_npc.ndpointer(dtype=self.dtype), _ct.c_int,
                             _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int),
                             _ct.POINTER(_ct.c_int))
    istat = _rp.c_fstluk(data, self._key, _ct.byref(cni), _ct.byref(cnj),
                             _ct.byref(cnk))
    if istat < 0:
      raise FSTDError()
    return data

# Missing data.
class _NaN_Array (_Array_Base):
  def __init__ (self,*shape):
    _Array_Base.__init__(self,shape,'float32')
  def __getitem__ (self,key):
    return self.__array__().__getitem__(key)
  def __array__ (self):
    import numpy as np
    data = np.empty(self.shape,dtype=self.dtype,order='FORTRAN')
    data[()] = float('nan')
    return data

# Combine multiple array-like objects into a higher-dimensional array-like
# object.
# E.g., If you have a numpy array of dimensions (time,level), of type 'object',
# and each element is a _Record_Array object of dimenions (ni,nj,nk), then
# this will give you a new array-like object of dimenions (time,level,ni,nj,nk)
# that can be manipulated like a numpy array (e.g. sliced, tranposed).
# The values won't be loaded until the object is passed to numpy.asarray().
class _Array (_Array_Base):
  @classmethod
  # Create the object from an array of array-like objects.
  def create (cls, data):
    import numpy as np
    # Special case: have a single array (not an array of arrays).
    if data.dtype.name != 'object':
      outer_shape = ()
      inner_shape = data.shape
      dtype = data.dtype
    # Usual case (array of array-like objects).
    else:
      outer_shape = data.shape
      # Inner array objects must all have the same shape.
      inner_shape = set(map(np.shape,data.flatten()))
      if len(inner_shape) > 1:
        raise ValueError (("Different shapes for inner array objects.  Found shapes: %s")%list(inner_shape))
      inner_shape = inner_shape.pop()
      dtype = np.result_type(*data.flatten())
    shape = tuple(outer_shape) + tuple(inner_shape)
    # Define a map from outer axes to inner axes.
    inner_dimids = [None]*len(outer_shape) + list(range(len(inner_shape)))
    inner_slices = [slice(None)]*len(inner_shape)
    return cls(shape, dtype, inner_dimids, data, inner_slices)
  def __init__ (self, shape, dtype, inner_dimids, data, inner_slices):
    assert len(shape) == len(inner_dimids)
    _Array_Base.__init__(self, shape, dtype)
    # Check if we have a dengenerate outer array.
    self._degenerate = not any(i is None for i in inner_dimids)
    # Check outer dimensions
    if not self._degenerate:
      assert sum(i is None for i in inner_dimids) == data.ndim
    # Map the full axes to the inner (record) axes.
    # Set to 'None' for outer axes not part of the record.
    self._inner_dimids = tuple(inner_dimids)
    # Array of references to the data from the FSTD records.
    self._data = data
    # Extra slicing to be done to the record data after reading it in.
    self._inner_slices = tuple(inner_slices)
  def __getitem__ (self, key):
    from itertools import product
    # Coerce key into a tuple of slice objects.
    if not isinstance(key,tuple):
      if hasattr(key,'__len__'): key = tuple(key)
      else: key = (key,)
    if len(key) == 1 and hasattr(key[0],'__len__'):
      key = tuple(key[0])
    if Ellipsis in key:
      i = key.index(Ellipsis)
      key = key[:i] + (slice(None),)*(self.ndim-len(key)+1) + key[i+1:]
    key = key + (slice(None),)*(self.ndim-len(key))
    if len(key) > self.ndim:
      raise ValueError(("Too many dimensions for slicing."))
    shape = []
    inner_dimids = []
    outer_slices = []
    inner_slices = list(self._inner_slices)
    for sl,n,i in zip(key,self.shape,self._inner_dimids):
      # Only retain dimenions that aren't reduced out.
      if not isinstance(sl,int):
        shape.append(len(range(n)[sl]))
        inner_dimids.append(i)
      # Outer slice?
      if i is None:
        outer_slices.append(sl)
      # Inner slice?
      else:
        S = inner_slices[i]
        start = S.start or 0
        stop = S.stop
        step = S.step or 1
        if isinstance(sl,int):
          inner_slices[i] = start + step*sl
        else:
          if sl.stop is not None:
            stop = start + step*sl.stop
          start = start + step*(sl.start or 0)
          step = step * (sl.step or 1)
          inner_slices[i] = slice(start,stop,step)

    data = self._data.__getitem__(tuple(outer_slices))
    return _Array(shape, self.dtype, inner_dimids, data, inner_slices)

  # Remove degenerate dimensions from the array.
  def squeeze (self, axis=None):
    if isinstance(axis,int):
      axis = (axis,)
    if axis is None:
      axis = [i for i,s in enumerate(self.shape) if s == 1]
    key = [slice(None)]*self.ndim
    for a in axis:
      if self.shape[a] > 1:
        raise ValueError(("Can only squeeze axes of length 1."))
      key[a] = 0
    return self.__getitem__(tuple(key))

  # Change the order of the dimensions
  def transpose (self, *axes):
    if len(axes) == 0:
      axes = tuple(range(self.ndim-1,-1,-1))
    if len(axes) == 1 and hasattr(axes[0],'__len__'):
      axes = tuple(axes[0])
    if len(axes) != self.ndim:
      raise ValueError(("Wrong number of dimenions for transpose."))
    if sorted(axes) != list(range(self.ndim)):
      raise ValueError(("Bad axis arguments."))
    shape = [self.shape[a] for a in axes]
    inner_dimids = [self._inner_dimids[a] for a in axes]
    return _Array(shape, self.dtype, inner_dimids, self._data, self._inner_slices)

  # Allow this object to be loaded into a numpy array.
  def __array__ (self):
    import numpy as np
    from itertools import product
    # Final order of inner axes
    trans = [i for i in self._inner_dimids if i is not None]
    # Adjust the axis numbers in transpose operation
    # to account for any slicing that was done.
    for i,s in list(enumerate(self._inner_slices))[::-1]:
      if isinstance(s,int):
        trans = [t if t<i else t-1 for t in trans if t != i]
    # Outer array is degenerate?
    if self._degenerate:
      return np.asarray(self._data[self._inner_slices]).transpose(*trans)
    # Get indices of all dimensions, in preparation for iterating.
    indices = [range(s) if i is None else [slice(None)] for i,s in zip(self._inner_dimids, self.shape)]
    data = np.empty(self.shape, dtype=self.dtype)
    for i,ind in enumerate(product(*indices)):
      data[ind] = np.asarray(self._data.flatten()[i][self._inner_slices]).transpose(*trans)
    return data

# Helper class - keep an FSTD file open until all references are destroyed.
class _FSTD_File (object):
  def __init__ (self, filename, mode):
    import rpnpy.librmn.all as rmn
    from rpnpy.librmn.base import fnom
    from rpnpy.librmn.fstd98 import fstouv
    self.filename = filename
    self.funit = fnom(filename, mode)
    fstouv(self.funit, mode)
  def __del__ (self):
    from rpnpy.librmn.fstd98 import fstfrm
    from rpnpy.librmn.base import fclos
    istat = fstfrm(self.funit)
    istat = fclos(self.funit)

# The type of data returned by the Buffer iterator.
from collections import namedtuple
_var_type = namedtuple('var', ('name','atts','axes','array'))
del namedtuple


# Define a class for encoding / decoding FSTD data.
# Each step is placed in its own "mixin" class, to make it easier to patch in 
# new behaviour if more exotic FSTD files are encountered in the future.
class _Buffer_Base (object):

  # Names of records that should be kept separate (never grouped into
  # multidimensional arrays).
  _meta_records = ()

  # Attributes which could potentially be used as axes.
  _outer_axes = ()

  # Attributes which uniquely identify a variable.
  _var_id = ('nomvar','ni','nj','nk')

  # Similar to above, but a human-readable version of the id.
  # Could be used for appending suffixes to variable names to make them unique.
  # Uses string formatting operations on the variable metadata.
  _human_var_id = ('%(nomvar)s', '%(ni)sx%(nj)s', '%(nk)sL')

  # Record parameters which should not be used as nc variable attributes.
  # (They're either internal to the file, or part of the data, not metadata).
  _ignore_atts = ('swa','lng','dltf','ubc','xtra1','xtra2','xtra3','key','shape','d')

  # Define any command-line arguments for reading FSTD files.
  @classmethod
  def _cmdline_args (cls, parser):
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('--minimal-metadata', action='store_true', help=_("Don't include FSTD record attributes and other internal information in the output file."))
    parser.add_argument('--ignore-typvar', action='store_true', help=_('Tells the converter to ignore the typvar when deciding if two records are part of the same field.  Default is to split the variable on different typvars.'))
    parser.add_argument('--ignore-etiket', action='store_true', help=_('Tells the converter to ignore the etiket when deciding if two records are part of the same field.  Default is to split the variable on different etikets.'))

  # Do some checks on the command-line arguments after parsing them.
  @classmethod
  def _check_args (cls, parser, args):
    return  # Nothing to check here.

  def __init__ (self, minimal_metadata=False, ignore_typvar=False, ignore_etiket=False):
    """
    Create a new, empty buffer.
    """
    self._params = []
    self._minimal_metadata = minimal_metadata
    if not ignore_typvar:
      # Insert typvar value just after nomvar.
      self._var_id = self._var_id[0:1] + ('typvar',) + self._var_id[1:]
      self._human_var_id = self._human_var_id[0:1] + ('%(typvar)s',) + self._human_var_id[1:]
    if not ignore_etiket:
      # Insert etiket value just after nomvar.
      self._var_id = self._var_id[0:1] + ('etiket',) + self._var_id[1:]
      self._human_var_id = self._human_var_id[0:1] + ('%(etiket)s',) + self._human_var_id[1:]

  # Extract metadata from a particular header.
  def _get_header_atts (self, header):
    for n,v in header.items():
      if n in self._ignore_atts: continue
      if isinstance(v,str):
        v = v.strip()
      yield (n,v)

  def clear (self):
    """
    Removes all existing data from the buffer.
    """
    self._params = []


  ###############################################
  # Basic flow for reading data

  def read_fstd_file (self, filename):
    """
    Read raw records from an FSTD file, into the buffer.
    Multiple files can be read sequentially.
    """
    import numpy as np
    from rpnpy.librmn.fstd98 import fstinl, fstprm, fstluk
    from rpnpy.librmn.const import FST_RO
    # Read the data
    f = _FSTD_File(filename,FST_RO)
    keys = fstinl(f.funit)
    for i,key in enumerate(keys):
      prm = fstprm(key)
      prm['d'] = _Record_Array(f,prm)
      self._params.append(prm)

  # Collect the list of params from all the FSTD records, and concatenate them
  # into arrays.  Result is a single dictionary containing the vectorized
  # parameters of all records.
  # The sole purpose of this routine is to put the metadata in a structure
  # that's more efficient for doing bulk (vectorized) manipulations, instead
  # of manipulating each record param dictionary one at a time.
  # Subclasses may also insert extra (non-FSTD) parameters in here which are
  # needed for doing the variable decoding.
  def _vectorize_params (self):
    from collections import OrderedDict
    import numpy as np
    # Make sure the parameter names are consistent for all records.
    if len(set(map(frozenset,self._params))) != 1:
      raise ValueError(("Inconsistent parameter names for the records."))
    fields = OrderedDict()
    for prm in self._params:
      for n,v in prm.items():
        fields.setdefault(n,[]).append(v)
    for n,v in list(fields.items()):
      # Treat array-like objects specially (don't want numpy to try to
      # read the data).
      if hasattr(v[0],'__array__'):
        v2 = v
        v = np.empty(len(self._params),dtype='O')
        v[:] = v2
      fields[n] = np.asarray(v)
    return fields


  def __iter__ (self):
    """
    Processes the records into multidimensional variables.
    Iterates over (name, atts, axes, array) tuples.
    Note that array may not be a true numpy array (values are not yet loaded
    in memory).  To load the array, pass it to numpy.asarray().
    """
    from collections import OrderedDict, namedtuple
    import numpy as np

    # Degenerate case: no data in buffer
    if len(self._params) == 0: return

    records = self._vectorize_params()

    # Group the records by variable.
    var_records = OrderedDict()
    var_id_type = namedtuple('var_id', self._var_id)
    for i in range(len(records['nomvar'])):
      # Get the unique variable identifiers.
      var_id = var_id_type(*[records[n][i] for n in self._var_id])
      # Ignore coordinate records.
      if var_id.nomvar.strip() in self._meta_records: continue
      var_records.setdefault(var_id,[]).append(i)

    # Loop over each variable and construct the data & metadata.
    for var_id, rec_ids in var_records.items():
      # Get the metadata for each record.
      atts = OrderedDict()
      for n in records.keys():
        if n in self._outer_axes or n in self._ignore_atts: continue
        v = records[n][rec_ids]
        # Remove missing values before continuing.
        v = np.ma.compressed(v)
        if len(v) == 0: continue
        # Only use attributes that are consistent across all variable records.
        if len(set(v)) > 1: continue
        v = v[0]
        # Trim string attributes (remove whitespace padding).
        if isinstance(v,str): v = v.strip()
        atts[n] = v

      # Get the axis coordinates.
      axes =  OrderedDict()
      for n in self._outer_axes:
        values = records[n][rec_ids]
        # Remove missing values before continuing.
        values = np.ma.compressed(values)
        # Ignore axes that have no actual coordinate values.
        if len(values) == 0: continue
        # Get all unique values (sorted).
        values = tuple(sorted(set(values)))
        axes[n] = values

      # Construct a multidimensional array to hold the data functions.
      data = np.empty(map(len,axes.values()), dtype='O')

      # Assume missing data (nan) unless filled in later.
      missing = _NaN_Array(var_id.ni, var_id.nj, var_id.nk)
      data.fill(missing)
      
      # Arrange the data funcs in the appropriate locations.
      for rec_id in rec_ids:
        index = tuple(axes[n].index(records[n][rec_id]) for n in axes.keys())
        data[index] = records['d'][rec_id]

      # Check if we have full coverage along all axes.
      have_data = [d is not missing for d in data.flatten()]
      if not np.all(have_data):
        warn (_("Missing some records for %s.")%var_id.nomvar)

      data = _Array.create (data)

      # Put the i,j,k dimensions in C order.
      data = data.transpose(list(range(data.ndim-3))+[data.ndim-1,data.ndim-2,data.ndim-3])

      axes['k'] = tuple(range(var_id.nk))
      axes['j'] = tuple(range(var_id.nj))
      axes['i'] = tuple(range(var_id.ni))

      yield _var_type(var_id.nomvar.strip(), atts, axes, data)

      #TODO: Find a minimum set of partial coverages for the data.
      # (e.g., if we have surface-level output for some times, and 3D output
      # for other times).

  #
  ###############################################




#####################################################################
# Mixins for different features / behaviour for the conversions.


#################################################
# Selecting for particular fields.
class _SelectVars (_Buffer_Base):
  @classmethod
  def _cmdline_args (cls, parser):
    super(_SelectVars,cls)._cmdline_args(parser)
    parser.add_argument('--vars', metavar='VAR1,VAR2,...', help=_('Comma-separated list of variables to convert.  By default, all variables are converted.'))
  def __init__ (self, vars=None, *args, **kwargs):
    if vars is not None:
      self._selected_vars = vars.split(',')
      print (_('Looking for variables: ') + ' '.join(self._selected_vars))
    else:
      self._selected_vars = None
    super(_SelectVars,self).__init__(*args,**kwargs)
  def __iter__ (self):
    for var in super(_SelectVars,self).__iter__():
      if self._selected_vars is not None:
        if var.name not in self._selected_vars:
          continue
      yield var


#################################################
# Logic for handling masks.

class _MaskedArray (_Array_Base):
  def __init__ (self, data, mask, fill):
    _Array_Base.__init__(self,data.shape,data.dtype)
    self._data = data
    self._mask = mask
    self._fill = fill
  def __array__ (self):
    import numpy as np
    data = np.array(self._data)
    mask = np.array(self._mask)
    data[mask==0] = self._fill
    return data
  def __getitem__ (self, key):
    return _MaskedArray(self._data.__getitem__(key), self._mask.__getitem__(key), self._fill)
  def squeeze (self, axis=None):
    return _MaskedArray(self._data.squeeze(axis), self._mask.squeeze(axis), self._fill)
  def transpose (self, *axes):
    return MaskedArray(self._data.transpos(*axes), self._mask.transpose(*axes), self._fill)
class _Masks (_Buffer_Base):
  @classmethod
  def _cmdline_args (cls, parser):
    super(_Masks,cls)._cmdline_args(parser)
    parser.add_argument('--fill-value', type=float, default=1e30, help=_("The fill value to use for masked (missing) data.  Gets stored as '_FillValue' attribute in the netCDF file.  Default is '%(default)s'."))
  def __init__ (self, fill_value=1e30, *args, **kwargs):
    # Assume we have a 1:1 correspondence between data records and mask
    # records, and that mask records are identified by nbits=1.
    # Under these assumptions, can attach the mask by defining an outer 'axis'
    # of length 2, which selects between mask/data arrays.
    #TODO: Make this more robust if necessary.
    #      E.g., are there cases where we have a 2D mask (lat,lon)
    #      applied to a 3D field (time,lat,lon) or (lat,lon,level)?
    self._outer_axes = ('is_mask',) + self._outer_axes
    self._fill_value = fill_value
    super(_Masks,self).__init__(*args,**kwargs)
  # Identify whether a record is a mask or data field.
  # Allows the decoder to stick these fields together over an 'is_mask' axis.
  def _vectorize_params (self):
    import numpy as np
    fields = super(_Masks,self)._vectorize_params()
    nrecs = len(fields['nomvar'])
    # Organize records based on whether they're mask or data.
    fields['is_mask'] = fields['nbits'] == 1
    # Typvar may be different between mask / data, so store both versions.
    # Blank out 'typvar' for mask records, and blank out 'mask_typvar'
    # for mask records.  Obviously.
    fields['mask_typvar'] = np.ma.array(fields['typvar'])
    fields['mask_typvar'].mask = ~fields['is_mask']
    fields['typvar'] = np.ma.asarray(fields['typvar'])
    fields['typvar'].mask = fields['is_mask']
    return fields
  # Apply the mask to the data.
  def __iter__ (self):
    from collections import OrderedDict
    import numpy as np
    for var in super(_Masks,self).__iter__():
      if 'is_mask' not in var.axes:
        yield var
        continue
      axes = OrderedDict(var.axes)
      mask_dim = list(axes.keys()).index('is_mask')
      # Do we have a mask/data pair?
      if len(axes['is_mask']) > 1:
        data = var.array[(slice(None),)*mask_dim+(0,)]
        mask = var.array[(slice(None),)*mask_dim+(1,)]
        # Apply the mask
        data = _MaskedArray(data,mask,fill=self._fill_value)
        var.atts['_FillValue'] = self._fill_value
      else:
        data = var.array.squeeze(axis=mask_dim)
      del axes['is_mask']
      yield type(var)(var.name, var.atts, axes, data)


#################################################
# Logic for handling date field.

class _Dates (_Buffer_Base):
  @classmethod
  def _cmdline_args (cls, parser):
    super(_Dates,cls)._cmdline_args(parser)
    parser.add_argument('--squash-forecasts', action='store_true', help=_('Use the date of validity for the "time" axis.  Otherwise, the default is to use the date of original analysis, and the forecast length goes in a "forecast" axis.'))

  def __init__ (self, squash_forecasts=False, *args, **kwargs):
    self._squash_forecasts = squash_forecasts
    if squash_forecasts:
      self._outer_axes = ('time',) + self._outer_axes
    else:
      self._outer_axes = ('time','forecast') + self._outer_axes
    super(_Dates,self).__init__(*args,**kwargs)

  # Get any extra (derived) fields needed for doing the decoding.
  def _vectorize_params (self):
    from rpnpy.rpndate import  RPNDate
    import numpy as np
    fields = super(_Dates,self)._vectorize_params()
    # Calculate the forecast (in hours).
    fields['forecast']=fields['deet']*fields['npas']/3600.
    # Time axis
    if self._squash_forecasts:
      dates = map(int,fields['datev'])
    else:
      dates = map(int,fields['dateo'])
    dates = [RPNDate(d).toDateTime().replace(tzinfo=None) if d > 0 else None for d in dates]
    dates = np.ma.masked_equal(dates,None)
    fields['time'] = dates
    return fields

  # Add time and forecast axes to the data stream.
  def __iter__ (self):
    from collections import OrderedDict
    import numpy as np
    # Keep track of all time and forecast axes found in the data.
    time_axes = set()
    forecast_axes = set()
    for var in super(_Dates,self).__iter__():
      if 'time' in var.axes:
        times = var.axes['time']
        if times not in time_axes:
          time_axes.add(times)
          atts = OrderedDict([('axis','T')])
          axes = OrderedDict([('time',var.axes['time'])])
          # Add the time axis to the data stream.
          yield type(var)('time',atts,axes,np.asarray(times))
      if 'forecast' in var.axes:
        forecasts = var.axes['forecast']
        if forecasts not in forecast_axes:
          forecast_axes.add(forecasts)
          atts = OrderedDict(units='hours')
          axes = OrderedDict([('forecast',var.axes['forecast'])])
          # Add the forecast axis to the data stream.
          yield type(var)('forecast',atts,axes,np.asarray(forecasts))
      yield var



#################################################
# Logic for handling timeseries data.
#
# This is a first attempt at handling these 'series' files as output from
# the GEM model, and may be incomplete / inaccurate.  Please correct this
# section if you notice anything wrong.
#
# There are two types of timeseries records I've seen:
#
# - typvar='T', grtyp='Y'.
#   Here, ni corresponds to horizontal points (like the usual Y-grid).
#   There should be corresponding '^^' and '>>' fields in this case.
#
# - Vertical profiles, which have typvar='T', grtype='+'.
#   This data uses a different meaning for ni and nj.
#   Here, 'ni' is actually the # of vertical levels, and 'nj' is the number of
#   forecast times.  The horizontal points are split per record, and enumerated
#   by the 'ip3' parameter.
#   ig1/ig2 is set to zero in my sample - coincidentally matches ip1/ip2 of
#   !! record.
#   ig3/ig4 give some kind of horizontal coordinate info (?).
#   ip1/ip2 seem to match ip1/ip2 of '^^', '>>' records.
#   'HH' record gives forecast hours corresponding to nj.
#   'SH' and 'SV' give some kind of vertical info corresponding to ni, but
#   with one extra level?
#   'STNS' gives the names of the stations (corresponding to ip3 numbers?)

class _Series (_Buffer_Base):
  def __init__ (self, *args, **kwargs):
    # Don't process series time/station/height records as variables.
    self._meta_records = self._meta_records + ('HH', 'STNS', 'SH', 'SV')
    # Add station # as another axis.
    self._outer_axes = ('station_id',) + self._outer_axes
    super(_Series,self).__init__(*args,**kwargs)
  def _vectorize_params (self):
    import numpy as np
    fields = super(_Series,self)._vectorize_params()
    nrecs = len(fields['nomvar'])
    # Identify timeseries records for further processing.
    is_t_plus = (fields['typvar'] == 'T ') & (fields['grtyp'] == '+')
    # For timeseries data, station # is provided by 'ip3'.
    station_id = np.ma.array(fields['ip3'])
    # For non-timeseries data, ignore this info.
    station_id.mask = ~is_t_plus
    fields['station_id'] = station_id
    # For timeseries data, the usual 'forecast' axis (from deet*npas) is not
    # used.  Instead, we will get forecast info from nj coordinate.
    if 'forecast' in fields:
      fields['forecast'] = np.ma.asarray(fields['forecast'])
      fields['forecast'].mask = is_t_plus
    # True grid identifier is in ip1/ip2?
    # Overwrite the original ig1,ig2,ig3,ig4 values, which aren't actually grid
    # identifiers in this case (they're just the lat/lon coordinates of each
    # station?)
    fields['ig1'][is_t_plus] = fields['ip1'][is_t_plus]
    fields['ig2'][is_t_plus] = fields['ip2'][is_t_plus]
    fields['ig3'][is_t_plus] = 0
    fields['ig4'][is_t_plus] = 0
    return fields
  def __iter__ (self):
    from collections import OrderedDict
    import numpy as np
    # Get station and forecast info.
    # Need to read from original records, because this into isn't in the
    # data stream.
    station = forecast = None
    for header in self._params:
      if header['nomvar'] == 'STNS':
        atts = OrderedDict()
        array = np.asarray(header['d']).squeeze(axis=2).transpose()
        # Re-cast array as string.
        # I don't know why I have to subtract 128 - maybe something to do with
        # how the characters are encoded in the file?
        # This isn't always needed.  Have test files for both cases.
        # Need help making this more robust!
        if array.flatten()[0] >= 128:
          array -= 128
        array = array.view('|S1')
        nstations, strlen = array.shape
        # Strip out trailing whitespace.
        array = array.flatten().view('|S%d'%strlen)
        array[:] = map(str.rstrip,array)
        array = array.view('|S1').reshape(nstations,strlen)
        # Encode it as 2D character array for netCDF file output.
        axes = OrderedDict([('i',tuple(range(nstations))),('station_strlen',tuple(range(strlen)))])
        station = _var_type('station',atts,axes,array)
      if header['nomvar'] == 'HH  ':
        atts = OrderedDict(units='hours')
        array = np.asarray(header['d']).flatten()
        axes = OrderedDict(forecast=tuple(array))
        forecast = _var_type('forecast',atts,axes,array)
    station_outputted = False
    forecast_outputted = False
    for var in super(_Series,self).__iter__():
      # Modify timeseries axes so XYCoords recognizes it.
      if var.atts.get('grtyp') == '+':
        axes = []
        for n,v in var.axes.items():
          # ni is actually vertical level.
          if n == 'i': axes.append(('station_level',v))
          # station_id (from ip3) should become new i axis.
          elif n == 'station_id':
            if station is not None:
              # Output station names as a separate variable.
              if not station_outputted:
                yield station
                station_outputted = True
              axes.append(('i',station.axes['i']))
            else:
              # Deal with case where station (STNS) record isn't available.
              axes.append(('i',v))
          # "borrow" k dimension to be new "j" dimension.
          # XYCoords expects both i and j dimensions, even though only 'i'
          # is really needed for unstructured lat/lon data.
          elif n == 'k' and len(v) == 1: axes.append(('j',v))
          # Original nj is actually forecast time.
          elif n == 'j':
            if forecast is not None:
              # Output forecast hours as a separate variable.
              if not forecast_outputted:
                yield forecast
                forecast_outputted = True
              axes.append(('forecast',forecast.axes['forecast']))
            else:
              # Deal with case where forecast (HH) record isn't available
              axes.append(('t',v))
          else: axes.append((n,v))
        axes = OrderedDict(axes)
        var = type(var)(var.name,var.atts,axes,var.array)
      yield var

#################################################
# Logic for handling vertical coordinates.

class _VCoords (_Buffer_Base):
  _vcoord_nomvars = ('HY','!!')
  def __init__ (self, *args, **kwargs):
    # Use decoded IP1 values as the vertical axis.
    self._outer_axes = ('level',) + self._outer_axes
    # Tell the decoder not to process vertical records as variables.
    self._meta_records = self._meta_records + self._vcoord_nomvars
    super(_VCoords,self).__init__(*args,**kwargs)
    # Don't group records across different level 'kind'.
    # (otherwise can't create a coherent vertical axis).
    self._var_id = self._var_id + ('kind',)
    self._human_var_id = self._human_var_id + ('vgrid%(kind)s',)
  def _vectorize_params (self):
    from rpnpy.librmn.fstd98 import DecodeIp
    import numpy as np
    fields = super(_VCoords,self)._vectorize_params()
    # Provide 'level' and 'kind' information to the decoder.
    decoded = map(DecodeIp,fields['ip1'],fields['ip2'],fields['ip3'])
    rp1 = zip(*decoded)[0]
    levels = np.array([r.v1 for r in rp1])
    kind = np.array([r.kind for r in rp1])
    # Only use first set of levels (can't handle ranges yet).
    fields['level'] = levels
    fields['kind'] = kind
    return fields
  # Add vertical axis as another variable.
  def __iter__ (self):
    from collections import OrderedDict
    import numpy as np
    from rpnpy.vgd.base import vgd_fromlist, vgd_get, vgd_free
    from rpnpy.vgd.const import VGD_KEYS
    from rpnpy.vgd import VGDError
    from rpnpy.librmn.fstd98 import DecodeIp
    # Pre-scan the raw headers for special vertical records.
    # (these aren't available in the data stream, because we told the decoder
    # to ignore them).
    vrecs = OrderedDict()
    for header in self._params:
      if header['nomvar'].strip() not in self._vcoord_nomvars: continue
      key = (header['ip1'],header['ip2'])
      # For old HY records, there's no matching ipX/igX codes.
      if header['nomvar'].strip() == 'HY': key = 'HY'
      if key in vrecs: continue
      vrecs[key] = header

    # Scan through the data, and look for any use of vertical coordinates.
    vaxes = OrderedDict()
    for var in super(_VCoords,self).__iter__():
      # Degenerate vertical axis?
      if 'ip1' in var.atts and var.atts['ip1'] == 0:
        del var.axes['level']
      if 'level' not in var.axes or 'kind' not in var.atts:
        yield var
        continue
      # Decode the vertical coordinate.
      levels = var.axes['level']
      kind = var.atts['kind']
      # Only need to provide one copy of the vertical axis.
      if (levels,kind) not in vaxes:
        # Keep track of any extra arrays needed for this axis.
        ancillary_variables = []
        # Get metadata that's specific to this axis.
        name = 'zaxis'
        atts = OrderedDict()
        atts['axis'] = 'Z'
        # Reference: http://web-mrb.cmc.ec.gc.ca/science//si/eng/si/libraries/rmnlib/fstd/main.html#RTFToC11
        if kind == 0:
          # height [m] (metres)
          name = 'height'
          atts['standard_name'] = 'height'
          atts['units'] = 'm'
          atts['positive'] = 'up'
        elif kind == 1:
          # sigma [sg] (0.0->1.0)
          name = 'sigma'
          atts['standard_name'] = 'atmosphere_sigma_coordinate'
          atts['positive'] = 'down'
        elif kind == 2:
          # pressure [mb] (millibars)
          name = 'pres'
          atts['standard_name'] = 'air_pressure'
          atts['units'] = 'hPa'
          atts['positive'] = 'down'
        elif kind == 3:
          # arbitrary code
          name = 'code'
          atts.pop('axis',None)  # Not really a vertical axis?
        elif kind == 4:
          # height [M] (metres) with respect to ground level
          name = 'height'
          atts['standard_name'] = 'height'
          atts['units'] = 'm'
          atts['positive'] = 'up'
        elif kind == 5:
          # hybrid coordinates [hy] (0.0->1.0)
          atts['positive'] = 'down'
          key = (var.atts['ig1'],var.atts['ig2'])
          if header['nomvar'].strip() == 'HY': key = 'HY'
          if key in vrecs:
            header = vrecs[key]
            # Add in metadata from the coordinate.
            atts.update(self._get_header_atts(header))
            # Add type-specific metadata.
            if header['nomvar'].strip() == '!!':
              # Get A and B info.
              vgd_id = vgd_fromlist(header['d'][...])
              if vgd_get (vgd_id,'LOGP'):
                name = 'zeta'
                # Not really a "standard" name, but there's nothing in the
                # CF convensions document on how to encode this.
                # I just merged the atmosphere_ln_pressure_coordinate and
                # atmosphere_hybrid_sigma_pressure_coordinate together.
                # http://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#dimensionless-v-coord
                atts['standard_name'] = 'atmosphere_hybrid_sigma_ln_pressure_coordinate'
              else:
                name = 'eta'
                atts['standard_name'] = 'atmosphere_hybrid_sigma_pressure_coordinate'
              # Add all parameters for this coordinate.
              internal_atts = OrderedDict()
              for key in VGD_KEYS:
                try:
                  val = vgd_get(vgd_id,key)
                  # Skip multidimensional arrays (can't be encoded as metadata).
                  if getattr(val,'ndim',1) > 1: continue
                  internal_atts[key] = val
                except (KeyError,VGDError):
                  pass  # Some keys not available in some vgrids?
              # Put this information in the final output file?
              if not self._minimal_metadata:
                atts.update(internal_atts)
              # Attempt to fill in A/B ancillary data (if available).
              try:
                all_z = list(internal_atts['VCDM'])+list(internal_atts['VCDT'])
                all_a = list(internal_atts['CA_M'])+list(internal_atts['CA_T'])
                all_b = list(internal_atts['CB_M'])+list(internal_atts['CB_T'])
                A = []
                B = []
                for z in levels:
                  ind = all_z.index(z)
                  A.append(all_a[ind])
                  B.append(all_b[ind])
                A = type(var)(name+'_A', {}, {name:levels}, np.asarray(A))
                B = type(var)(name+'_B', {}, {name:levels}, np.asarray(B))
                ancillary_variables.extend([A,B])
              except (KeyError,ValueError,VGDError):
                warn (_("Unable to get A/B coefficients."))
              vgd_free (vgd_id)
            # Not a '!!' coordinate, so must be 'HY'?
            else:
              name = 'eta'
              atts['standard_name'] = 'atmosphere_hybrid_sigma_pressure_coordinate'
              # Get A and B info.
              eta = np.asarray(levels)
              ptop = DecodeIp(header['ip1'],0,0)[0].v1
              # Conversion taken from 'ig_to_hybref' function in librmn:
              pref = float(header['ig1'])
              rcoef = header['ig2']/1000.0
              # Apply the formula to compue A & B (from old fstd_core.c code):
              etatop = ptop/pref
              B = ((eta - etatop) / (1 - etatop)) ** rcoef
              A = pref * 100. * (eta - B)
              B = type(var)(name+'_B', {}, {name:levels}, B)
              A = type(var)(name+'_A', {}, {name:levels}, A)
              ancillary_variables.extend([A,B])
              # Add extra HY record metadata.
              atts.update(ptop=ptop, rcoef=rcoef, pref=pref)
        elif kind == 6:
          # theta [th]
          name = 'theta'
          atts['standard_name'] = 'air_potential_temperature'
          atts['units'] = 'K'
          atts['positive'] = 'up'

        # Add this vertical axis.
        axes = OrderedDict([(name,levels)])
        if len(ancillary_variables) > 0:
          atts['ancillary_variables'] = ' '.join(v.name for v in ancillary_variables)
        array = np.asarray(levels)
        vaxes[(levels,kind)] = type(var)(name,atts,axes,array)
        yield vaxes[(levels,kind)]
        # Add any ancillary data needed for the axis.
        for anc in ancillary_variables:
          yield anc
      # Get the vertical axis.
      vaxis = vaxes[(levels,kind)]
      # Modify the variable's dimension name to match the axis name.
      axes = OrderedDict(((vaxis.name if n == 'level' else n),v) for n,v in var.axes.items())
      var = type(var)(var.name,var.atts,axes,var.array)
      yield var


#################################################
# Logic for handling lat/lon coordinates.

class _XYCoords (_Buffer_Base):
  _xycoord_nomvars = ('^^','>>')
  def __init__ (self, *args, **kwargs):
    # Tell the decoder not to process horizontal records as variables.
    self._meta_records = self._meta_records + self._xycoord_nomvars
    super(_XYCoords,self).__init__(*args,**kwargs)
    # Variables must have an internally consistent horizontal grid.
    self._var_id = self._var_id + ('grtyp',)
    self._human_var_id = self._human_var_id + ('%(grtyp)s',)
    # Also, must have consistent igX records for a variable.
    if 'ig1' not in self._var_id:
      self._var_id = self._var_id + ('ig1','ig2','ig3','ig4')
      self._human_var_id = self._human_var_id + ('grid_%(ig1)s_%(ig2)s_%(ig3)s_%(ig4)s',)
  # Add horizontal coordinate info to the data stream.
  def __iter__ (self):
    from collections import OrderedDict
    from rpnpy.librmn.interp import ezqkdef, ezgdef_fmem, gdll, EzscintError
    import numpy as np

    # Scan through the data, and look for any use of horizontal coordinates.
    latlon = OrderedDict()
    for var in super(_XYCoords,self).__iter__():
      # Don't touch variables that have no horizontal extent.
      if 'i' not in var.axes or 'j' not in var.axes:
        yield var
        continue
      # Check if we already defined this grid.
      # First, construct a key identifying the grid.
      key = var.atts['grtyp']
      # Special case for timeseries data:
      # Ignore grtyp, since e.g. grtyp='Y' and grtyp='+' both use same grids.
      # See _Series mixin for more info about timeseries data.
      if var.atts.get('typvar') == 'T': key = 'T'
      key = (key,) + tuple(var.atts[n] for n in ('ni','nj','ig1','ig2','ig3','ig4'))
      if key not in latlon:
        # Get basic information about this grid.
        gridinfo = OrderedDict()
        for n in ('ni','nj','grtyp','ig1','ig2','ig3','ig4'):
          v = var.atts[n]
          if isinstance(v,str):
            gridinfo[n] = v
          else:
            gridinfo[n] = int(v)  # ezgdef_fmem is very picky about types.
        # Remember the associated '>>','^^' metadata for later.
        xatts = OrderedDict([('axis','X')])
        yatts = OrderedDict([('axis','Y')])
        # Check for reference grid data.
        for header in self._params:
          nomvar = header['nomvar'].strip()
          if nomvar not in self._xycoord_nomvars: continue
          k1 = (header['ip1'],header['ip2'],header['ip3'])
          k2 = (var.atts['ig1'],var.atts['ig2'],var.atts['ig3'])
          if k1 == k2:
            gridinfo['grref'] = header['grtyp'].strip()
            gridinfo['ig1'] = int(header['ig1'])
            gridinfo['ig2'] = int(header['ig2'])
            gridinfo['ig3'] = int(header['ig3'])
            gridinfo['ig4'] = int(header['ig4'])
            if nomvar == '>>':
              # Need to reduce out 'nk' dimension, or ezgdef_fmem aborts
              # on 'Y' grid.
              gridinfo['ax'] = header['d'][...].squeeze(axis=2)
              xatts.update(self._get_header_atts(header))
            if nomvar == '^^':
              gridinfo['ay'] = header['d'][...].squeeze(axis=2)
              yatts.update(self._get_header_atts(header))
        try:
          # Get the lat & lon data.
          if gridinfo['grtyp'] in ('A','B','E','G','L','N','S'):
            #TODO: free this grid after use?
            gdid = ezqkdef (**gridinfo)
            ll = gdll(gdid)
          # Timeseries data already has lat/lon info, nothing to decode?
          # (see _Series mixin).
          # ezgdef_fmem doesn't seem to handle this grid type (get garbage)
          # so get it directly here (assuming ^^ and >> are already lat/lon).
          elif gridinfo.get('grref') == 'T':
            ll = dict(lat=gridinfo['ay'],lon=gridinfo['ax'])
          #TODO: add 'X' grid support to rpnpy.librmn.interp.ezgdef_fmem?
          elif gridinfo.get('grtyp') == 'X' and gridinfo.get('grref') == 'L':
            ll = dict(lat=gridinfo['ay'],lon=gridinfo['ax'])
          # Fall back to more general grid routine?
          else:
            gdid = ezgdef_fmem (**gridinfo)
            ll = gdll(gdid)
        except (TypeError,EzscintError):
          warn(_("Unable to get grid info for '%s'")%var.name)
          yield var
          continue
        latarray = ll['lat'].transpose() # Switch from Fortran to C order.
        latatts = OrderedDict()
        latatts['long_name'] = 'latitude'
        latatts['standard_name'] = 'latitude'
        latatts['units'] = 'degrees_north'
        lonarray = ll['lon'].transpose() # Switch from Fortran to C order.
        lonatts = OrderedDict()
        lonatts['long_name'] = 'longitude'
        lonatts['standard_name'] = 'longitude'
        lonatts['units'] = 'degrees_east'
        # Start with generic (i,j) axes for lat/lon data.
        lataxes = lonaxes = OrderedDict([('j',var.axes['j']),('i',var.axes['i'])])
        # Do we have a non-trivial structured 2D field?
        # If so, use the appropriate (x,y) coordinate system.
        if 'ax' in gridinfo and 'ay' in gridinfo and latarray.shape[0] > 1 and lonarray.shape[0] > 1:
          # Only do this for 1D ax and ay parameters!
          if gridinfo['ax'].shape[0] == 1 and gridinfo['ay'].shape[0] == 1:
            lataxes = lonaxes = OrderedDict([('y',tuple(gridinfo['ay'].flatten())),('x',tuple(gridinfo['ax'].flatten()))])
        # Try to resolve lat/lon to 1D Cartesian coordinates, if possible.
        # Calculate the mean lat/lon arrays in double precision.
        if latarray.shape[1] > 1 and lonarray.shape[1] > 1:
          meanlat = np.mean(np.array(latarray,dtype=float),axis=1,keepdims=True)
          meanlon = np.mean(np.array(lonarray,dtype=float),axis=0,keepdims=True)
          if np.allclose(latarray,meanlat) and np.allclose(lonarray,meanlon):
            # Reduce back to single precision for writing out.
            meanlat = np.array(meanlat,dtype=latarray.dtype).squeeze()
            meanlon = np.array(meanlon,dtype=lonarray.dtype).squeeze()
            # Ensure monotonicity of longitude field.
            # (gdll may sometimes wrap last longitude to zero).
            # Taken from old fstd_core.c code.
            if meanlon[-2] > meanlon[-3] and meanlon[-1] < meanlon[-2]:
              meanlon[-1] += 360.
            lataxes = OrderedDict([('lat',tuple(meanlat))])
            lonaxes = OrderedDict([('lon',tuple(meanlon))])
            latarray = meanlat
            lonarray = meanlon
        # Detect 1D unstructured lat/lon, and remove degenerate dimension.
        if latarray.shape[0] == 1 and lonarray.shape[0] == 1:
          lataxes = OrderedDict(list(lataxes.items())[1:])
          lonaxes = OrderedDict(list(lonaxes.items())[1:])
          latarray = latarray.flatten()
          lonarray = lonarray.flatten()
        # For non-cartesian (but structured) 2D grids, add x and y coordinates.
        if 'x' in lonaxes and 'y' in lataxes:
          yield type(var)('x',xatts,{'x':lonaxes['x']},np.array(lonaxes['x']))
          yield type(var)('y',yatts,{'y':lataxes['y']},np.array(lataxes['y']))
        # Otherwise, assume '^^' / '>>' correspond to lat/lon, so any metadata
        # can go into the lat and lon fields.
        else:
          latatts.update(yatts)
          lonatts.update(xatts)
        # Define lat/lon variables.
        lat = type(var)('lat',latatts,lataxes,latarray)
        lon = type(var)('lon',lonatts,lonaxes,lonarray)
        # Put the lat/lon variables in the data stream, before any dependent
        # data variables.
        yield lat
        yield lon
        latlon[key] = (lat,lon)
      lat,lon = latlon[key]
      # Update the var's horizontal coordinates.
      axes = OrderedDict()
      array = var.array
      for dim,(axisname,axisvalues) in enumerate(var.axes.items()):
        # Use appropriate x-dimension.
        if axisname == 'i':
          if 'lon' in lon.axes:
            axisname, axisvalues = 'lon', lon.axes['lon']
          elif 'x' in lon.axes:
            axisname, axisvalues = 'x', lon.axes['x']
        # Use appropriate y-dimension.
        elif axisname == 'j':
          if 'lat' in lat.axes:
            axisname, axisvalues = 'lat', lat.axes['lat']
          elif 'y' in lat.axes:
            axisname, axisvalues = 'y', lat.axes['y']
          # Do we have 1D unstructured lat/lon?
          elif len(axisvalues) == 1 and len(lat.axes) == 1:
            # Remove 2nd (degenerate) dimension from the variable.
            array = array.squeeze(axis=dim)
            continue
        axes[axisname] = axisvalues

      # For 2D lat/lon, add these to the metadata.
      if 'lat' not in axes or 'lon' not in axes:
        var.atts['coordinates'] = 'lon lat'

      yield type(var)(var.name,var.atts,axes,array)


#################################################
# Remove extraneous dimensions from the output.

class _NoNK (_Buffer_Base):
  def __iter__ (self):
    for var in super(_NoNK,self).__iter__():
      axes = var.axes
      array = var.array
      if 'k' in axes and len(axes['k']) == 1:
        array = array.squeeze(axis=list(axes.keys()).index('k'))
        del axes['k']
      yield type(var)(var.name,var.atts,axes,array)


#################################################
# Add netCDF metadata to the variables

class _netCDF_Atts (_Buffer_Base):
  @classmethod
  def _cmdline_args (cls, parser):
    import argparse
    super(_netCDF_Atts,cls)._cmdline_args(parser)
    parser.add_argument('--metadata-file', type=argparse.FileType('r'), action='append', help=_('Apply netCDF metadata from the specified file.  You can repeat this option multiple times to build metadata from different sources.'))
  def __init__ (self, metadata_file=None, *args, **kwargs):
    import ConfigParser
    from collections import OrderedDict
    if metadata_file is None:
      metafiles = []
    else:
      metafiles = metadata_file
    metadata = OrderedDict()
    configparser = ConfigParser.SafeConfigParser()
    for metafile in metafiles:
      configparser.readfp(metafile)
    for varname in configparser.sections():
      metadata[varname] = OrderedDict(configparser.items(varname))
    self._metadata = metadata
    super(_netCDF_Atts,self).__init__(*args,**kwargs)
  def __iter__ (self):
    from collections import OrderedDict

    axis_renames = {}

    for var in super(_netCDF_Atts,self).__iter__():
      name = var.name
      atts = OrderedDict(var.atts)
      # Add extra metadata provided by the user?
      if var.name in self._metadata:
        atts.update(self._metadata[var.name])
        # Rename the field? (Using special 'rename' key in the metadata file).
        if 'rename' in atts:
          name = atts.pop('rename')
          # Also rename any axis with this name.
          axis_renames[var.name] = name

      # Check if any of the axes in this variable need to be renamed.
      axis_names, axis_values = zip(*var.axes.items())
      axis_names = [axis_renames.get(n,n) for n in axis_names]
      axes = OrderedDict(zip(axis_names,axis_values))

      yield type(var)(name,atts,axes,var.array)


#################################################
# Logic for reading/writing FSTD data from/to netCDF files.

class _netCDF_IO (_netCDF_Atts):
  @classmethod
  def _cmdline_args (cls, parser):
    super(_netCDF_IO,cls)._cmdline_args(parser)
    parser.add_argument('--time-units', choices=['seconds','minutes','hours','days'], default='hours', help=_('The units of time for the netCDF file.  Default is %(default)s.'))
    parser.add_argument('--reference-date', metavar=_('YYYY-MM-DD'), help=_('The reference date for the netCDF time axis.  The default is the starting date in the file.'))
    parser.add_argument('--buffer-size', type=int, default=100, help=_('How much data to write at a time (in MBytes).  Default is %(default)s.'))

  @classmethod
  def _check_args (cls, parser, args):
    from datetime import datetime
    super(_netCDF_IO,cls)._check_args(parser,args)
    # Parse the reference date into a datetime object.
    if args.reference_date is not None:
      try:
        datetime.strptime(args.reference_date,'%Y-%m-%d')
      except ValueError:
        parser.error(_("Unable to to parse the reference date '%s'.  Expected format is '%s'")%(args.reference_date,_('YYYY-MM-DD')))

  def __init__ (self, time_units='hours', reference_date=None, buffer_size=100, *args, **kwargs):
    self._time_units = time_units
    self._reference_date = reference_date
    self._buffer_size = int(buffer_size)
    super(_netCDF_IO,self).__init__(*args,**kwargs)

  def __iter__ (self):
    from datetime import datetime
    import numpy as np
    from netCDF4 import date2num

    if self._reference_date is None:
      reference_date = None
    else:
      reference_date = datetime.strptime(self._reference_date,'%Y-%m-%d')

    for var in super(_netCDF_IO,self).__iter__():

      # Modify time axes to be relative units instead of datetime objects.
      if var.name in var.axes and isinstance(var.array[0],datetime):
        units = '%s since %s'%(self._time_units, reference_date or var.array[0])
        var.atts.update(units=units)
        array = np.asarray(date2num(var.array,units=units))
        var = type(var)(var.name,var.atts,var.axes,array)

      yield var


  def write_nc_file (self, filename, global_metadata=None):
    """
    Write the records to a netCDF file.
    Requires the netCDF4 package.
    """
    from netCDF4 import Dataset
    import numpy as np
    from itertools import product
    from collections import OrderedDict
    f = Dataset(filename, "w", format="NETCDF4")

    # List of metadata keys that are internal to the FSTD file.
    internal_meta = list(self._vectorize_params().keys())

    # Apply global metadata (from config files and global_metadata argument).
    if 'global' in self._metadata:
      f.setncatts(self._metadata['global'])
    if global_metadata is not None:
      f.setncatts(global_metadata)

    # Need to pre-scan all the variables to generate unique names.
    varlist = list(iter(self))

    # Generate unique axis names.
    axis_table = dict()
    for varname, atts, axes, array in varlist:
      for axisname, axisvalues in axes.items():
        axisvalues = tuple(axisvalues)
        if axisname not in axis_table:
          axis_table[axisname] = []
        if axisvalues not in axis_table[axisname]:
          axis_table[axisname].append(axisvalues)
    axis_renames = dict()
    for axisname, axisvalues_list in axis_table.items():
      if len(axisvalues_list) == 1: continue
      warn (_("Multiple %s axes.  Appending integer suffixes to their names.")%axisname)
      for i,axisvalues in enumerate(axisvalues_list):
        axis_renames[(axisname,axisvalues)] = axisname+str(i+1)

    # Apply axis renames.
    def rename_axis ((axisname,axisvalues)):
      key = (axisname,tuple(axisvalues))
      if key in axis_renames:
        return (axis_renames[key],axisvalues)
      return (axisname,axisvalues)
    for i, var in enumerate(varlist):
      varname = var.name
      # If this is a coordinate variable, use same renaming rules as the
      # dimension name.
      if varname in var.axes:
        varname, axisvalues = rename_axis((varname,var.axes[varname]))
      axes = OrderedDict(map(rename_axis,var.axes.items()))
      varlist[i] = _var_type(varname, var.atts, axes, var.array)

    # Generate a string-based variable id.
    # Only works for true variables from the FSTD source
    # (needs metadata like etiket, etc.)
    def get_var_id (var):
      out = []
      for fmt in self._human_var_id:
        out.append(fmt%var.atts)
      return tuple(out)

    # Generate unique variable names.
    var_table = dict()
    for i, var in enumerate(varlist):
      if var.name not in var_table:
        var_table[var.name] = []
      # Identify the variables by their index in the master list.
      var_table[var.name].append(i)
    for varname, var_indices in var_table.items():
      # Only need to rename variables that are non-unique.
      if len(var_indices) == 1: continue
      try:
        var_ids = [get_var_id(varlist[i]) for i in var_indices]
      except KeyError:
        # Some derived axes may not have enough metadata to generate an id,
        # so the best we can do is append an integer suffix.
        var_ids = [(str(r),) for r in range(1,len(var_indices)+1)]

      var_ids = zip(*var_ids)

      # Omit parts of the var_id that are invariant over all the variables.
      var_ids = [var_id for var_id in var_ids if len(set(var_id)) > 1]
      # Starting from the rightmost key, remove as many keys as possible while
      # maintaining uniqueness.
      for j in reversed(range(len(var_ids))):
        test = var_ids[:j] + var_ids[j+1:]
        if len(set(zip(*test))) == len(var_indices):
          var_ids = var_ids[:j] + var_ids[j+1:]

      var_ids = zip(*var_ids)

      var_ids = ['_'.join(var_id) for var_id in var_ids]

      warn (_("Multiple definitions of %s.  Adding unique suffixes %s.")%(varname, ', '.join(var_ids)))

      # Apply the name changes.
      for i, var_id in zip(var_indices, var_ids):
        varname, atts, axes, array = varlist[i]
        newname = varname + '_' + var_id
        varlist[i] = _var_type(newname,atts,axes,array)
        # Apply the name changes to any metadata that references this variable.
        for var in varlist:
          # Must match axes.
          if not set(axes.keys()) <= set(var.axes.keys()): continue
          for key,val in list(var.atts.items()):
            if not isinstance(val,str): continue
            val = val.split()
            if varname in val:
              val[val.index(varname)] = newname
            var.atts[key] = ' '.join(val)

    #TODO: Make sure names don't start with a digit?
    # However, this seems to work okay through this interface.

    for varname, atts, axes, array in varlist:
      for axisname, axisvalues in axes.items():
        # Only need to create each dimension once (even if it's in multiple
        # variables).
        if axisname not in f.dimensions:
          f.createDimension(axisname, len(axisvalues))
      # Write the variable.
      v = f.createVariable(varname, datatype=array.dtype, dimensions=list(axes.keys()))
      # Write the metadata.
      # Strip out FSTD-specific metadata?
      if self._minimal_metadata:
        for n in internal_meta:
          atts.pop(n,None)
      v.setncatts(atts)
      # Determine how much we can write at a time.
      # Try to keep it under the buffer size, but make sure the last 2
      # dimensions don't get split (represent a single FSTD record?)
      a = 0
      check = array.size * array.dtype.itemsize
      while check > self._buffer_size*1E6 and a < array.ndim-2:
        check /= array.shape[a]
        a = a + 1
      for ind in product(*map(range,array.shape[:a])):
        try:
          v[ind] = np.asarray(array[ind])
        except (IndexError,ValueError):
          warn(_("Internal problem with the script - unable to get data for '%s'")%varname)
          continue
    # We need to explicitly state that we're using CF conventions in our
    # output files, or some utilities (like IDV) won't accept the data.
    f.Conventions = "CF-1.6"

    f.close()


# Default interface for I/O.
class Buffer (_netCDF_IO,_NoNK,_XYCoords,_VCoords,_Series,_Dates,_Masks,_SelectVars):
  """
  High-level interface for FSTD data, to treat it as multi-dimensional arrays.
  Contains logic for dealing with most of the common FSTD file conventions.
  """


# Command-line invocation:
def _fstd2nc_cmdline (buffer_type=Buffer):
  from argparse import ArgumentParser
  from sys import stdout, exit, argv
  from os.path import exists
  parser = ArgumentParser(description=_("Converts an RPN standard file (FSTD) to netCDF format."))
  parser.add_argument('infile', nargs='+', metavar='<fstd_file>', help=_('The FSTD file(s) to convert.'))
  parser.add_argument('outfile', metavar='<netcdf_file>', help=_('The name of the netCDF file to create.'))
  buffer_type._cmdline_args(parser)
  parser.add_argument('--no-history', action='store_true', help=_("Don't put the command-line invocation in the netCDF metadata."))
  args = parser.parse_args()
  buffer_type._check_args(parser, args)
  args = vars(args)
  infiles = args.pop('infile')
  outfile = args.pop('outfile')
  no_history = args.pop('no_history')
  buf = buffer_type(**args)

  # Make sure input file exists
  for infile in infiles:
    if not exists(infile):
      print (_("Error: '%s' does not exist!")%(infile))
      exit(1)

    buf.read_fstd_file(infile)

  # Check if output file already exists
  if exists(outfile):
    overwrite = False
    if stdout.isatty():
      while True:
        print (_("Warning: '%s' already exists!  Overwrite? (y/n):")%(outfile)),
        try: ans = raw_input()
        except NameError: ans = input()
        if ans.lower() in ('y','yes','o','oui'):
          overwrite = True
          break
        if ans.lower() in ('n','no','non'):
          overwrite = False
          break
        print (_("Sorry, invalid response."))
    if overwrite is False:
      print (_("Refusing to overwrite existing file '%s'.")%(outfile))
      exit(1)

  # Append the command invocation to the netCDF metadata?
  if no_history:
    global_metadata = None
  else:
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    command = list(argv)
    # Any arguments with spaces should be surrounded by quotes.
    for i,c in enumerate(command):
      if " " in c:
        command[i] = "'"+c+"'"
    command = " ".join(command)
    history = timestamp + ": " + command
    global_metadata = {"history":history}

  buf.write_nc_file(outfile, global_metadata)

# Command-line invocation with error trapping.
# Hides the Python stack trace when the user aborts the command.
def _fstd2nc_cmdline_trapped (*args, **kwargs):
  try:
    _fstd2nc_cmdline ()
  except KeyboardInterrupt:
    print (_("Aborted by user."))
    exit(1)


if __name__ == '__main__':
  _fstd2nc_cmdline_trapped()

