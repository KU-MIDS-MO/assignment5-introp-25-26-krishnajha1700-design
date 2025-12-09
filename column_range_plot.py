import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    # compute column ranges
    col_max = np.max(A, axis=0)
    col_min = np.min(A, axis=0)
    ranges = col_max - col_min

    # bar plot
    x = np.arange(len(ranges))
    plt.figure()
    plt.bar(x, ranges)
    plt.xlabel("Column Index")
    plt.ylabel("Range (max - min)")
    plt.title("Column Ranges")
    plt.tight_layout()

    # save before showing
    plt.savefig(filename)
    plt.show()

    return ranges
