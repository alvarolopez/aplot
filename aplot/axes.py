from aplot import colors


def setup_axes(axes, ygrid=True, xgrid=False, xtics=True):
    axes.spines["top"].set_visible(False)
    axes.spines["right"].set_visible(False)
    axes.spines["left"].set_color(colors.gray)
    axes.spines["bottom"].set_color(colors.gray)

    axes.get_xaxis().tick_bottom()
    axes.get_yaxis().tick_left()

    axes.yaxis.grid(ygrid)
    axes.xaxis.grid(xgrid)

    axes.tick_params(axis='both', which='major', labelsize=8, colors=colors.gray)
    axes.tick_params(axis='both', which='minor', labelsize=6, colors=colors.gray)

    if not xtics:
        axes.tick_params(axis='x',          # changes apply to the x-axis
                         which='both',      # both major and minor ticks are affected
                         bottom='off',      # ticks along the bottom edge are off
                         top='off',         # ticks along the top edge are off
                         labelbottom='off') # labels along the bottom edge are off
