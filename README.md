# Object-Detection-Project
The OSU Artificial Intelligence club started this project Winter Term 2022.The goal of this project is to count the amount of people in Kelley Engineering Center using the YOLOv5 model architecture

Current files in the tutorial repository are from: https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html

To run this code simply run the main file with your Python intepretter. 

# Setup
First, you must download the Cityscapes dataset. You can download the the dataset using the `donwload_dataset.sh` script:
```bash
$ sh download_dataset.sh
```

Next, you need to install the dependencies, you can install the dependencies using conda with the following command:
```bash
$ conda env create --file ped_detect.yml
```

And finally, clone the yolov5 github repo as follows:
```bash
$ git clone https://github.com/ultralytics/yolov5.git
```

And you should be all set!

# Project Organization
This project is organized as follows:
```
.
├── config/
│   └── **ALL DATASET CONFIG FILES GO HERE**
├── data/
│   └── YOLOv5_CrowdHuman/
│       └── **DATASET FILES GO HERE**
├── lib/
│   └── **ALL HELPER FILES GO HERE**
├── misc/
│   └── ml_tutorials/ (you can ignore this)
├── models/
│   ├── pretrained/
│   │   └── **ALL PRETRAINED MODELS GO HERE**
│   └── train/
│       └── **ALL TRAINED MODELS GO HERE**
├── sample_images/
│   └── **SAMPLE IMAGES FOR INFERENCE**
├── tools/
│   └── **ALL TRAINING AND TESTING SCRIPTS GO HERE**
├── deployment/
│   └── **ALL OPEN-CV INFERENCE FILES GO HERE**
├── yolov5/
│   └── **CLONED GITHUB REPO GOES HERE**
├── download_dataset.sh
├── ped_detect.yml (conda environment)
├── README.md
└── .gitignore
```