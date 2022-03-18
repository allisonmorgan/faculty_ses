#!/usr/bin/env python

__author__ = "Sam Way"
__copyright__ = "Copyright 2017, The Clauset Lab"
__license__ = "BSD"
__maintainer__ = "Sam Way"
__email__ = "samfway@gmail.com"
__status__ = "Development"

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rcParams
from matplotlib.lines import Line2D

# Constants
SINGLE_FIG_SIZE = (6, 4)
DOUBLE_FIG_SIZE = (12, 4)
TRIPLE_FIG_SIZE = (3, 4)
PLOT_DIR = "plots"
BAR_WIDTH = 0.6
TICK_SIZE = 15
XLABEL_PAD = 10
LABEL_SIZE = 14
TITLE_SIZE = 16
LEGEND_SIZE = 12
LINE_WIDTH = 2
LIGHT_COLOR = '0.7'
LIGHT_COLOR_V = np.array([float(LIGHT_COLOR) for i in range(3)])
DARK_COLOR = '0.4'
DARK_COLOR_V = np.array([float(DARK_COLOR) for i in range(3)])
ALMOST_BLACK = '0.125'
ALMOST_BLACK_V = np.array([float(ALMOST_BLACK) for i in range(3)])
ACCENT_COLOR = '#00ad43'

# Configuration
rcParams['pdf.use14corefonts'] = True
rcParams['ps.useafm'] = True
rcParams['text.latex.preamble'] = [
    r'\usepackage{helvet}',
    # r'\usepackage[scale=1.0]{tgheros}',
    r'\usepackage[frenchmath]{newtxsf}',
    r'\renewcommand{\familydefault}{\sfdefault}'
    r'\usepackage{mathastext}']  # Force sans-serif math mode (for axes labels)


rcParams['font.family'] = 'sans-serif'
rcParams['font.weight'] = 'regular'  # ... for regular text
rcParams['pdf.fonttype'] = 42
# Choose a nice font here
rcParams['font.family'] = ['Helvetica Neue', 'HelveticaNeue', 'Helvetica']
rcParams['ps.fonttype'] = 42
rcParams['text.color'] = ALMOST_BLACK
rcParams['axes.unicode_minus'] = False

rcParams['xtick.major.pad'] = '8'
rcParams['axes.edgecolor'] = ALMOST_BLACK
rcParams['axes.labelcolor'] = ALMOST_BLACK

rcParams['lines.color'] = ALMOST_BLACK
rcParams['xtick.color'] = ALMOST_BLACK
rcParams['ytick.color'] = ALMOST_BLACK
rcParams['text.color'] = ALMOST_BLACK
rcParams['lines.solid_capstyle'] = 'butt'
rcParams['text.usetex'] = True # Let TeX do the typsetting


def single_fig(figsize=SINGLE_FIG_SIZE):
    return plt.subplots(1, 1, figsize=figsize)


def color_bp(bp, color):
    """ Helper function for making prettier boxplots """
    c = np.array(color)  # * 0.5
    c = tuple(c)

    for x in bp['boxes']:
        plt.setp(x, color=c)
        x.set_facecolor(color)
    for x in bp['medians']:
        plt.setp(x, color='w')
    for x in bp['whiskers']:
        plt.setp(x, color=c)
    for x in bp['fliers']:
        plt.setp(x, color=c)
    for x in bp['caps']:
        plt.setp(x, color=c)


def adjust_spines(ax, spines):
    """
    From:
    http://matplotlib.org/examples/pylab_examples/spine_placement_demo.html
    """
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # outward by 10 points
            spine.set_smart_bounds(True)
        else:
            spine.set_color('none')  # don't draw spine

    # turn off ticks where there is no spine
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        # no yaxis ticks
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        # no xaxis ticks
        ax.xaxis.set_ticks([])


def hide_right_top_axis(ax):
    """ Remove the top and right axis """
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)


def finalize(ax, fontsize=LABEL_SIZE, labelpad=7):
    """ Apply final adjustments """
    ax.tick_params(direction='out')
    for tick in ax.get_xticklabels():
        tick.set_fontname("Helvetica")
    for tick in ax.get_yticklabels():
        tick.set_fontname("Helvetica")
    hide_right_top_axis(ax)
    ax.yaxis.label.set_size(fontsize)
    ax.xaxis.label.set_size(fontsize)
    ax.tick_params(axis='both',
                   which='major',
                   labelsize=fontsize, pad=labelpad)
    ax.xaxis.set_tick_params(width=1)
    ax.yaxis.set_tick_params(width=1)

def custom_legend_handles(markers, colors, markersizes, **kwargs):
    
    # For now, assume everything has the same length
    assert(len(markers) == len(colors))
    assert(len(colors) == len(markersizes))
    
    handles = []
    for i in range(len(markers)):
        handles.append(Line2D(range(1), range(1), color=colors[i], marker=markers[i], markersize=markersizes[i], 
                             linestyle='None', markeredgecolor='w', **kwargs))
        
    return handles

# https://stackoverflow.com/questions/11517986/indicating-the-statistically-significant-difference-in-bar-graph
def label_diff(ax, i, j, text, X, Y):
    x = (X[i]+X[j])/2
    y = max(Y[i], Y[j])-0.14
    # dx = abs(X[i]-X[j])

    props = {'connectionstyle':'bar','arrowstyle':'-','shrinkA':20,'shrinkB':20,'linewidth':1}
    ax.annotate(text, xy=(x, y+0.15), zorder=10, fontsize=TITLE_SIZE, ha='center')
    ax.annotate('', xy=(X[i],y), xytext=(X[j],y), arrowprops=props, zorder=1)

