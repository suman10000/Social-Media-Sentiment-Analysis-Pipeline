import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Social Media Sentiment Dashboard",
    layout="wide"
)

st.title("📊 Social Media Sentiment Analysis Dashboard")


@st.cache_data
def load_data():
    df = pd.read_csv("../processed_data.csv")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df

df = load_data()


st.sidebar.header("Filters")

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["date"].min(), df["date"].max()]
)

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=df["sentiment_label"].unique(),
    default=df["sentiment_label"].unique()
)

filtered_df = df[
    (df["date"] >= pd.to_datetime(date_range[0])) &
    (df["date"] <= pd.to_datetime(date_range[1])) &
    (df["sentiment_label"].isin(sentiment_filter))
]


total = len(filtered_df)
positive = len(filtered_df[filtered_df["sentiment_label"] == "Positive"])
negative = len(filtered_df[filtered_df["sentiment_label"] == "Negative"])
neutral = len(filtered_df[filtered_df["sentiment_label"] == "Neutral"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tweets", total)
col2.metric("Positive", positive)
col3.metric("Negative", negative)
col4.metric("Neutral", neutral)

st.divider()


pie_chart = px.pie(
    filtered_df,
    names="sentiment_label",
    title="Sentiment Distribution"
)

st.plotly_chart(pie_chart, use_container_width=True)


daily_trend = (
    filtered_df
    .groupby("date")["sentiment_score"]
    .mean()
    .reset_index()
)

line_chart = px.line(
    daily_trend,
    x="date",
    y="sentiment_score",
    title="Daily Average Sentiment Score"
)

st.plotly_chart(line_chart, use_container_width=True)


histogram = px.histogram(
    filtered_df,
    x="sentiment_score",
    nbins=50,
    title="Sentiment Score Distribution"
)

st.plotly_chart(histogram, use_container_width=True)


platform_counts = filtered_df["platform"].value_counts().reset_index()
platform_counts.columns = ["platform", "count"]

platform_chart = px.bar(
    platform_counts,
    x="platform",
    y="count",
    title="Tweets by Platform"
)

st.plotly_chart(platform_chart, use_container_width=True)
