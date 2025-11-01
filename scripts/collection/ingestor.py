# Data Ingestion
from abc import ABC, abstractmethod

# Import libraries for ingesting dataset
import pandas as pd 
import numpy as np 
import os, sys

# Implement Data Ingestor class 
class Ingestor(ABC):
    # Intialise variables: ingesting daa
    def __init__(self, folder, filename):
        self.path = "C:\Development\Projects\MachineLearning\Laptop-Price-Predictor-System\data"
        self.source_folder = os.path.join(self.path, folder)
        self.source_filename = filename

    # Method 1: Load the data
    @abstractmethod
    def load_data(self, format:str) -> pd.DataFrame:
        pass 

    # Method 2: Validate the data
    @abstractmethod
    def validate_data(self):
        pass 

    # Method: Ingest data from selected folder 
    @abstractmethod
    def ingest(self):
        pass 

# Implement FileIngestor
class FileIngestor(Ingestor):
    # Method 1: Load the data 
    def load_data(self, format:str) -> pd.DataFrame:
        # Check the format of dataset
        if format == ".csv" and self.source_filename.endswith(format):
            csv_file = os.path.join(self.source_folder, f"{self.source_filename}.{format}")
            dataset = pd.read_csv(csv_file)
        elif format == ".sql" and self.source_filename.endswith(format):
            database = 
        # load the dataset



# Examples code 
if __name__ == "__main__":
    pass 