import kagglehub
import os

def download_data():
    # Download latest version
    path = kagglehub.dataset_download("pandrii000/hituav-a-highaltitude-infrared-thermal-dataset")

    print("Path to dataset files:", path)

    os.makedirs("tmp")
    subdir = os.path.join(path, "hit-uav")
    os.rename(subdir, os.path.join("tmp", "dataset"))