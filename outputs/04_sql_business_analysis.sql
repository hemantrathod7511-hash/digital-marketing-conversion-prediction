CREATE DATABASE marketing_campaign_db;


USE marketing_campaign_db;

SHOW TABLES;

SELECT COUNT(*) AS total_customers
FROM campaigns;

DESCRIBE campaigns;

SELECT *
FROM campaigns
LIMIT 5;

SELECT
    Conversion,
    COUNT(*) AS customers
FROM campaigns
GROUP BY Conversion
ORDER BY Conversion;


SELECT
    CampaignChannel,
    COUNT(*) AS customers,
    SUM(Conversion) AS conversions,
    ROUND(AVG(Conversion) * 100, 2) AS conversion_rate_pct
FROM campaigns
GROUP BY CampaignChannel
ORDER BY conversion_rate_pct DESC;


SELECT
    CampaignType,
    COUNT(*) AS customers,
    SUM(Conversion) AS conversions,
    ROUND(SUM(AdSpend), 2) AS total_ad_spend,
    ROUND(
        SUM(AdSpend) / NULLIF(SUM(Conversion), 0),
        2
    ) AS cost_per_conversion
FROM campaigns
GROUP BY CampaignType
ORDER BY cost_per_conversion ASC;



SELECT
    CASE
        WHEN Age < 25 THEN '18-24'
        WHEN Age < 35 THEN '25-34'
        WHEN Age < 45 THEN '35-44'
        WHEN Age < 55 THEN '45-54'
        ELSE '55+'
    END AS age_band,
    COUNT(*) AS customers,
    SUM(Conversion) AS conversions,
    ROUND(AVG(Conversion) * 100, 2) AS conversion_rate_pct
FROM campaigns
GROUP BY age_band
ORDER BY
    CASE
        WHEN age_band = '18-24' THEN 1
        WHEN age_band = '25-34' THEN 2
        WHEN age_band = '35-44' THEN 3
        WHEN age_band = '45-54' THEN 4
        ELSE 5
    END;
    
    
    

SELECT
    CampaignChannel,
    COUNT(*) AS customers,
    ROUND(SUM(AdSpend), 2) AS total_ad_spend,
    SUM(Conversion) AS conversions,
    ROUND(AVG(Conversion) * 100, 2) AS conversion_rate_pct,
    ROUND(
        SUM(AdSpend) / NULLIF(SUM(Conversion), 0),
        2
    ) AS cost_per_conversion
FROM campaigns
GROUP BY CampaignChannel
ORDER BY cost_per_conversion ASC;