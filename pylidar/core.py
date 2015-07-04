from pylidar import np, plt
from itertools import islice

from matplotlib.colors import LightSource
from mpl_toolkits.mplot3d import Axes3D

class LIDAR(object):
    """Class for loading geospatial Digital Surface Models (DSM)."""

    def __init__(self, input_filename=None):

        if input_filename is not None:
            self.input_filename = input_filename

            with open(self.input_filename) as f:
                for line in islice(f, 0, 6):
                    name, val = line.strip().split()
                    if int(val) == float(val):
                        conv = int
                    else:
                        conv = float
                    setattr(self, name, conv(val))

            self.z = np.loadtxt(self.input_filename, skiprows=6)

            self.z[self.z == self.NODATA_value] = np.nan

            x = np.linspace(self.xllcorner, self.xllcorner+(self.ncols-1*self.cellsize), self.ncols)
            y = np.linspace(self.yllcorner, self.yllcorner+(self.nrows-1*self.cellsize), self.nrows)

            self.x, self.y = np.meshgrid(x, y)

    def plot(self, cmap=plt.cm.terrain, *args, **kwargs):

        fig = plt.figure()
        ax = fig.add_subplot(111)

        extent = [self.x.min(), self.x.max(), self.y.min(), self.y.max()]

        ax.imshow(self.z, cmap=cmap, extent=extent, *args, **kwargs)

        ax.get_xaxis().get_major_formatter().set_useOffset(False)
        ax.get_yaxis().get_major_formatter().set_useOffset(False)

        plt.show()

    def plot_shaded(self, cmap=plt.cm.terrain, lightsource_kwargs=None, *args, **kwargs):

        if lightsource_kwargs is None:
            lightsource_kwargs = {'azdeg':225, 'altdeg':5}

        extent = [self.x.min(), self.x.max(), self.y.min(), self.y.max()]

        arr = self.z.copy()
        nan_mask = np.isnan(arr)
        arr_min = arr[~nan_mask].min()
        if nan_mask.any():
            arr[nan_mask] = max(arr_min-10, 0)

        ls = LightSource(**lightsource_kwargs)
        shaded = ls.shade(arr, cmap=cmap)

        fig = plt.figure()
        ax = fig.add_subplot(111)

        im = ax.imshow(shaded, cmap=cmap, extent=extent, *args, **kwargs)
        plt.colorbar(im)

        ax.get_xaxis().get_major_formatter().set_useOffset(False)
        ax.get_yaxis().get_major_formatter().set_useOffset(False)

        plt.show()

