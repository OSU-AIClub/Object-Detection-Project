import os
from shutil import rmtree, copy

import numpy as np
from sklearn.model_selection import train_test_split
from tqdm import tqdm

def generate_dataset_split(dataset_path:str, val_split=0.10, test_split=0.20):
    """Generates a Train, Validation, and Testing split for a YOLOv5 dataset.

    Parameters
    ----------
    dataset_path` : str
        Path to the YOLOv5 dataset.
    val_split : float, optional
        Proportion of images to be dedicated to the validation split, by default 0.10
    test_split : float, optional
        Proportion of image to be dedicated to the test split, by default 0.20
    """    

    assert(type(val_split) is float)
    assert(type(test_split) is float)
    assert(val_split + test_split < 1) # cannot have the splits exceed the actual amount of samples


    # Find the paths of all important directories
    images_path = os.path.join(dataset_path, "images")
    labels_path = os.path.join(dataset_path, "labels")
    train_imgs_path = os.path.join(images_path, "train")
    val_imgs_path = os.path.join(images_path, "val")
    test_imgs_path = os.path.join(images_path, "test")
    train_labels_path = os.path.join(labels_path, "train")
    val_labels_path = os.path.join(labels_path, "val")
    test_labels_path = os.path.join(labels_path, "test")

    # Delete old train val split
    imgs_dirs_to_remove = [train_imgs_path, val_imgs_path, test_imgs_path]
    label_dir_to_remove = [train_labels_path, val_labels_path, test_labels_path]

    print("Removing existing train, val, and test splits.")
    for directory in [*imgs_dirs_to_remove, *label_dir_to_remove]:
        if os.path.exists(directory):
            print(f"\tDeleting `{directory}`...")
            rmtree(directory)
        else:
            print(f"\t`{directory}` not found, skipping.")
    print("Finished removing existing train, val, and test splits.")

    """
    file structure should look like this now:
    
    data/
    ├─ images/
    |  ├─ all/
    |  |  ├─ ** ALL IMAGES **
    ├─ labels/
    │  ├─ ** ALL TXT ANNOTATIONS **
    ├─ dataset.yaml

    """

    # Create Split
    rel_train_val_split = (1 / (1 - test_split)) * val_split    # calculate val split relative to the TrainVal subsection
    images = set([im for im in os.listdir(os.path.join(images_path, "all")) if im.endswith(".jpg")])
    lables = set([lbl for lbl in os.listdir(os.path.join(labels_path, "all")) if f"{lbl.split('.')[0]}.jpg" in images])
    images = set([im for im in images if f"{im.split('.')[0]}.txt" in lables])
    images = np.array(list(images)).reshape(-1,1)
    lables = np.array(list(lables)).reshape(-1,1)

    print("\nCreating new train, val, and test splits...")
    TrainValImgs, TestImgs, TrainValLabels, TestLabels = train_test_split(images, lables, test_size=test_split)
    TrainImgs, ValImgs, TrainLabels, ValLabels = train_test_split(TrainValImgs, TrainValLabels, test_size=rel_train_val_split)
    print(f"\t# Samples in Train Split:     {TrainImgs.size}")
    print(f"\t# Samples in Val Split:       {ValImgs.size}")
    print(f"\t# Samples in Test Split:      {TestImgs.size}")

    # copy files to new split
    print("\nSaving train split files...")
    if not os.path.exists(train_imgs_path + "/"):
        os.mkdir(train_imgs_path + "/")
    if not os.path.exists(train_labels_path + "/"):
        os.mkdir(train_labels_path + "/")
    for im, lbl in tqdm(zip(TrainImgs.tolist(), TrainLabels.tolist()), total=len(TrainImgs.tolist())):
        copy(os.path.join(images_path, "all/", im[0]), train_imgs_path + "/")
        copy(os.path.join(labels_path, "all/", lbl[0]), train_labels_path + "/")

    print("\nSaving validation split files...")
    if not os.path.exists(val_imgs_path + "/"):
        os.mkdir(val_imgs_path + "/")
    if not os.path.exists(val_labels_path + "/"):
        os.mkdir(val_labels_path + "/")
    for im, lbl in tqdm(zip(ValImgs.tolist(), ValLabels.tolist()), total=len(ValImgs.tolist())):
        copy(os.path.join(images_path, "all/", im[0]), val_imgs_path + "/")
        copy(os.path.join(labels_path, "all/", lbl[0]), val_labels_path + "/")
    
    print("\nSaving test split files...")
    if not os.path.exists(test_imgs_path + "/"):
        os.mkdir(test_imgs_path + "/")
    if not os.path.exists(test_labels_path + "/"):
        os.mkdir(test_labels_path + "/")
    for im, lbl in tqdm(zip(TestImgs.tolist(), TestLabels.tolist()), total=len(TestImgs.tolist())):
        copy(os.path.join(images_path, "all/", im[0]), test_imgs_path + "/")
        copy(os.path.join(labels_path, "all/", lbl[0]), test_labels_path + "/")

    """ 
    File Structure Should Look Like This Now:
    
    data/
    ├─ images/
    |  ├─ all/
    |  |  ├─ ** ALL IMAGES **
    |  ├─ train/
    |  |  ├─ ** ALL TRAIN IMAGES **
    |  ├─ val/
    |  |  ├─ ** ALL VAL IMAGES **
    |  ├─ test/
    |  |  ├─ ** ALL VAL IMAGES **
    ├─ labels/
    |  ├─ all/
    |  |  ├─ ** ALL TXT ANNOTATIONS **
    |  ├─ train/
    |  |  ├─ ** ALL TRAIN TXT ANNOTATIONS **
    |  ├─ val/
    |  |  ├─ ** ALL VAL TXT ANNOTATIONS **
    |  ├─ test/
    |  |  ├─ ** ALL VAL TXT ANNOTATIONS **
    ├─ dataset.yaml
    """

    return

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate train, val, and test splits for a YOLOv5 dataset")    
    parser.add_argument('--data', type=str, default="../data/YOLOv5_CrowdHuman/")
    parser.add_argument('--val-split', type=float, default=0.1)
    parser.add_argument('--test-split', type=float, default=0.2)

    args = parser.parse_args()

    generate_dataset_split(args.data, args.val_split, args.test_split)