CREATE OR REPLACE TABLE dim_user (
    user_id INTEGER,
    user STRING
);

CREATE OR REPLACE TABLE dim_date (
    date_id INTEGER,
    date DATE,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

CREATE OR REPLACE TABLE dim_platform (
    platform_id INTEGER,
    platform STRING
);

CREATE OR REPLACE TABLE dim_location (
    location_id INTEGER,
    location STRING
);

CREATE OR REPLACE TABLE fact_sentiment (
    user_id INTEGER,
    date_id INTEGER,
    platform_id INTEGER,
    location_id INTEGER,
    sentiment_score FLOAT,
    sentiment_label STRING
);


SELECT COUNT(*) FROM dim_user;
SELECT COUNT(*) FROM dim_date;
SELECT COUNT(*) FROM dim_platform;
SELECT COUNT(*) FROM dim_location;
SELECT COUNT(*) FROM fact_sentiment;