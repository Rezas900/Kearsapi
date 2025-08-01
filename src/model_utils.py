import os

file_path = os.path.abspath(__file__)
src_dir = os.path.dirname(file_path)
root_dir = os.path.dirname(src_dir)

def Modelpath(model_name, format = "kears"):
    os.makedirs(os.path.join(root_dir, "Model"), exist_ok=True)
    model_path = os.path.join(root_dir, "Model", model_name + "." + format)
    return model_path