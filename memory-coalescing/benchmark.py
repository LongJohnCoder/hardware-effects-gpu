import os
import sys

import matplotlib.pyplot as plt
import seaborn

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(ROOT)
from utils import benchmark


data = [
    ("Start offset", [1, 32]),
    ("Move offset", [32, 1])
]

frame = benchmark(data)

g = seaborn.barplot(data=frame, x="Start offset", y="Time", hue="Move offset")
plt.show()
