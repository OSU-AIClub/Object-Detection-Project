# Object-Detection-Project
The OSU Artificial Intelligence club started this project Winter Term 2022.The goal of this project is to count the amount of people detected by a camera using the YOLOv5 model architecture.

#  Deployment Demo
## Setup
First, move into the deployment directory:
```bash
$ cd ./opencv_deployment/
```

Next, you must install the necessary packages. You can do so using the following command.
```bash
$ pip install -r requirements.txt
```

And now you should be ready!

## Running
If you haven't already, be sure to change into the deployment directory:
```bash
$ cd ./opencv_deployment/
```

Then, run the application:

```bash
$ python app.py
```

Please note that you can modify some of the values in the `config.py` file to change how the frequency of detected persons are logged and other variables:
```python
# Detection History
HISTORY_WINDOW = 60     # in seconds
HISTORY_FREQUENCY = 0.5   # in seconds, the frequency the history is updated + image is changed

# Stable Detections
AVERAGE_WINDOW = 5    # in seconds

# Display
BBOX_COLOR = (255,0,0)              # B, G, R
COUNT_COLOR = (0,0, 255)            # B, G, R
CONFIDENCE_COLOR = (255,255,255)    # B, G, R

FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SIZE = 0.5
TEXT_THICKNESS = 1
```

#  Custom Detection Model
## Setup
First, you must download the Cityscapes dataset. You can download the the dataset using the `donwload_dataset.sh` script:
```bash
$ sh download_dataset.sh
```

Next, you need to install the dependencies, you can install the dependencies using conda with the following command and activate the environment:
```bash
$ conda env create --file ped_detect.yml
$ conda activate ped_detect
```

Next, if you want to use WANDB for tracking the training and evaluating:
```bash
$ pip install wandb
$ wandb login
```

And finally, clone the yolov5 github repo as follows:
```bash
$ git clone https://github.com/ultralytics/yolov5.git
```

And you should be ready!

## Training
Before training, I recommend that you recreate the dataset splits to ensure randomness. You can modify the default split amounts in the code of the python file.
```bash
cd ./lib/
python dataset_split.py
```
**First time running? You must use the above command to create the splits**



Training is simple. Change into the tools directory, and then run the `train.sh` script.

```bash
$ cd tools
$ bash train.sh
```

There are 5 parameters that can be changed in the `train.sh` script:
```bash
DATASET_CONFIG_FILE=crowd_human.yaml # File should be in the config/ directory
YOLO_MODEL=yolov5s  # yolov5n, yolov5s, yolov5m, yolov5l, or yolov5x
EPOCHS=6
VAL_BBOX=true   # stores inference on all of val set to WANDB
BBOX_INTERVAL=3 # epoch freequency of VAL_BBOX
CREATE_SPLIT=true   # creates new train, val, test splits if true
```

# Project Organization
This project is organized as follows:
```
.
├── custom_model/       ** TRAINING OF CUSTOM MODEL HERE **
│   ├── config/
│   │   └── crowd_human.yaml
│   ├── data/
│   ├── download_dataset.sh
│   ├── lib/
│   │   ├── dataset_split.py
│   │   └── __init__.py
│   ├── misc/
│   │   └── ml_tutorials/
│   │       ├── load_data.py
│   │       ├── main.py
│   │       ├── simplecnn.py
│   │       ├── train.py
│   │       └── utils.py
│   ├── models/
│   │   └── pretrained/
│   │       └── yolov5s.pt
│   ├── ped_detect.yml
│   ├── sample_images/
│   │   └── P4-FEB-iStock-1352165307.jpg
│   ├── tools/
│   │   ├── sample_inference.py
│   │   ├── train.sh
│   │   └── wandb/
│   └── yolov5/
├── opencv_deployment/      ** APPLICATION IS HERE **
│   ├── app.py
│   ├── config.py
│   ├── detection_history.py
│   ├── display.py
│   ├── freqency_graph.png
│   ├── main.py
│   ├── model.py
│   ├── stable_detections.py
│   ├── stock_video.mp4
│   └── yolov5s.pt
├── README.md
└── tree.txt
```
