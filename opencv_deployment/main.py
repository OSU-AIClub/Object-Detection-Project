import cv2

from display import display_detections_count
from model import load_pretrained_yolo5, model_inference, parse_people_detections, count_frame_detections
from stable_detections import create_detection_df, add_detection


WINDOW_TITLE = 'People Detection'


if __name__ == '__main__':
    # Load prebuilt model (YOLO5)
    model = load_pretrained_yolo5()

    # Evaluate on live images from camera 
    cap = cv2.VideoCapture(0)
    moving_avg_df = create_detection_df()

    while cap.isOpened():

        # Grab the current state of video (frame)
        _, frame = cap.read()

        # Make detections 
        results = model_inference(model, frame)

        # Filter out Non People Detections and Store as Pandas Dataframe
        results = parse_people_detections(results)

        # Log Detections
        moving_avg_df = add_detection(moving_avg_df, count_frame_detections(results))

        # Draw Detections and Display Count
        image = display_detections_count(frame, results, moving_avg_df)

        cv2.imshow(WINDOW_TITLE, image)

        # End on 'q' button press
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
