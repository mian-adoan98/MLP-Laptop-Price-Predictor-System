# Collector: collect data from data sources 

# Implement dependencies to build abstract classes
from abc import ABC, abstractmethod
import os 
# Implement dependencies to build classes to collect data
import numpy as np 
import pandas as pd 
import seaborn as sns 

# Implement DataCollector abstract class
class DataCollector(ABC):
    # Initialise data fields
    def __init__(self, filename: str):
        pass 

    # abstract method:
    @abstractmethod
    def load(self) -> pd.DataFrame:
        pass  

# Implement DataLoader class
class DataLoader(DataCollector):
    # Initialise datafields 
    def __init__(self, filename: str, folder: str):
        self.project_path = "C:\Development\Projects\MachineLearning\Laptop-Price-Predictor-System"
        self.filename = filename
        self.folder_path = os.path.join(self.project_path, folder)
        self.file = os.path.join(self.folder_path, filename)

    # Method: load the dataset
    def load(self) -> pd.DataFrame:
        # check if folder exist
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path, exist_ok=True)
        
        # check if file contains extension .csv
        if self.file.endswith(".csv"):
            print("File accepted")
        else:
            raise FileNotFoundError(f"File is not accepted/missing an extension. File {self.filename} is not a csv file")

        # Load the dataset
        dataset = pd.read_csv(self.file, index_col=0)
        return dataset
    
## Implement DataSaver class
class DataSaver:
    # Initialise DataSaver-attributes
    def __init__(self, folder):
        self.project_path = "C:\Development\Projects\MachineLearning\Laptop-Price-Predictor-System"
        self.folder_path = os.path.join(self.project_path, folder)
        

    # Method 1: saving multiple datasets into a folder 
    def save_multiple_ds(self, data_dict: dict):
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

    # Method 2: saving one single dataset into a folder 
    def save_one_ds(self, dataset: pd.DataFrame, filename: str):
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

# Main space: Example code
if __name__ == "__main__":
    # Initialise variables to select a file from a folder 
    data_folder = "data"
    laptop_ds_file = "ebay_laptop_ds.csv"

    # Build a DataLoader class 
    dataloader = DataLoader(laptop_ds_file, data_folder)
    dataset = dataloader.load()

    print(dataset)