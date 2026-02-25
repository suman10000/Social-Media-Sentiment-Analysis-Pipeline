from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

spark = SparkSession.builder \
    .appName("SentimentStreaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")


stream_df = spark.readStream \
    .format("rate") \
    .option("rowsPerSecond", 5) \
    .load()


simulated_stream = stream_df.select(
    expr("CASE WHEN value % 3 = 0 THEN 'Positive' "
         "WHEN value % 3 = 1 THEN 'Negative' "
         "ELSE 'Neutral' END AS sentiment_label")
)


sentiment_counts = simulated_stream.groupBy("sentiment_label").count()


query = sentiment_counts.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()