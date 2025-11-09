/* Check and Import Tables */
/* Select database */
USE LAPTOP_RAW_DB;

/* Select tables: categorical_properties, complex_properties, numerical_properties */
SELECT * FROM CATEGORICAL_PROPERTIES;

/* Data Analysis: CATEGORICAL PROPERTIES */
/* Number brand names grouped by brand */
SELECT BRAND, COUNT(BRAND) AS NUM_BRAND FROM CATEGORICAL_PROPERTIES
GROUP BY BRAND ORDER BY BRAND;

/*Number of rows in a dataset*/
SELECT COUNT(*) AS TOTAL_SAMPLES FROM CATEGORICAL_PROPERTIES; -- 4182
