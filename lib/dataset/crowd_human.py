import os
import json

import fiftyone

def get_crowd_human_dataset(dataset_dir, split="train"):
    if split is "train":
        directory = os.path.join(dataset_dir, "train/")
    elif split is "val":
        directory = os.path.join(dataset_dir, "val/")
    else:
        raise ValueError("Invalid Split Argument")

    dataset_type = fiftyone.types.YOLOv4Dataset
    dataset = fiftyone.Dataset.from_dir(
        dataset_dir=directory,
        dataset_type=dataset_type
    )
    
    return dataset


def launch_fiftyone_dataset(fiftyone_dataset=None):
    if not fiftyone_dataset:
        fiftyone_dataset = get_crowd_human_dataset()
    fiftyone.launch_app(fiftyone_dataset)

if __name__ == '__main__':
    dataset_dir = "/home/n8srumsey/Documents/AI Club/datasets/Darknet_CrowdHuman"
    launch_fiftyone_dataset(dataset_dir)
