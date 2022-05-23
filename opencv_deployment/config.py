import cv2

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
