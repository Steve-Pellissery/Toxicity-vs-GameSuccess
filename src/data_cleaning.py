import pandas as pd

def clean_reviews(df):
    df = df.dropna(subset=["review"])
    df['review'] = df['review'].astype(str)
    return df

def remove_outliers(df, column, threshold):
    return df[df[column] < threshold]
