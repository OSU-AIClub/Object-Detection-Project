from datetime import datetime

import pandas as pd

from config import HISTORY_FREQUENCY, HISTORY_WINDOW


def create_history_df():
    cols = ['Time', 'People Detected']
    df = pd.DataFrame(columns= cols)

    return df
    

def add_to_history(df, n_detected):
    curr_time = datetime.now()

    for index, row in df.iterrows():
        if (curr_time - row['Time']).total_seconds() < HISTORY_FREQUENCY:
            return df

    to_drop = []
    for index, row in df.iterrows():
        if (curr_time - row['Time']).total_seconds() > HISTORY_WINDOW:
            to_drop.append(index)
    df = df.drop(to_drop)

    data = {'Time': [curr_time], 'People Detected': [n_detected]}

    df = pd.concat([ df, pd.DataFrame.from_dict(data) ], ignore_index=True)

    return df
