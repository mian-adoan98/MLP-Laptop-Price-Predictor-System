# Laptop Price Database: Data Management Procedure

-- Create a database for storing all laptop price datasets
CREATE DATABASE LAPTOP_RAW_DB;

-- Use Laptop_db database
USE LAPTOP_RAW_DB;

/*
Creating tables for managing laptop price datasets, are: 
	- Numerical Table: contain all numerical raw feature data including null values, inconsistencies, etc. 
    - Categorical Table: contain all categorical raw feature data with duplicates, null values, etc. 
    - Complex Table: contain all features with multiple different values essential for feature extraction
*/

-- Table 1: NUMERICAL PROPERTIES
CREATE TABLE NUMERICAL_PROPERTIES (
	LAPTOP_ID INT PRIMARY KEY AUTO_INCREMENT,
    PRICE DOUBLE,
    WIDTH_DISPLAY INT,
    HEIGHT_DISPLAY INT,
    HARD_DRIVE INT,
    SSD_CAPACITY INT,
    RAM_SIZE INT,
    PROCESSOR_SPEED INT
);
SELECT * FROM NUMERICAL_PROPERTIES;

-- Table 2: CATEGORICAL PROPERTIES
CREATE TABLE CATEGORICAL_PROPERTIES(
	LAPTOP_ID INT PRIMARY KEY AUTO_INCREMENT,
    BRAND VARCHAR(10),
    CURRENCY TEXT,
    COLOR TEXT,
    CONDITIONS VARCHAR(225),
    GPU VARCHAR(225),
    PROCESSOR VARCHAR(225),
    PROCESSOR_SPEED VARCHAR(225),
    PROCESSOR_SPEED_UNIT TEXT,
    LAPTOP_TYPE TEXT,
    OPERATING_SYSTEM VARCHAR(225),
    STORAGE_TYPE VARCHAR(10),
    HARD_DRIVE_CAPACITY_UNIT VARCHAR(10),
    SSD_CAPACITY_UNIT VARCHAR(225),
    SCREEN_SIZE_INCH VARCHAR(225),
    RAM_SIZE_UNIT VARCHAR(225)
);
SELECT * FROM CATEGORICAL_PROPERTIES;

-- Table 3: COMPLEX PROPERTIES
CREATE TABLE COMPLEX_PROPERTIES(
	LAPTOP_ID INT PRIMARY KEY AUTO_INCREMENT,
    FEATURES TEXT,
    CONDITION_DESCR TEXT,
    SELLER_NOTES TEXT
);
SELECT * FROM COMPLEX_PROPERTIES;

/* *** Deleting and databases and tables in purpose of effective data management *** */
-- Delete database (if necessary)
DROP DATABASE LAPTOP_RAW_DB; 

-- Delete tables (if necessary)
DROP TABLE NUMERICAL_PROPERTIES;
DROP TABLE CATEGORICAL_PROPERTIES;
DROP TABLE COMPLEX_PROPERTIES;