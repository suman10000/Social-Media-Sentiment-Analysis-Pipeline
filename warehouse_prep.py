import pandas as pd


df = pd.read_csv("processed_data.csv")

print("Loaded processed data")


dim_user = df[["user"]].drop_duplicates().reset_index(drop=True)
dim_user["user_id"] = dim_user.index + 1
dim_user = dim_user[["user_id", "user"]]


df["date"] = pd.to_datetime(df["date"], errors="coerce")

dim_date = df[["date"]].drop_duplicates().reset_index(drop=True)
dim_date["date_id"] = dim_date.index + 1
dim_date["year"] = dim_date["date"].dt.year
dim_date["month"] = dim_date["date"].dt.month
dim_date["day"] = dim_date["date"].dt.day
dim_date = dim_date[["date_id", "date", "year", "month", "day"]]


dim_platform = df[["platform"]].drop_duplicates().reset_index(drop=True)
dim_platform["platform_id"] = dim_platform.index + 1
dim_platform = dim_platform[["platform_id", "platform"]]


dim_location = df[["location"]].drop_duplicates().reset_index(drop=True)
dim_location["location_id"] = dim_location.index + 1
dim_location = dim_location[["location_id", "location"]]


fact = df.merge(dim_user, on="user")
fact = fact.merge(dim_date, on="date")
fact = fact.merge(dim_platform, on="platform")
fact = fact.merge(dim_location, on="location")

fact_sentiment = fact[[
    "user_id",
    "date_id",
    "platform_id",
    "location_id",
    "sentiment_score",
    "sentiment_label"
]]


dim_user.to_csv("dim_user.csv", index=False)
dim_date.to_csv("dim_date.csv", index=False)
dim_platform.to_csv("dim_platform.csv", index=False)
dim_location.to_csv("dim_location.csv", index=False)
fact_sentiment.to_csv("fact_sentiment.csv", index=False)

print("Star Schema files created successfully!")