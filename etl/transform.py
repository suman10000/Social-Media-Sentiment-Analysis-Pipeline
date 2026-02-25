import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def clean_text(text):
    text = str(text)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"[^A-Za-z0-9 ]+", "", text)
    return text.lower()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.05:
        label = "Positive"
    elif score <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"

    return score, label

def transform_data(df: pd.DataFrame) -> pd.DataFrame:

    print("Transforming data...")

    df["clean_text"] = df["text"].apply(clean_text)

    df[["sentiment_score", "sentiment_label"]] = df["clean_text"].apply(
        lambda x: pd.Series(get_sentiment(x))
    )

    df["platform"] = "Twitter"
    df["location"] = "India"

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    print("Transformation Completed.")

    return df