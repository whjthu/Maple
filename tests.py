from defs import *


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

# test_color_bars(color_light, hatch_def)


def test_data_generator(type=DataType.REGULAR, dims=[], special_ratio=0.2):
    print(data_generator(type, dims, special_ratio))

# test_data_generator(type = DataType.REGULAR, dims = [2,3,2])
# test_data_generator(type = DataType.WITH_BIGNUM, dims = [2,3,2])
