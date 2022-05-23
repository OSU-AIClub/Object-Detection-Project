import cv2

from display import display_detections_count
from model import load_pretrained_yolo5, model_inference, parse_people_detections, count_frame_detections
from stable_detections import create_detection_df, add_detection, average_detections
from detection_history import create_history_df, add_to_history
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import time

WINDOW_TITLE = 'People Detection'
PLOT_FREQUENCY = True

last_plotted = time.time()

if __name__ == '__main__':
    # Load prebuilt model (YOLO5)
    model = load_pretrained_yolo5()

    # Evaluate on live images from camera 
    cap = cv2.VideoCapture("stock_video.mp4")
    # cap = cv2.VideoCapture(0)
    
    
    moving_avg_df = create_detection_df()
    history_df = create_history_df()

    while cap.isOpened():

        # Grab the current state of video (frame)
        _, frame = cap.read()

        # Make detections 
        results = model_inference(model, frame)

        # Filter out Non People Detections and Store as Pandas Dataframe
        results = parse_people_detections(results)

        # Log Detections
        moving_avg_df = add_detection(moving_avg_df, count_frame_detections(results))
        history_df = add_to_history(history_df, average_detections(moving_avg_df))

        # Draw Detections and Display Count
        image = display_detections_count(frame, results, moving_avg_df)

        cv2.imshow(WINDOW_TITLE, image)
        
        if PLOT_FREQUENCY and time.time() - last_plotted > 1:
            last_plotted = time.time()
            plt.clf()
            
            ax = sns.lineplot(data=history_df, x="Time", y="People Detected")
            
            locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
            formatter = mdates.ConciseDateFormatter(locator)
            
            ax.xaxis.set_major_locator(locator)
            ax.xaxis.set_major_formatter(formatter)
            ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
            ax.yaxis.set_major_formatter(ticker.ScalarFormatter())            
            plt.axis([None, None, 0, None])
            plt.savefig("freqency_graph.png")
        
        # End on 'q' button press
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
