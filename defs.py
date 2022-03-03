from types import CodeType
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from numpy.lib.function_base import cov

# Set font type for Chinese
# matplotlib.rcParams['pdf.fonttype'] = 42
# matplotlib.rcParams['ps.fonttype'] = 42

# Set env var
basedir = './outputs/'
sysname = 'Sys'

# Set rcParams
sz, fontsz = (6, 3), 16
rcParams = {
    'axes.labelsize': fontsz,
    'font.size': fontsz,
    'legend.fontsize': fontsz,
    'xtick.labelsize': fontsz,
    'ytick.labelsize': fontsz,
    'figure.figsize': sz,
    # Set font type to Linux Libertine, which is the default font type in Latex.
    # The font must be already installed.
    'font.sans-serif': 'Linux Libertine',
    # Another way to set font type to Linux Libertine.
    # In this way, users do not need to intall the font type mannually.
    # Instead, Latex support (e.g., MiKTeX) is needed.
    # "font.family": "serif",
    # "text.usetex": True,
    # 'text.latex.preview': True,
    # 'text.latex.preamble': [
    #     r"""
    #     \usepackage{libertine}
    #     \usepackage[libertine]{newtxmath}
    #     """],
}
plt.rcParams.update(rcParams)

hb = '\\\\//\\\\//'

SHOW_FIGURE = True
SAVE_FIGURE = False
FIGURE_TYPE = 'pdf'


# Define color theme
color_light = [
    '#f4b183',
    '#ffd966',
    '#c5e0b4',
    '#bdd7ee',
    "#8dd3c7",
    "#bebada",
    "#fb8072",
    "#80b1d3",
    "#fdb462",
    "#cccccc",
    "#fccde5",
    "#b3de69",
    "#ffd92f",
    '#fc8d59',
    '#74a9cf',
    '#66c2a4',
    '#f4a143',
    '#ffc936',
    '#78c679',
]

color_dark = [
    '#5AA469',
    '#1A508B',
    '#F39233',
    '#B61919',
    '#333333',
]

# Define hatches
hatch_def = [
    '//',
    '\\\\',
    'xx',
    '++',
    '--',
    '||',
    '..',
    'oo',
    '',
]

# Define markers
marker_def = [
    'o',
    'x',
    'D',
    '*',
    '+',
]

# Define line styles
linestyle_def = [
    'solid',                       # 'solid',  Same as (0, ()) or '-'
    'dotted',                      # 'dotted', Same as (0, (1, 1)) or ':'
    'dashed',                      # 'dashed', Same as '--'
    'dashdot',                     # 'dashdot' Same as '-.'
    (0, (1, 10)),                  # 'loosely dotted'
    (0, (1, 1)),                   # 'dotted'
    (0, (1, 1)),                   # 'densely dotted',
    (0, (5, 10)),                  # 'loosely dashed',
    (0, (5, 5)),                   # 'dashed',
    (0, (5, 1)),                   # 'densely dashed',
    (0, (3, 10, 1, 10)),           # 'loosely dashdotted',
    (0, (3, 5, 1, 5)),             # 'dashdotted',
    (0, (3, 1, 1, 1)),             # 'densely dashdotted',
    (0, (3, 5, 1, 5, 1, 5)),       # 'dashdotdotted',
    (0, (3, 10, 1, 10, 1, 10)),    # 'loosely dashdotdotted'
    (0, (3, 1, 1, 1, 1, 1)),       # 'densely dashdotdotted'
]


def test_color_bars(color_vec=color_light, hatch_vec=hatch_def, path=''):
    N = len(color_vec)
    figsz = {'figure.figsize': (N, 5)}
    plt.rcParams.update(figsz)
    dat = [1 for i in range(N)]
    fig, ax = plt.subplots()
    W = 0.35
    ind = np.arange(N) - 2 * W
    ax.bar(ind, dat, color=color_vec, hatch=hatch_vec)
    bars = ax.patches
    hatches = []
    for i in range(N):
        hatches.append(hatch_vec[i % len(hatch_vec)])
    for bar, hatch in zip(bars, hatches):
        bar.set_hatch(hatch)
    legend_handles = [mpatches.Patch(
        facecolor=color_vec[i], hatch=hatches[i], label=str(i)) for i in range(N)]
    plt.legend(legend_handles, range(
        N), bbox_to_anchor=(1, 1), ncol=2)
    plt.subplots_adjust(bottom=0.2)
    xvals = np.arange(N)
    ax.set_xticks(ind)
    ax.set_xticklabels(str(x) for x in xvals)
    if SHOW_FIGURE:
        plt.tight_layout()
        plt.show()
    if SAVE_FIGURE:
        fig.savefig(basedir + 'test_color_bars.' +
                    FIGURE_TYPE, bbox_inches='tight')


test_color_bars(color_light, hatch_def)


def test_color_lines(color_vec=color_dark, marker_vec=marker_def, linestyle_vec=linestyle_def):
    N = len(color_vec)
    figsz = {'figure.figsize': (8, max(N//3, 4))}
    plt.rcParams.update(figsz)
    dat = [[i for j in range(5)] for i in range(N)]
    fig, ax = plt.subplots()
    markers = []
    for i in range(N):
        markers.append(marker_vec[i % len(marker_vec)])

    for i in range(N):
        ax.plot(dat[i], linestyle=linestyle_vec[i],
                color=color_vec[i], marker=markers[i])

    legend_handles = [mlines.Line2D([], [], linestyle=linestyle_vec[i],
                                    color=color_vec[i], marker=markers[i], label=str(i)) for i in range(N)]
    plt.legend(handles=legend_handles, ncol=N//15 +
               1, bbox_to_anchor=(1, 1), fontsize=14)
    if SHOW_FIGURE:
        plt.tight_layout()
        plt.show()
    if SAVE_FIGURE:
        fig.savefig(basedir + 'test_color_lines.' +
                    FIGURE_TYPE, bbox_inches='tight')


# test_color_lines(color_dark, marker_def, linestyle_def)

# Generate dummy data for plotting
def data_generator(dims=[]):
    pass
