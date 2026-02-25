--Here we need to do a Basic Join Test (Sanity Check)
SELECT 
    u.user,
    d.date,
    f.sentiment_label,
    f.sentiment_score
FROM fact_sentiment f
JOIN dim_user u ON f.user_id = u.user_id
JOIN dim_date d ON f.date_id = d.date_id
LIMIT 10;

--Here we are doing a CTE Example (Sentiment Distribution Per Day)
WITH daily_sentiment AS (
    SELECT 
        d.date,
        f.sentiment_label,
        COUNT(*) AS total_count
    FROM fact_sentiment f
    JOIN dim_date d ON f.date_id = d.date_id
    GROUP BY d.date, f.sentiment_label
)
SELECT *
FROM daily_sentiment
ORDER BY date;

--Now we do a Window Function Example (Top 5 Most Negative Days)
WITH negative_counts AS (
    SELECT 
        d.date,
        COUNT(*) AS negative_count
    FROM fact_sentiment f
    JOIN dim_date d ON f.date_id = d.date_id
    WHERE f.sentiment_label = 'Negative'
    GROUP BY d.date
)
SELECT *
FROM (
    SELECT *,
           RANK() OVER (ORDER BY negative_count DESC) AS rank_position
    FROM negative_counts
)
WHERE rank_position <= 5;

--Here we perform a Rolling Sentiment Trend (Window Function Advanced)
SELECT 
    d.date,
    AVG(f.sentiment_score) AS daily_avg_score,
    AVG(AVG(f.sentiment_score)) 
        OVER (ORDER BY d.date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
        AS rolling_7_day_avg
FROM fact_sentiment f
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY d.date
ORDER BY d.date;

-- Now we apply Clustering
ALTER TABLE fact_sentiment 
CLUSTER BY (date_id, sentiment_label);

--Verification of Clustering
SELECT SYSTEM$CLUSTERING_INFORMATION('fact_sentiment');