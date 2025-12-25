import pandas as pd


def clean(df_cleaned):
    # Чистим вилкой
    df_cleaned = df_cleaned.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])
    df_cleaned = df_cleaned.fillna(
        {
            "Age": df_cleaned["Age"].median(),
            "Embarked": df_cleaned["Embarked"].mode()[0],
        }
    )
    df_cleaned = df_cleaned.dropna(subset=["Fare"])
    return df_cleaned
