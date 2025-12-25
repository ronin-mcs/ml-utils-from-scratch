from src.io import load_data, save_data
from src.cleaning import clean
from src.features import make_features

df = load_data(path="data/raw/tested.csv")
df_cleaned = clean(df)
df_features = make_features(df_cleaned)
save_data(df_features, "data/clean/tested_clean.csv")
