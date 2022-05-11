import torch
import numpy as np
import cv2



def removeNonPeople(results):
    results_df = results.pandas().xyxy[0]
    results_df = results_df[results_df["name"].str.contains("person") == True]

    return results_df

def countPeople(results_df):
    return len(results_df.index)

def drawCount(results_df, image):
    count = countPeople(results_df)
    width = image.shape[1]
    text = f"Count: {count}"
    color = (0,0, 255)
    location = (width - 100, 40)
    cv2.putText(image, text, location, cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)

    return image

def display_detections(image, results_df):
    for _, row in results_df.iterrows():
        if row['confidence'] > 0.5:
            top_left = (int(row['xmin']), int(row['ymin']))
            bottom_right = (int(row['xmax']), int(row['ymax']))
            image = cv2.rectangle(image, top_left, bottom_right, (255,0,0), thickness=2)
            detect_str = "{:.6f}".format(row['confidence'])
            cv2.putText(image, detect_str, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
    return image

if __name__ == '__main__':
    # Load prebuilt model (YOLO5)
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', force_reload=True)


    # Evaluate on live images from camera 
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        
        # Grab the current state of video (frame)
        _, frame = cap.read()
        
        # Make detections 
        results = model(frame)
        results_df = removeNonPeople(results)

        count = countPeople(results_df)
        image = display_detections(frame, results_df)
        image = drawCount(results_df, frame)

        cv2.imshow('People Detection', image)
        
        # End on 'q' button press
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
