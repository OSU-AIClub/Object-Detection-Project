import time

import pandas as pd


AVERAGE_WINDOW = 10     # in seconds


def create_detection_df():
    cols = ['time', 'n_detected']
    df = pd.DataFrame(columns= cols)

    return df
    

def add_detection(df, n_detected):
    curr_time = time.time()

    to_drop = []
    for index, row in df.iterrows():
        if curr_time - row['time'] > AVERAGE_WINDOW:
            to_drop.append(index)
    df = df.drop(to_drop)

    data = {'time': [curr_time], 'n_detected': [n_detected]}

    df = pd.concat([ df, pd.DataFrame.from_dict(data) ], ignore_index=True)

    return df


def average_detections(df):
    mean_detected = df['n_detected'].mean()

    print(f"{round(mean_detected)}: {mean_detected}")

    return round(mean_detected)
