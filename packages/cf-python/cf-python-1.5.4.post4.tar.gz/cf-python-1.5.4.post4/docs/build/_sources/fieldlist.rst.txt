.. currentmodule:: cf
.. default-role:: obj

.. _fs_field_list:

Introduction to the `cf.FieldList` object
=========================================

A `cf.FieldList` object is an ordered sequence of `cf.Field` objects.

It supports nearly all of the :ref:`python list-like operations
<python:typesseq-mutable>`, the exceptions being the arithmetic and
comparison operators for which it has :ref:`its own definitions
<fs-fl-a-and-c>`. For example:

>>> fl
[<CF Field: x_wind(grid_latitude(110), grid_longitude(106)) m s-1>,
 <CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>]
>>> fl[0]
<CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>
>>> fl[::-1] 
[<CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>,
 <CF Field: x_wind(grid_latitude(110), grid_longitude(106)) m s-1>]
>>> fl[slice(1, -1, 2)]
[<CF Field: x_wind(grid_latitude(110), grid_longitude(106)) m s-1>]

Note that an indexing by an integer returns an individual field, but
other types of index always return a field list.

>>> len(fl)
2
>>> f = fl.pop()
>>> f
<CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>
>>> len(fl)
1
>>> fl.append(f)
>>> len(fl)
2
>>> f in fl
True
>>> from operator import attrgetter
>>> fl
[<CF Field: x_wind(grid_latitude(110), grid_longitude(106)) m s-1>,
 <CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>]
>>> fl.sort(key=attrgetter('standard_name'))
[<CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>,
 <CF Field: x_wind(grid_latitude(110), grid_longitude(106)) m s-1>]

Selecting fields
^^^^^^^^^^^^^^^^

One or more fields from a field list may be selected with the
`~cf.FieldList.select` method. This returns a single field or a new
field list, depending on how many fields are selected. For example.

>>> fl
[<CF Field: x_wind(grid_latitude(110), grid_longitude(106)) m s-1>,
 <CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>]
>>> fl.select('air_temperature')
<CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>]
>>> fl.select('[air_temperature|x_wind]')
[<CF Field: x_wind(grid_latitude(110), grid_longitude(106)) m s-1>,
 <CF Field: air_temperature(time(12), latitude(73), longitude(96)) K>]
 
Using field methods
^^^^^^^^^^^^^^^^^^^

A subset of a field's callable methods are also available to a field
list object (see the list of :ref:`field list methods
<fieldlist_methods>`). In general, these are methods which, on a
field, return a field or `None`. These methods are applied to each
constituent field independently, so


>>> gl = fl.max()
>>> fl.max(i=True)

is exactly equivalent to

>>> gl = cf.FieldList([f.max() for f in fl])
>>> for f in fl:
...     f.max(i=True)

.. _fs-fl-a-and-c:

Arithmetic and comparison
^^^^^^^^^^^^^^^^^^^^^^^^^

All of the :ref:`operators defined for a field
<Arithmetic-and-comparison>` are also allowed for field list, the
operation applying to each field independently. For example the
commands:

>>> gl = fl + 2
>>> gl = 2 // fl
>>> gl = fl == 0
>>> fl += 2

are exactly equivalent to:

>>> gl = cf.FieldList(f + 2 for f in fl)
>>> gl = cf.FieldList(2 // f for f in fl)
>>> gl = cf.FieldList(f == 0 for f in fl)
>>> for f in fl:
...     f += 2

