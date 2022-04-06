
python ../yolov5/train.py --data ../config/crowd_human.yaml --cfg ../yolov5/models/yolov5m.yaml --weights ../models/pretrained/yolov5s.pt --batch -1 --epochs 6 --save-period 1 --bbox_interval 3