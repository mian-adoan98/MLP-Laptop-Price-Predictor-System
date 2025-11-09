/* CHECKUP ALL DATA ARE LOADED AND PROCESSED */

/*Select the database for further investigation*/
USE LAPTOP_RAW_DB;
/**Check if all datasets are imported propertly**/
SELECT * FROM NUMERICAL_PROPERTIES;
SELECT * FROM COMPLEX_PROPERTIES;
SELECT * FROM CATEGORICAL_PROPERTIES;

/*Check all records that have been registered properly*/

/*Drop datasets if not all records have been registered correctly*/
DROP TABLE NUMERICAL_PROPERTIES;
