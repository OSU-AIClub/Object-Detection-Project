# ========================================#
#                train.sh                 #
#                                         #
#  Runs training script for YOLOv5 model  #
# =========================================

# TRAINING PARAMETERS
DATASET_CONFIG_FILE=crowd_human.yaml
YOLO_MODEL=yolov5s  # yolov5n, yolov5s, yolov5m, yolov5l, or yolov5x
EPOCHS=6
VAL_BBOX=true   # stores inference on all of val set to WANDB
BBOX_INTERVAL=3 # freequency of VAL_BBOX
CREATE_SPLIT=true   # creates new train, val, test splits

# IF CREATE_SPLIT
if [ CREATE_SPLIT ]
then
    python ../lib/dataset_spilt.py --data ../data/YOLOv5_CrowdHuman/ --val-split 0.1 --test-split 0.2
fi

# RUN TRAIN
if [ VAL_BBOX ]
then
    python ../yolov5/train.py --data ../config/$DATASET_CONFIG_FILE --cfg ../yolov5/models/$YOLO_MODEL.yaml --weights ../models/pretrained/$YOLO_MODEL.pt --batch -1 --epochs $EPOCHS --save-period 1 --bbox_interval $BBOX_INTERVAL
else     
    python ../yolov5/train.py --data ../config/$DATASET_CONFIG_FILE --cfg ../yolov5/models/$YOLO_MODEL.yaml --weights ../models/pretrained/$YOLO_MODEL.pt --batch -1 --epochs $EPOCHS --save-period 1
fi