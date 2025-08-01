import os
import time

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(file_path)
root_dir = os.path.dirname(src_dir)


def logdir(name_logdir=None):
    os.makedirs(os.path.join(root_dir, "logs"), exist_ok=True)
    run_id = time.strftime("run-%Y-%m-%d-%H-%M-%S")
    return os.path.join(root_dir, "logs", name_logdir, run_id)
