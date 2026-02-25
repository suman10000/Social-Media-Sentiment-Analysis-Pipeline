import pandas as pd
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


column_names = ["target", "id", "date", "flag", "user", "text"]

df = pd.read_csv(
    "training.1600000.processed.noemoticon.csv",
    encoding="latin-1",
    names=column_names
)

print("Data Loaded Successfully")
print(df.head())


def clean_text(text):
    text = str(text)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"[^A-Za-z0-9 ]+", "", text)
    return text.lower()

df["clean_text"] = df["text"].apply(clean_text)


analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        label = "Positive"
    elif score <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"
    return score, label

df[["sentiment_score", "sentiment_label"]] = df["clean_text"].apply(
    lambda x: pd.Series(get_sentiment(x))
)


df["platform"] = "Twitter"
df["location"] = "India"


df["date"] = pd.to_datetime(df["date"], errors="coerce")


df.to_csv("processed_data.csv", index=False)

print("ETL Completed Successfully.")