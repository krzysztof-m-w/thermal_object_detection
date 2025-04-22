import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import PIL.Image as Image
import tqdm
import yaml

def plot_with_labels(image, label, names, ax, color='red'):
    """Plot image with labels."""
    ax.imshow(image, zorder=1)  # Set image zorder
    for box in label:
        label, x_center, y_center, width, height = box[:5]
        x_center *= image.shape[1]
        y_center *= image.shape[0]
        width *= image.shape[1]
        height *= image.shape[0]  
        rect = plt.Rectangle(
            (x_center - width / 2, y_center - height / 2),
            width, height,
            linewidth=2, edgecolor=color, facecolor='none',
            zorder=2  # Ensure it's drawn above the image
        )
        ax.add_patch(rect)
        ax.text(
            x_center - width / 2, y_center - height / 2 - 10,
            names[label],
            color='red', fontsize=10, zorder=3  # Ensure text is above the rectangle
        )
        ax.add_patch(rect)
    ax.axis('off')


def load_data(dir_name: str):
    """Load data from the specified directory."""
    data = []
    for file_name in tqdm.tqdm(os.listdir(dir_name), desc="Loading images"):
        if file_name.endswith('.jpg'):
            file_path = os.path.join(dir_name, file_name)
            image = Image.open(file_path)
            data.append(np.array(image))
    return data

def load_labels(dir_name: str):
    """Load labels from the specified directory."""
    labels = []
    for file_name in tqdm.tqdm(os.listdir(dir_name), desc="Loading labels"):
        if file_name.endswith('.txt'):
            file_path = os.path.join(dir_name, file_name)
            with open(file_path, 'r') as f:
                lines = f.readlines()
                label = np.array([[float(elm) for elm in line.split(" ")] for line in lines])
                labels.append(label)

    return labels

def load_names(path: str):
    with open(path, 'r') as file:
        data = yaml.safe_load(file)
        names = data.get("names", {})
    return names