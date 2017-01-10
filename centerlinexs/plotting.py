# These are for graphic only
import matplotlib.pyplot as plt
from shapely.geometry import *
from matplotlib.collections import PatchCollection
from descartes import PolygonPatch

class Plotter:

    def __init__(self):
        self.fig = plt.figure(1, figsize=(10, 10))
        self.ax = self.fig.gca()

    def plotShape(self, mp, color, alpha, zord):
        """
        Nothing fancy here. Just a plotting function to help us visualize
        :param ax:
        :param mp:
        :param color:
        :param alpha:
        :param zord:
        :return:
        """
        # We're using Descartes here for polygonpathc
        if mp.type == 'Polygon':
            self.ax.add_patch(PolygonPatch(mp, fc=color, ec='#000000', lw=0.2, alpha=alpha, zorder=zord))

        elif mp.type == 'LineString':
            x, y = mp.xy
            self.ax.plot(x, y, color=color, alpha=alpha, linewidth=1, solid_capstyle='round', zorder=zord)

        elif mp.type == 'MultiPoint':
            for idx, p in enumerate(mp):
                x, y = p.xy
                self.ax.plot(x, y, color=color, alpha=alpha, markersize=2, marker="o", zorder=zord)

        elif mp.type == 'MultiLineString':
            for idx, p in enumerate(mp):
                x, y = p.xy
                self.ax.plot(x, y, color=color, alpha=alpha, linewidth=1, solid_capstyle='round', zorder=zord)

        elif mp.type == 'MultiPolygon':
            patches = []
            for idx, p in enumerate(mp):
                patches.append(PolygonPatch(p, fc=color, ec='#000000', lw=0.2, alpha=alpha, zorder=zord))
                self.ax.add_collection(PatchCollection(patches, match_original=True))

    @staticmethod
    def showPlot(bounds=None):
        if bounds is not None:
            plt.ylim(bounds[1], bounds[3])
            plt.xlim(bounds[0], bounds[2])
        plt.autoscale(enable=False)
        plt.show()