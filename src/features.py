import pandas as pd


def make_features(df_cleaned):
    df_cleaned = pd.get_dummies(
        df_cleaned, columns=["Sex", "Embarked"], drop_first=True
    )
    return df_cleaned
