import pandas as pd

DATA_PATH = "data/raw/tested.csv"


def load_data(path=DATA_PATH):
    return pd.read_csv(path)


def save_data(df, path):
    df.to_csv(path, index=False)
