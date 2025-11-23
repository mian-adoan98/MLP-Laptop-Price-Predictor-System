# Saver: collect data from data sources 

# Implement dependencies to build abstract classes
from abc import ABC, abstractmethod
import os 

# Implement dependencies to build classes to collect data
import numpy as np 
import pandas as pd 
import seaborn as sns 

# Implement functionality 
class DataSaver(ABC):
    # Initialise variables 
    def __init__(self, folder):
        self.project_path = "C:\Development\Projects\MachineLearning\Laptop-Price-Predictor-System"
        self.folder_path = os.path.join(self.project_path, folder)

    # Overloading method
    @abstractmethod
    def save(self, filename: str):
        pass 

## Implement DataSaver class
class OneFileSaver(DataSaver):
    # Initialise DataSaver-attributes
    def __init__(self, folder):
        self.project_path = "C:\Development\Projects\MachineLearning\Laptop-Price-Predictor-System"
        self.folder_path = os.path.join(self.project_path, folder)
        
    # Method 2: saving one single dataset into a folder 
    def save(self, dataset: pd.DataFrame, filename: str):
        # Check if folder exists
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        # Save dataset to selected folder 
        # Filename as csv-files
        csv_filename = f"{filename}.csv"

        # Create a file path
        self.file = os.path.join(self.folder_path, csv_filename) 
        dataset.to_csv(self.file)
        print(f"File {csv_filename} has been stored successfully")

## Implement class MultiFileSaver
class MultiFileSaver(DataSaver):
     # Initialise DataSaver-attributes
    def __init__(self, folder):
        self.project_path = "C:\Development\Projects\MachineLearning\Laptop-Price-Predictor-System"
        self.folder_path = os.path.join(self.project_path, folder)

    # Method 1: saving multiple datasets into a folder 
    def save(self, data_dict: dict):
        """data_dict: 
            - Key: filename assinging to the dataset
            - Value: dataset that will be stored"""
        # Check if folder exists
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        # Iteration: save every dataset into the selected path
        file_idx = 0
        for filename, dataset in data_dict.items():
            # Filename as csv-files
            csv_filename = f"{filename}.csv"

            # Create a file path
            self.file = os.path.join(self.folder_path, csv_filename) 
            dataset.to_csv(self.file)
            
            # Display file saving process
            file_idx += 1
            print(f"File {file_idx}: dataset as {filename}.csv --> {self.folder_path} (Saving is successful")

# Example code 
if __name__ == "__main__":
    pass 