from matplotlib import pyplot


def save_pdf(name):
    name = "%s.pdf" % name
    pyplot.tight_layout()
    pyplot.savefig(name, bbox_inches='tight')
