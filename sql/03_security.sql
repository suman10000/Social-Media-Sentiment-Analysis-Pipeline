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