import os

def make_dir(save_path : str):
  isExist = os.path.exists(save_path)
  if not isExist:
    os.makedirs(save_path)
    print("The new directory is created!")