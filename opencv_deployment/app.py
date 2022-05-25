import tkinter as tk
import cv2
from PIL import Image, ImageTk
import numpy as np

from display import display_detections_count
from model import load_pretrained_yolo5, model_inference, parse_people_detections, count_frame_detections
from stable_detections import create_detection_df, add_detection, average_detections
from detection_history import create_history_df, add_to_history
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import time

PLOT_FREQUENCY = True


last_plotted = time.time()


width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Uncomment to Evaluate on Images from Video
# cap = cv2.VideoCapture("stock_video.mp4")

model = load_pretrained_yolo5()

moving_avg_df = create_detection_df()
history_df = create_history_df()

root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root)
lmain.pack()


def show_frame():
    global moving_avg_df
    global history_df
    global last_plotted
    
    # Grab the current state of video (frame)
    _, frame = cap.read()

    if frame is None:
        exit()

    # Make detections 
    results = model_inference(model, frame)

    # Filter out Non People Detections and Store as Pandas Dataframe
    results = parse_people_detections(results)

    # Log Detections
    moving_avg_df = add_detection(moving_avg_df, count_frame_detections(results))
    history_df = add_to_history(history_df, average_detections(moving_avg_df))

    # Draw Detections and Display Count
    frame = display_detections_count(frame, results, moving_avg_df)
    
    if PLOT_FREQUENCY and time.time() - last_plotted > 1:
        """ Updates the frequency graph """
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
    
    # Stack Both Images on Top of Eachother
    cv2image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    image = cv2.imread('freqency_graph.png')
    cv2image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    cv2image2 = cv2.resize(cv2image2, dsize=(cv2image1.shape[1], cv2image1.shape[0]), interpolation=cv2.INTER_AREA)

    cv2image = np.vstack((cv2image1, cv2image2))

    # Draw both Images to the Frame
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
    
if __name__ == '__main__':
    show_frame()
    root.mainloop()