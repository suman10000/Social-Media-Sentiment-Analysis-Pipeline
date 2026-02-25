DELETE FROM fact_sentiment
WHERE sentiment_label = 'Neutral';

SELECT COUNT(*) FROM fact_sentiment;

SELECT COUNT(*) 
FROM fact_sentiment 
AT (OFFSET => -60*5);

SHOW GRANTS TO ROLE ACCOUNTADMIN;
SHOW ROLES;
USE ROLE SECURITYADMIN;
CREATE ROLE analyst_role;
SHOW ROLES;

USE ROLE ACCOUNTADMIN;

CREATE OR REPLACE SECURE VIEW dim_user_masked AS
SELECT 
    user_id,
    CASE 
        WHEN CURRENT_ROLE() IN ('SYSADMIN','ACCOUNTADMIN')
        THEN user
        ELSE 'REDACTED'
    END AS user
FROM dim_user;

USE ROLE SYSADMIN;
SELECT * FROM dim_user_masked;


--for semi structured 

CREATE OR REPLACE TABLE tweet_raw_json (
    id STRING,
    tweet_data VARIANT
);

INSERT INTO tweet_raw_json (id, tweet_data)
SELECT
    '1',
    PARSE_JSON('{
        "user": "john_doe",
        "location": "Mumbai",
        "device": "Android",
        "hashtags": ["#AI", "#BigData"],
        "engagement": {
            "likes": 120,
            "retweets": 45
        }
    }');

SELECT
    tweet_data:user::STRING AS user_name,
    tweet_data:location::STRING AS location,
    tweet_data:engagement.likes::INTEGER AS likes,
    tweet_data:hashtags[0]::STRING AS first_hashtag
FROM tweet_raw_json;