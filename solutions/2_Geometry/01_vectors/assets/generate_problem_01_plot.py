"""Generate the 3D vector-operation diagram for Exercise 1."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.ticker import MaxNLocator


u = np.array([2, -1, 3])
v = np.array([-1, 4, 2])
panels = [
    ("Addition", u, v, r"$u$", r"$v$", r"$u+v=(1,3,5)$"),
    ("Subtraction", u, -v, r"$u$", r"$-v$", r"$u-v=(3,-5,1)$"),
    ("Scaled combination", 3 * u, -2 * v, r"$3u$", r"$-2v$", r"$3u-2v=(8,-11,5)$"),
]
blue, orange, green = "#2563eb", "#d97706", "#059669"
plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans"})
fig = plt.figure(figsize=(18, 7.6), facecolor="white")
fig.suptitle("Vector operations in three dimensions", fontsize=23, fontweight="bold", y=0.97)
fig.text(0.5, 0.9, r"$u=(2,-1,3)$     $v=(-1,4,2)$", ha="center", fontsize=17)

for i, (title, first, second, first_label, second_label, result_label) in enumerate(panels, 1):
    ax = fig.add_subplot(1, 3, i, projection="3d")
    result = first + second
    origin = np.zeros(3)
    for start, vector, color, style in [
        (origin, first, blue, "solid"),
        (origin, second, orange, "solid"),
        (first, second, orange, "dashed"),
        (origin, result, green, "solid"),
    ]:
        ax.quiver(*start, *vector, color=color, linewidth=2.4,
                  arrow_length_ratio=0.13, linestyle=style, normalize=False)
    ax.scatter(*origin, color="#374151", s=20)
    ax.scatter(*result, color=green, s=25)
    # Cubic limits and box aspect preserve geometric length and angle proportions.
    points = np.array([origin, first, second, result])
    lower, upper = points.min(axis=0), points.max(axis=0)
    center = (lower + upper) / 2
    radius = max(upper - lower) * 0.62
    for axis, mid in zip([ax.set_xlim, ax.set_ylim, ax.set_zlim], center):
        axis(mid - radius, mid + radius)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=26, azim=-145)
    for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
        axis.set_major_locator(MaxNLocator(nbins=4, integer=True))
        axis.pane.fill = False
    ax.set_xlabel("x", labelpad=7)
    ax.set_ylabel("y", labelpad=7)
    ax.set_zlabel("z", labelpad=7)
    ax.tick_params(labelsize=10)
    ax.set_title(title, fontsize=17, pad=16)
    handles = [
        Line2D([0], [0], color=blue, lw=2.4, label=first_label),
        Line2D([0], [0], color=orange, lw=2.4, label=second_label),
        Line2D([0], [0], color=green, lw=2.4, label=result_label),
    ]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.08),
              frameon=False, fontsize=12)

fig.text(0.5, 0.025, "Dashed orange arrows translate the second vector to the tip of the first. "
         "Green arrows show the resulting displacement.", ha="center", fontsize=12, color="#374151")
fig.subplots_adjust(left=0.03, right=0.97, top=0.79, bottom=0.24, wspace=0.08)
output = Path(__file__).with_name("problem_01_vectors_3d.png")
fig.savefig(output, dpi=180, facecolor="white")
plt.close(fig)
print(output)
