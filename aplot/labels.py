from matplotlib import pyplot

from aplot import colors


def set_labels(xlabel=None, ylabel=None, title=None):
    if xlabel:
        pyplot.xlabel(xlabel, fontsize=10, color=colors.gray)

    if ylabel:
        pyplot.ylabel(ylabel, fontsize=10, color=colors.gray)

    if title:
        pyplot.title(title, fontsize=12, color=colors.gray)
