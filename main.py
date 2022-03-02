import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2


# Load prebuilt model (YOLO5)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')


# Evaluate on live images from camera 
cap = cv2.VideoCapture(0)
while cap.isOpened():
    
    # Grab the current state of video (frame)
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    # End on 'q' button press
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
     
cap.release()
cv2.destroyAllWindows()
