# Data Ingestion
from abc import ABC, abstractmethod

# Import libraries for ingesting dataset
import pandas as pd 
import numpy as np 
import os, sys

# Variables
project_path = "C:\Development\Projects\MachineLearning\Laptop-Price-Predictor-System\data"

# Implement Data Ingestor class 
class Ingestor(ABC):
    # Intialise variables: ingesting daa
    def __init__(self, folder, filename):
        self.path = "C:\Development\Projects\MachineLearning\Laptop-Price-Predictor-System\data"
        self.source_folder = os.path.join(self.path, folder)
        self.source_filename = filename

    # Method 1: Validate the data
    @abstractmethod
    def validate_data(self, extension: str):
        pass 

    # Method 2: Ingest data from selected folder 
    @abstractmethod
    def ingest(self):
        pass 

# Implement FileIngestor
class FileIngestor(Ingestor):
    # Intialise variables: ingesting daa
    def __init__(self, folder):
        self.path = "C:\Development\Projects\MachineLearning\Laptop-Price-Predictor-System\data"
        self.source_folder = os.path.join(self.path, folder)

    # Method 1: ingest data
    def ingest(self, filename) -> pd.DataFrame:
        # Extract format of the file
        format = filename.split(".")[-1]

        # Check which file is approved for ingestion
        # Ingesting file with csv-extension & check if the file contains a csv-extension
        if filename.endswith(format):
            csv_file = os.path.join(self.source_folder, filename)
            data = pd.read_csv(csv_file, index_col=0)
        
        # Ingesting file with sql-extension
        elif format == ".sql" and filename.endswith(format):
            sql_name = os.path.join(self.source_folder,filename)
            data = pd.read_sql(sql_name)
     
        # Ingesting file with html-extension
        return data
    
   # Method 2: Validate data
    def validate_data(self, extension: str, filename: str):
        # if filename exist in folder 
        if filename in self.source_folder:
            print(f"File {filename} exists.")
        else:
            print(f"Source file {filename} does not exist. Specify the filename correctly.")
        
        # check filename with correct format
        extensions = [".csv", ".txt", ".sql"]
        file_extension = filename.split(".")[-1]
        if file_extension in extensions:
            print(f"File extions is approved")
        else:
            print(f"File extension disapproved. Specify the file extension correctly")


# Implement class ZipfileIngestor
class ZipFileIngestor(Ingestor):
    pass 


# Examples code 
if __name__ == "__main__":
    pass 