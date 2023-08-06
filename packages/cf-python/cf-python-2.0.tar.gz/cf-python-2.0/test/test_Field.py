import datetime
import inspect
import os
import unittest

import numpy

import cf

class FieldTest(unittest.TestCase):
    def setUp(self):
        self.filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     'test_file.nc')
        self.filename2 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'test_file2.nc')
        self.chunk_sizes = (17, 34, 300, 100000)[::-1]
        self.original_chunksize = cf.CHUNKSIZE()
        self.f = cf.read1(self.filename)

        self.test_only = []
#        self.test_only = ['test_Field___add__']
        self.test_only = ['test_Field_collapse']
#        self.test_only = ['test_Field_transpose','test_Field_squeeze']
#        self.test_only = ['test_Field_match','test_Field_items']
#        self.test_only = ['test_Field_items']
#        self.test_only = ['test_Field_axes','test_Field_data_axes']
#        self.test_only = ['test_Field_where']
#        self.test_only = ['test_Field_anchor']
#        self.test_only = ['test_Field_period']
#        self.test_only = ['test_Field_mask_invalid']
#        self.test_only = ['test_Field___setitem__']
#        self.test_only = ['test_Field_section']

    def test_Field___setitem__(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        for chunksize in self.chunk_sizes:            
            f = cf.read1(self.filename).squeeze()

            f[...] = 0
            self.assertTrue((f == 0).all())
            f[3:7, 2:5] = -1
            self.assertTrue((f.array[3:7, 2:5] == -1).all())
            f[6:2:-1, 4:1:-1] = numpy.array(-1)
            self.assertTrue((f.array[6:2:-1, 4:1:-1] == -1).all())
            f[[0, 3, 8], [1, 7, 8]] = numpy.array([[[[-2]]]])
            self.assertTrue((f[[0, 3, 8], [1, 7, 8]].array == -2).all())
            f[[8, 3, 0], [8, 7, 1]] = cf.Data(-3, None)
            self.assertTrue((f[[8, 3, 0], [8, 7, 1]].array == -3).all())
            f[[7, 4, 1], slice(6, 8)] = [-4]
            self.assertTrue((f[[7, 4, 1], slice(6, 8)].array == -4).all())
        #--- End: for    
        cf.CHUNKSIZE(self.original_chunksize)
    #--- End: def

    def test_Field___add__(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        for chunksize in self.chunk_sizes:            
            f = cf.read1(self.filename).squeeze()
            g = f.copy()
            f_plus_g = f + g
            g_plus_f = g + f
#            self.assertTrue((f_plus_g).equals(g_plus_f, traceback=True),
#                            'f\n{}\nf.copy()\n{}\nf+f.copy()\n{}\nf.copy()+f\n{}'.format(
#                                str(f), str(g), str(f_plus_g), str(g_plus_f)))

            g = f[0]
            f_plus_g = f + g
            g_plus_f = g + f
#            self.assertTrue((f_plus_g).equals(g_plus_f, traceback=True),
#                            'f\n{}\nf[0]\n{}\nf+f[0]\n{}\nf[0]+f\n{}'.format(
#                                str(f), str(g), str(f_plus_g), str(g_plus_f)))
        #--- End: for    
        cf.CHUNKSIZE(self.original_chunksize)
    #--- End: def

    def test_Field_anchor(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        dimarray = self.f.dim('grid_lon').array
      
        for chunksize in self.chunk_sizes:            
            f = cf.read1(self.filename)

            for period in (dimarray.min()-5, dimarray.min()):
                anchors = numpy.arange(dimarray.min()-3*period,
                                       dimarray.max()+3*period, 0.5)

                f.cyclic('grid_lon', period=period)

                # Increasing dimension coordinate    
                for anchor in anchors:
                    g = f.anchor('grid_lon', anchor)
                    x0 = g.coord('grid_lon').datum(-1) - period
                    x1 = g.coord('grid_lon').datum(0)
                    self.assertTrue(
                        x0 < anchor <= x1,
                        'INCREASING period=%s, x0=%s, anchor=%s, x1=%s' % \
                        (period, x0, anchor, x1))
                #--- End: for

                # Decreasing dimension coordinate    
                flipped_f = f.flip('grid_lon')
                for anchor in anchors:
                    g = flipped_f.anchor('grid_lon', anchor)
                    x1 = g.coord('grid_lon').datum(-1) + period
                    x0 = g.coord('grid_lon').datum(0)
                    self.assertTrue(
                        x1 > anchor >= x0,
                        'DECREASING period=%s, x0=%s, anchor=%s, x1=%s' % \
                        (period, x1, anchor, x0))
                #--- End: for
            #--- End: for
        #--- End: for    
        cf.CHUNKSIZE(self.original_chunksize)
    #--- End: def

    def test_Field_axes(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        f = self.f
        self.assertTrue(f.axes() == {'dim0':1, 'dim1':10, 'dim2':9})

        for i in range(f.ndim):
            self.assertTrue(f.axis(i) == f.data_axes()[i])

        self.assertTrue(set(f.axes(slice(0,3))) == set(f.data_axes()))

        for k, v in f.ncdimensions.iteritems():
            self.assertTrue(f.axis('ncdim%' + v) == k)
    #--- End: def

    def test_Field_data_axes(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        self.assertTrue(self.f.copy().data_axes() == ['dim0', 'dim1', 'dim2'])
        f = cf.Field(data=cf.Data(9))
        self.assertTrue(f.data_axes() == [])
        del f.Data
        self.assertTrue(f.data_axes() == None)
    #--- End: def

    def test_Field_equals(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        for chunksize in self.chunk_sizes:    
            cf.CHUNKSIZE(chunksize)
            f = cf.read1(self.filename)
            g = f.copy()
            self.assertTrue(f.equals(g, traceback=True))
            self.assertFalse(f.equals(g+1, traceback=False))
        #--- End: for    
        cf.CHUNKSIZE(self.original_chunksize)
    #--- End: def

#    def test_Field_indices(self):
#        if self.test_only and inspect.stack()[0][3] not in self.test_only:
#            return
#
#        for chunksize in self.chunk_sizes:            
#            f = cf.read(self.filename)[0]
#            
#            
#
#        cf.CHUNKSIZE(self.original_chunksize)
#    #--- End: def

    def test_Field_items(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        f = cf.read1(self.filename)

        self.assertTrue(len(f.Items()) == 16)
        self.assertTrue(len(f.Items(role='damr')) == 9)

        self.assertTrue(len(f.items()) == 14)
        self.assertTrue(len(f.items(inverse=True)) == 0)

        self.assertTrue(len(f.items(ndim=1)) == 8)
        self.assertTrue(len(f.items(ndim=1, inverse=True)) == 6)

        self.assertTrue(len(f.items(ndim=2)) == 6)
        self.assertTrue(len(f.items(ndim=2, inverse=True)) == 8)

        self.assertTrue(len(f.items(ndim=cf.ge(3))) == 0)
        self.assertTrue(len(f.items(ndim=cf.ge(3), inverse=True)) == 14)

        self.assertTrue(len(f.items(ndim=cf.gt(3))) == 0)
        self.assertTrue(len(f.items(ndim=cf.gt(3), inverse=True)) == 14)

        self.assertTrue(len(f.items(role='d')) == 3)
        self.assertTrue(len(f.items(role='da')) == 6)
        self.assertTrue(len(f.items(role='dam')) == 7)

        self.assertTrue(len(f.items(axes='Y')) == 9)
        self.assertTrue(len(f.items(axes='Y', inverse=True)) == 5)

        self.assertTrue(len(f.items(axes='Z')) == 3)
        self.assertTrue(len(f.items(axes='Z', inverse=True)) == 11)
        
        self.assertTrue(len(f.items('X')) == 1)
        self.assertTrue(len(f.items('Y')) == 1)
        self.assertTrue(len(f.items('Z')) == 1)
        self.assertTrue(len(f.items('X', inverse=True)) == 13)
        self.assertTrue(len(f.items('Y', inverse=True)) == 13)
        self.assertTrue(len(f.items('Z', inverse=True)) == 13)
        self.assertTrue(len(f.items(['X', 'Y', {'standard_name': 'longitude', 'units': 'radians'}])) == 3)
        self.assertTrue(len(f.items(['X', 'Y', {'standard_name': 'longitude', 'units': 'K'}])) == 2)

        self.assertTrue(len(f.items(ndim=2)) == 6)
        self.assertTrue(len(f.items(axes='X', ndim=2)) == 6)

        self.assertTrue(len(f.items(axes='X', ndim=2, match_and=False)) == 8)

        self.assertTrue(len(f.items('longitude', axes='X', ndim=2)) == 1)
        self.assertTrue(len(f.items('grid_longitude', axes='X', ndim=2)) == 0)
        self.assertTrue(len(f.items('grid_longitude', axes='X', ndim=2, match_and=False)) == 8)

        self.assertTrue(len(f.items('atmosphere_hybrid_height_coordinate')) == 1)

        self.assertTrue(len(f.items(axes='X')) == 8)
        self.assertTrue(len(f.items(axes='Y')) == 9)
        self.assertTrue(len(f.items(axes='Z')) == 3)

        self.assertTrue(len(f.items(axes=['X','Y'])) == 11)
        self.assertTrue(len(f.items(axes=['X','Z'])) == 11)
        self.assertTrue(len(f.items(axes=['Z','Y'])) == 12)

        self.assertTrue(len(f.items(axes_all='X')) == 2)
        self.assertTrue(len(f.items(axes_all='Y')) == 3)
        self.assertTrue(len(f.items(axes_all='Z')) == 3)
        self.assertTrue(len(f.items(axes_all=['X','Y'])) == 6)
        self.assertTrue(len(f.items(axes_all=['X','Z'])) == 0)
        self.assertTrue(len(f.items(axes_all=['Z','Y'])) == 0)

        self.assertTrue(len(f.items(axes_subset='X')) == 8)
        self.assertTrue(len(f.items(axes_subset='Y')) == 9)
        self.assertTrue(len(f.items(axes_subset='Z')) == 3)
        self.assertTrue(len(f.items(axes_subset=['X','Y'])) == 6)
        self.assertTrue(len(f.items(axes_subset=['X','Z'])) == 0)
        self.assertTrue(len(f.items(axes_subset=['Z','Y'])) == 0)

        self.assertTrue(len(f.items(axes_superset='X')) == 2)
        self.assertTrue(len(f.items(axes_superset='Y')) == 3)
        self.assertTrue(len(f.items(axes_superset='Z')) == 3)

        self.assertTrue(len(f.items(axes_superset=['X','Y'])) == 11)
        self.assertTrue(len(f.items(axes_superset=['X','Z'])) == 5)
        self.assertTrue(len(f.items(axes_superset=['Z','Y'])) == 6)
    #--- End: def

    def test_Field_match(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        f = cf.read1(self.filename)
        f.long_name = 'qwerty'
        f.ncvar = 'tas'
        all_kwargs = (
            {'inverse': False},
            {'inverse': False, 'select': None},
            {'inverse': False, 'select': {}},
            {'inverse': False, 'select': []},
            {'inverse': False, 'select': [None]},
            {'inverse': False, 'select': [{}]},
            {'inverse': False, 'select': [None, {}]},
            {'inverse': False, 'select':  'eastward_wind'},
            {'inverse': False, 'select':  'eastward_wind', 'exact': True},
            {'inverse': False, 'select':  'eastward_'},
            {'inverse': False, 'select':  'e.*_wind$'},
            {'inverse': False, 'select':  'standard_name:eastward_wind'},
            {'inverse': False, 'select':  'standard_name:eastward_wind', 'exact': True},
            {'inverse': False, 'select':  'standard_name:eastward_'},
            {'inverse': False, 'select': {'standard_name': 'eastward_wind'}},
            {'inverse': False, 'select': {'standard_name': 'eastward_'}},
            {'inverse': False, 'select': cf.eq('.*_wind', exact=False)},
            {'inverse': False, 'select':  'long_name:qwerty'},
            {'inverse': False, 'select':  'long_name:qwerty', 'exact': True},
            {'inverse': False, 'select':  'long_name:qwe'},
            {'inverse': False, 'select': {'long_name': 'qwerty'}},
            {'inverse': False, 'select': {'long_name': 'qwe'}},
            {'inverse': False, 'select': {'long_name': cf.eq('qwerty')}},
            {'inverse': False, 'select': {'long_name': cf.eq('qwe', exact=False)}},
            {'inverse': False, 'select': 'ncvar%tas'},
            {'inverse': False, 'select': 'ncvar%tas', 'exact': True},
            {'inverse': False, 'select': 'ncvar%ta'},
            {'inverse': False, 'select': {None: 'ncvar%.*as$'}},
            {'inverse': False, 'select': {None: 'ncvar%tas$'}},
            {'inverse': False, 'select': {None: 'ncvar%tas'}},
            {'inverse': False, 'select': {None: 'ncvar%ta'}},
            #          
            {'inverse': False, 'select':  'eastward_wind', 'ndim': cf.wi(1, 3)},
            {'inverse': False, 'select':  'BBB', 'ndim': cf.wi(1, 3), 'match_and': False},
            {'inverse': False, 'select':  ['BBB', 'east'], 'ndim': cf.wi(1, 3), 'match_and': True},
            {'inverse': False, 'ndim': cf.wi(1, 3)},
        )
        for kwargs in all_kwargs:
            self.assertTrue(f.match(**kwargs), 
                            'f.match(**%s) failed' % kwargs)
            kwargs['inverse'] = not kwargs['inverse']
            self.assertFalse(f.match(**kwargs),
                             'f.match(**%s) failed' % kwargs)
        #--- End: for
    #--- End: def

    def test_Field_period(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        f = cf.read1(self.filename)
        f.dim('X').period(None)
        f.cyclic('X', False)
        self.assertTrue(f.period('X') is None)
        f.cyclic('X', period=360)
        self.assertTrue(f.period('X') == cf.Data(360, 'degrees'))
        f.cyclic('X', False)
        self.assertTrue(f.period('X') == cf.Data(360, 'degrees'))
        f.dim('X').period(None)
        self.assertTrue(f.period('X') is None)
    #--- End: def

    def test_Field_section(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        for chunksize in self.chunk_sizes:
            cf.CHUNKSIZE(chunksize)
            f = cf.read1(self.filename2)
            self.assertTrue(len(f.section(('X','Y'))) == 1800,
                            'CHUNKSIZE = %s' % chunksize)
        #--- End: for
        cf.CHUNKSIZE(self.original_chunksize)
    #--- End: def

    def test_Field_squeeze(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        f0 = cf.read(self.filename)

        for f in (f0[0], f0):
            f = f.copy()
            f.squeeze(i=True)
            g = f.copy()
            h = f.copy()
            i = h.squeeze(i=True)
            self.assertTrue(f.equals(g))
            self.assertTrue(h is i)
        #--- End: for    
    #--- End: def

    def test_Field_transpose(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        f = cf.read1(self.filename)

        # Null tranpose
        self.assertTrue(f is f.transpose([0, 1, 2], i=True))
        self.assertTrue(f.equals(f.transpose([0, 1, 2])))

        for chunksize in self.chunk_sizes:
            cf.CHUNKSIZE(chunksize)            
            f = cf.read(self.filename)[0]
            h = f.transpose((1, 2, 0))
            h0 = h.transpose(('atmos', 'grid_latitude', 'grid_longitude'))
            h.transpose((2, 0, 1), i=True)
            h.transpose(('grid_longitude', 'atmos', 'grid_latitude'), i=True)
            h.varray
            h.transpose(('atmos', 'grid_latitude', 'grid_longitude'), i=True)
            self.assertTrue(cf.equals(h, h0, traceback=True))
            self.assertTrue((h.array==f.array).all())
        #--- End: for    
        cf.CHUNKSIZE(self.original_chunksize)
    #--- End: def

    def test_Field_collapse(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        for chunksize in self.chunk_sizes:
            f = cf.read(self.filename2)[0]

            g = f.collapse('mean')
            self.assertTrue(g.cell_methods == cf.CellMethods('time: maximum time: latitude: longitude: mean').write(f.axes_names()))

            g = f.collapse('mean', axes=['T', 'X'])
            self.assertTrue(g.cell_methods == cf.CellMethods('time: maximum time: longitude: mean').write(f.axes_names()))

            g = f.collapse('mean', axes=[0, 2])
            self.assertTrue(g.cell_methods == cf.CellMethods('time: maximum time: longitude: mean').write(f.axes_names()))
            
            g = f.collapse('T: mean within years time: minimum over years', 
                           within_years=cf.M(), weights=None, _debug=0)
            self.assertTrue(g.cell_methods == cf.CellMethods('time: maximum time: mean within years time: minimum over years').write(f.axes_names()))

            for m in range(1, 13):
                a = numpy.empty((5, 4, 5))
                for i, year in enumerate(f.subspace(T=cf.month(m)).coord('T').year.unique()):
                    q = cf.month(m) & cf.year(year)
                    x = f.subspace(T=q)
                    x.data.mean(axes=0, i=True)
                    a[i] = x.array
                #--- End: for
                a = a.min(axis=0)
                self.assertTrue(numpy.allclose(a, g.array[m % 12]))
            #--- End: for  

            g = f.collapse('T: mean', group=360)

            for group in (cf.M(12), 
                          cf.M(12, month=12),
                          cf.M(12, day=16),
                          cf.M(12, month=11, day=27)):
                g = f.collapse('T: mean', group=group)
                bound = g.coord('T').bounds.dtarray[0, 1]
                self.assertTrue(bound.month == group.offset.month,
                                "{}!={}, group={}".format(bound.month, group.offset.month, group))
                self.assertTrue(bound.day   == group.offset.day,
                                "{}!={}, group={}".format(bound.day, group.offset.day, group))
            #--- End: for  

#            for group in (cf.D(30), 
#                          cf.D(30, month=12),
#                          cf.D(30, day=16),
#                          cf.D(30, month=11, day=27)):
#                g = f.collapse('T: mean', group=group)
#                bound = g.coord('T').bounds.dtarray[0, 1]
#                self.assertTrue(bound.day == group.offset.day,
#                                "{}!={}, bound={}, group={}".format(bound.day, group.offset.day, bound, group))
            #--- End: for  

        #--- End: for    

        cf.CHUNKSIZE(self.original_chunksize)
    #--- End: def

    def test_Field_where(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        f = cf.read(self.filename)[0]
        a = f.array

        for chunksize in self.chunk_sizes:
            f = cf.read(self.filename)[0]

            for condition in (True, 1, [[[True]]], [[[[[456]]]]]):
                g = f.where(condition, -9)
                self.assertTrue(g[0].min() == -9)
                self.assertTrue(g[0].max() == -9)                

            g = f.where(cf.le(34), 34)
            self.assertTrue(g[0].min() == 34)
            self.assertTrue(g[0].max() == 89)   

            g = f.where(cf.le(34), cf.masked)
            self.assertTrue(g[0].min() == 35)
            self.assertTrue(g[0].max() == 89) 

            g = f.where(cf.le(34), cf.masked, 45)
            self.assertTrue(g[0].min() == 45)
            self.assertTrue(g[0].max() == 45)               
        #--- End: for

        cf.CHUNKSIZE(self.original_chunksize)
    #--- End: def   

    def test_Field_mask_invalid(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        f = cf.read(self.filename)[0]

        g = f.mask_invalid()
        g = cf.FieldList(f).mask_invalid()
        g = f.mask_invalid(i=True)
        g = cf.FieldList(f).mask_invalid(i=True)
    #--- End: def
        
#--- End: class

if __name__ == '__main__':
    print 'Run date:', datetime.datetime.now()
    cf.environment()
    print''
    unittest.main(verbosity=2)
