import os

import matplotlib.pyplot as plt

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(file_path)
root_dir = os.path.dirname(src_dir)


def save_fig(chapter, fig_id, format="png", resolution=300, tight_layout=True):
    os.makedirs(os.path.join(root_dir, "IMAGE", chapter), exist_ok=True)
    path = os.path.join(root_dir, "IMAGE", chapter, fig_id + "." + format)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, dpi=resolution, format=format)
