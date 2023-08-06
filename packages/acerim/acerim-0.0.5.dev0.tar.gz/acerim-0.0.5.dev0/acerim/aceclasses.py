#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:24:07 2016

@author: christian 
"""
import gdal
import pandas as pd
import numpy as np
from acerim import acefunctions as af
#%%
class CraterDataFrame(pd.DataFrame):
    """
    Class for representing and manipulating crater data. Extends the pandas 
    Dataframe, a "two-dimensional size-mutable, potentially heterogeneous
    tabular data structure". Columns represent data fields and rows represent
    individual craters. See help(pandas.DataFrame) for more info. 
    
    Parameters
    ----------
    data : str or pandas.DataFrame
        Str will assume a filename ending in '.csv' with data to be read. It is 
        recommended to pass a pandas.DataFrame object if complicated import 
        options are required.
    **kwargs : 
        All optional arguments from pandas.DataFrame can be appended as keyword 
        arguments.
                
        
    Examples
    --------
    >>> cdict = {'Lat' : [10, -20., 80.0],'Lon' : [14, -40.1, 317.2],'Diam' : [2, 12., 23.7]}
    >>> cdf = CraterDataFrame(cdict)
    >>> cdf['Diam'][0]
    2.0
    >>> index = ['Crater A', 'Crater B', 'Crater C']
    >>> cdf2 = CraterDataFrame(cdict, index=index)
    >>> cdf2.loc['Crater A']['Lat']
    10.0
    >>> cols = ['Lat', 'Lon', 'Diam']
    >>> cdf3 = CraterDataFrame(cdict, index=index, columns=cols)
    >>> cdf3.keys()[0]
    'Lat'
    """
    def __init__(self, data=None, index_col=None, latcol=None, 
    			 loncol=None, radcol=None, **kwargs):
        """
        Initialize a CraterDataFrame object. See help(CraterDataFrame)
        for correct usage.
        
        """
        if isinstance(data, str):
            data = pd.read_csv(data, index_col=index_col) 
        super(CraterDataFrame, self).__init__(data, **kwargs)
        
        # If no lat-, lon-, or rad- col provided, try to find them in columns
        if not latcol:
            findlat = ['lat' in col.lower() for col in self.columns]
            if any(findlat):
                latcol = self.columns[np.where(findlat)[0][0]]
        if not loncol:
            findlon = ['lon' in col.lower() for col in self.columns]
            if any(findlon):
                loncol = self.columns[np.where(findlon)[0][0]]
        if not radcol:
            findrad = ['rad' in col.lower() for col in self.columns]
            finddiam = ['diam' in col.lower() for col in self.columns]
            if any(findrad):
                radcol = self.columns[np.where(findrad)[0][0]]
            elif any(finddiam):
                diamcol = self.columns[np.where(finddiam)[0][0]]
                self['_Rad'] = (0.5)*self[diamcol]
                radcol = '_Rad'
        if not latcol or not loncol or not radcol:
            raise ImportError('Unable to infer lat or lon or rad from header.'\
                              +'Specify name of latcol, loncol and/or radcol')
        self.latcol = latcol
        self.loncol = loncol
        self.radcol = radcol


class AceDataset(object):
    """
    Class for loading and manipulating image data. Wraps the gdal Dataset
    object. See help(gdal.Dataset) for list of wrapped attributes and methods.
    Input image must be in simple cylindrical projection (Plate Caree).
    
    Parameters
    ----------
    dataset : str or gdal.Dataset
        Str will assume a filename compatible with gdal.Open(data). It is 
        recommended to pass an open simple cylindrical projected gdal.Dataset 
        object if other import or reprojection options are required. 
    nlat : int, float
        North latitude of dataset in (decimal) degrees.
    slat : int, float
        South latitude of dataset in (decimal) degrees.
    wlon : int, float
        West latitude of dataset in (decimal) degrees.
    elon : int, float
        East latitude of dataset in (decimal) degrees.
    r : int, float
        Radius of planeary body in km.
    *kwargs : ...
        Additional attributes to include in this instance of AceDataset, 
        accessible by the supplied keyword.
    
    >>> import os
    >>> f=os.path.dirname(os.path.abspath('__file__'))+'/tests/moon.tif'
    >>> ads = AceDataset(f, radius=1737)
    """
    def __init__(self, dataset, nlat=None, slat=None, wlon=None, elon=None, 
                 radius=None, ppd=None, **kwargs):
        """
        Initialize an AceDataset object. See help(AceDataset) for correct 
        usage.
        """        
        if isinstance(dataset, str):
            self.gdalDataset = gdal.Open(dataset)
            if not self.gdalDataset:
                raise ImportError('Unable to open file. Check file path.')
        elif isinstance(dataset, gdal.Dataset):
            self.gdalDataset = dataset
        else:
            raise ImportError('Invalid input dataset')
        args = [nlat, slat, wlon, elon, radius, ppd]
        attrs = ['nlat','slat','wlon','elon','radius','ppd']
        dsinfo = self.get_info()
        for i,arg in enumerate(args):
            if arg is None: # If optional argument missing, fill from dsinfo
                setattr(self, attrs[i], dsinfo[i])
            else:
                setattr(self, attrs[i], arg)

        for key, value in kwargs.items():
            setattr(self, key, value)


    def __getattr__(self, name):
        """Points method and attribute calls to self.gdalDataset."""
        if name not in self.__dict__: # If not implemented in AceWrapper
            func = getattr(self.__dict__['gdalDataset'], name)
            if callable(func): # Call method
                def gdalDataset_wrapper(*args, **kwargs):
                    return func(*args, **kwargs)
                return gdalDataset_wrapper
            else: # Not callable so must be attribute
                return func


    def calc_mpp(self, lat=0):
        """
        Return the ground resolution in meters/pixel at the given latitude. 
        
        Parameters
        ----------
        lat: int, float
            Current latitude. Defaults to the equator (lat=0) if not specified. 
        
        Examples
        --------
        >>> import os
        >>> f = os.path.dirname(os.path.abspath('__file__'))+'/tests/moon.tif'
        >>> a = AceDataset(f, radius = 1737)
        >>> '{:.3f}'.format(a.calc_mpp())
        '7.579'
        >>> '{:.3f}'.format(a.calc_mpp(50))
        '4.872'
        """
        pixwidth = 1/self.ppd
        dist = af.greatcircdist(lat, 0, lat, pixwidth, self.radius)
        return dist
              

    def get_info(self):
        """
        Return list of georeferencing and projection information from the input
        data file if available. See help(gdal.Dataset) for compatible files.
        
        Returns
        -------
        nlat : int, float
            North latitude from gdal.Dataset.GetProjection()
        slat : int, float
            South latitude calculated using resolution (degrees/pixel) from 
            gdal.Dataset.GetProjection() and the y-size of the image.
        wlon : int, float
            West latitude from gdal.Dataset.GetProjection()
        elon : int, float
            East latitude calculated using resolution (degrees/pixel) from 
            gdal.Dataset.GetProjection() and the x-size of the image.
        ppd : float
            Pixel resolution in pixels/degree from gdal.Dataset.GetProjection.
            
        Examples
        --------
        >>> import os
        >>> f = os.path.dirname(os.path.abspath('__file__'))+'/tests/moon.tif'
        >>> a = AceDataset(f)
        >>> a.get_info()
        (90.0, -90.0, -180.0, 180.0, 6378.137, 4.0)
        """
        xsize, ysize = self.RasterXSize, self.RasterYSize
        geotrans = self.GetGeoTransform()
        try:
            radius = 0.001*float(self.GetProjection().split(',')[3]) # Assume WKT format
        except IndexError:
            raise ImportError('Dataset radius not defined')
            radius = None
        wlon, dpp, nlat = (geotrans[0], geotrans[1], geotrans[3])
        elon = wlon + xsize*dpp
        slat = nlat - ysize*dpp
        ppd = 1/dpp
        return nlat, slat, wlon, elon, radius, ppd
#%%        
        
    def is_global(self):
        """
        Check if self has 360 degrees of longitude.
        
        Examples
        --------
        >>> import os
        >>> f = os.path.dirname(os.path.abspath('__file__'))+'/tests/moon.tif'
        >>> a = AceDataset(f, 90, -90, 0, 360, 1737)
        >>> a.is_global()
        True
        """
        return abs(self.elon - self.wlon) == 360
    
    
    def get_roi(self, lat, lon, rad, wsize=1, mask_crater=False, plot=False, 
               get_extent=False):
        """
        Return square ROI centered on (lat,lon) which extends wsize crater 
        radii from the crater center. 
        
        If the the lon extent of a global dataset is crossed, use wrap_lon(). 
        If the lon extent of a non global dataset of the lat extent is crossed, 
        raise error.
    
        Arguments:
        ----------
        lat : int, float
            Crater latitude, centre latitude of ROI.
        lon : int, float
            Crater longitude, centre longitude of ROI.
        rad : int, float
            Crater radius.
        wsize : int, float
            Window size in crater radii. Side length of ROI around crater is 
            2*wsize*rad (E.g., ROI with wsize=1 gives smallest square around
            crater, making the side lengths 1 diam).
        mask_crater : bool
            Masks the crater floor from the resulting ROI by replacing the 
            crater with an ellipse of NaN.
        plot : bool
            Plots the returned ROI.

        Returns:
        --------
        roi: 2Darray
            Numpy 2D array of data centered on the specified crater and 
            extending wsize*rad distance from the crater centre.
        """
        def wrap_lon(ads, minlon, maxlon, topind, height):
            """
            Return ROI that extends past the right edge of a global dataset by 
            wrapping and concatenating the right and left sides of the ROI.
            """
            if minlon < ads.wlon: 
                leftind = af.get_ind(minlon, lonarr - 360)
                leftwidth = af.deg2pix(ads.wlon - minlon, ads.ppd)
                rightind = af.get_ind(ads.wlon, lonarr)
                rightwidth = af.deg2pix(maxlon - ads.wlon, ads.ppd)
            elif maxlon > ads.elon:
                leftind = af.get_ind(minlon, lonarr)
                leftwidth = af.deg2pix(ads.elon - minlon, ads.ppd)
                rightind = af.get_ind(ads.elon, lonarr + 360)
                rightwidth = af.deg2pix(maxlon - ads.elon, ads.ppd)                
            left_roi = ads.ReadAsArray(leftind, topind, leftwidth, height)
            right_roi = ads.ReadAsArray(rightind, topind, rightwidth, height)
            return np.concatenate((left_roi, right_roi), axis=1)
                      
        # If crater lon out of bounds, switch lon convention [(0,360) <-> (-180,180)]
        if lon > self.elon: 
            lon -= 360
        if lon < self.wlon:
            lon += 360
        # Get window extent in degrees
        dwsize = af.m2deg(wsize*rad, self.calc_mpp(lat), self.ppd)
        minlat = lat-dwsize
        maxlat = lat+dwsize
        minlon = lon-dwsize
        maxlon = lon+dwsize
        extent = (minlon, maxlon, minlat, maxlat)
        # Throw error if window bounds are not in lat bounds.
        if minlat < self.slat or maxlat > self.nlat:
            raise ImportError('Latitude ({},{}) out of dataset bounds ({},{}) '.format(
                                       minlat, maxlat, self.slat, self.nlat))
        # Make dataset pixel arrays
        latarr = np.linspace(self.nlat, self.slat, self.RasterYSize)
        lonarr = np.linspace(self.wlon, self.elon, self.RasterXSize)
        # Get top index and height of ROI
        topind = af.get_ind(maxlat, latarr) 
        height = af.deg2pix(2*dwsize, self.ppd)
        # Check if ROI crosses lon extent of global ROI and needs to be wrapped
        if self.is_global() and (minlon < self.wlon or maxlon > self.elon):
            roi = wrap_lon(self, minlon, maxlon, topind, height)  
        else: 
            # Get left index and width of ROI and read data from dataset
            leftind = af.get_ind(minlon,lonarr) 
            width = af.deg2pix(2*dwsize, self.ppd)
            roi = self.ReadAsArray(leftind, topind, width, height) # gdal Dataset method
        if roi is None:
            raise ImportError('GDAL could not read dataset into array')
            return
        if mask_crater:
            cmask = af.crater_floor_mask(self, roi, lat, lon, rad)
            roi = af.mask_where(roi, cmask)
        if plot:
            self.plot_roi(roi, extent=extent)    
        if get_extent:
            return roi, extent
        else:
            return roi 

    
    def plot_roi(self, roi, *args, **kwargs):
        """
        Implements plot_roi function in functions.py. 
        """
        af.plot_roi(self, roi, *args, **kwargs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
