def generate_dataset_split(dataset_path, train_split: float):
    # delete old train val split 

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