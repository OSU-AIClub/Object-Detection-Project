import cv2

from stable_detections import average_detections


from config import COUNT_COLOR, BBOX_COLOR, CONFIDENCE_COLOR, FONT, FONT_SIZE, TEXT_THICKNESS

def display_count(image, count):
    width = image.shape[1]
    text = f"Count: {count}"
    color = COUNT_COLOR
    location = (width - 80, 20)
    cv2.putText(image, text, location, FONT, FONT_SIZE, color, TEXT_THICKNESS, cv2.LINE_AA)

    return image


def display_detections(image, results_df):
    for _, row in results_df.iterrows():
        if row['confidence'] > 0.5:
            top_left = (int(row['xmin']), int(row['ymin']))
            bottom_right = (int(row['xmax']), int(row['ymax']))
            image = cv2.rectangle(image, top_left, bottom_right, BBOX_COLOR, thickness=2)
            detect_str = "{:.8f}".format(row['confidence'])
            cv2.putText(image, detect_str, top_left, FONT, FONT_SIZE, CONFIDENCE_COLOR, TEXT_THICKNESS, cv2.LINE_AA)
    
    return image


def display_detections_count(image, results, detections_df):
    image = display_detections(image, results)

    count = average_detections(detections_df)
    image = display_count(image, count)

    return image
