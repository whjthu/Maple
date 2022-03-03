from os import curdir
import re
from tarfile import REGULAR_TYPES
from types import CodeType
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from numpy.lib.function_base import cov
from enum import Enum
from random import randint
import math

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


# Generate dummy data for plotting
class DataType:
    REGULAR = 0
    WIDE_RANGE = 1
    WITH_BIGNUM = 2
    WITH_INF = 3


def data_generator(type=DataType.REGULAR, dims=[], special_ratio=0.2) -> np.array:
    assert len(dims) > 0, "[dataData dimension cannot be 0"
    seeds = []
    for _ in range(100):
        if type == DataType.REGULAR:
            seeds.append(randint(3, 10))
        elif type == DataType.WIDE_RANGE:
            seeds.append(randint(1, 1000))
        elif type == DataType.WITH_BIGNUM:
            if randint(0, 1000) > 1000*special_ratio:
                seeds.append(randint(3, 10))
            else:
                seeds.append(randint(100, 200))
        elif type == DataType.WITH_INF:
            if randint(0, 1000) > 1000*special_ratio:
                seeds.append(randint(3, 10))
            else:
                seeds.append(math.inf)
    idx = 0
    result = np.empty(dims)

    def fillNumber(data: np.array, curdim: int):
        nonlocal seeds, idx
        assert curdim < len(dims), "Index error in data generation"
        for i in range(dims[curdim]):
            if curdim < len(dims)-1:
                fillNumber(data[i], curdim+1)
            else:
                data[i] = seeds[idx]
                idx += 1

    fillNumber(result, 0)
    return result
