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
        self.project_path = "C:\Development\Projects\MachineLearning\Laptop-Price-Predictor-System\data"
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
    


# Main space: Example code
if __name__ == "__main__":
    # Initialise variables to select a file from a folder 
    data_folder = "data"
    laptop_ds_file = "ebay_laptop_ds.csv"

    # Build a DataLoader class 
    dataloader = DataLoader(laptop_ds_file, data_folder)
    dataset = dataloader.load()

    print(dataset)