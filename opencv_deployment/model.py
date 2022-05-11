import torch


def load_pretrained_yolo5():
    return torch.hub.load('ultralytics/yolov5', 'yolov5s', force_reload=True)

def model_inference(model, frame):
    return model(frame).pandas().xyxy[0]

def parse_people_detections(results):
    return results[results["name"].str.contains("person") == True]

def count_frame_detections(results_df):
    return len(results_df.index)
