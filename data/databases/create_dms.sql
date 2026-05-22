-- Create database LaptopSalesDB; 
CREATE DATABASE LaptopSalesDB; 

-- Use database LaptopSalesDB
USE LaptopSalesDB; 

/*	Creating 4 or 5 tables that store all relevant data to ensure data integrity
	- MemoryPerformance: provides storage and memory related data (RAM, Storage, SDD, ROM, etc. )
	- ProcessorDetails: provides processor details (CPU, Clockspeed, etc. )
	- LaptopMetadata: contains descriptive information about laptops (brand, price, color, etc. )
	- HardwareComponents: containing all physical hardware items (I/O components, processor
	- GraphicDetails: containing all visual multimedia components (screen, resolution, etc. )

*/

-- Create a ProcessorDetails table
CREATE TABLE ProcessorDetails (
	ProcessorID VARCHAR(10) PRIMARY KEY, 
	ProcessorName VARCHAR(50),
	ProcessorSpeed DECIMAL(3,1) CHECK (ProcessorSpeed > 0.0),
	ProcessorSpeedUnit VARCHAR(10) CHECK (ProcessorSpeedUnit in ('GHz', 'MHz'))
);

-- Create a LaptopMetadata table 
CREATE TABLE LaptopMetadata (
	INFO_ID VARCHAR(5) PRIMARY KEY,
	BRAND VARCHAR(20),
	COLOR VARCHAR(20),
	CONDITIONS VARCHAR(50),
	PRICE DECIMAL(10,2)
);

-- Manage tables and database (if necessary)
SELECT * FROM [dbo].[ProcessorDetails];
SELECT * FROM [dbo].[LaptopMetadata]; 

DROP TABLE [dbo].[ProcessorDetails];
DROP TABLE [dbo].[LaptopMetadata]; 

