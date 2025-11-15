/* CHECKUP ALL DATA ARE LOADED AND PROCESSED */

/*Select the database for further investigation*/
USE LAPTOP_RAW_DB;
/**Check if all datasets are imported propertly**/
SELECT * FROM NUMERICAL_PROPERTIES;
SELECT * FROM CATEGORICAL_PROPERTIES;

/*Check all records that have been registered properly*/
SELECT * FROM NUMERICAL_PROPERTIES ORDER BY LAPTOP_ID DESC; # 4182
SELECT * FROM CATEGORICAL_PROPERTIES ORDER BY LAPTOP_ID DESC; # 4182

/*Drop datasets if not all records have been registered correctly*/
DROP TABLE NUMERICAL_PROPERTIES; 
DROP TABLE CATEGORICAL_PROPERTIES;