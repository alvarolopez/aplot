from collections import OrderedDict

from matplotlib import pyplot
from matplotlib import font_manager


def setup_legend(axes):
    font = font_manager.FontProperties()
    font.set_size('small')
    handles, labels = pyplot.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    lg = axes.legend(by_label.values(),
                       by_label.keys(),
                       loc="upper center",
                       bbox_to_anchor=(0.5, -0.1),
                       fancybox=True,
                       prop=font,
                       ncol=5)
    lg.draw_frame(False)
