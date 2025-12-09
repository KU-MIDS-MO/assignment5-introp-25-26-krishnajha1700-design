import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(data, filename="turning_points.pdf"):
    data = np.asarray(data)
    shift = np.diff(data)

    flips = []
    for h in range(1, len(shift)):
        if shift[h] == 0 or shift[h-1] == 0:
            continue
        if np.sign(shift[h]) != np.sign(shift[h-1]):
            flips.append(h)

    pts = np.array(flips)

    t = np.arange(len(data))
    plt.figure()
    plt.plot(t, data, marker='o')
    plt.plot(pts, data[pts], "ro")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Turning Points")
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

    return pts
