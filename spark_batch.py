from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count


spark = SparkSession.builder \
    .appName("Sentiment Batch Processing") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read.csv("processed_data.csv", header=True, inferSchema=True)

sentiment_counts = df.groupBy("sentiment_label").agg(
    count("*").alias("total_count")
)

print("\nSentiment Distribution:")
sentiment_counts.show()

daily_avg = df.groupBy("date").agg(
    avg("sentiment_score").alias("avg_sentiment")
)

print("\nDaily Average Sentiment:")
daily_avg.show()

platform_counts = df.groupBy("platform").agg(
    count("*").alias("total_count")
)

print("\nPlatform Distribution:")
platform_counts.show()

spark.stop()