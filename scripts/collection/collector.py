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
    def __init__(self, folder: str):
        self.project_path = "C:\Development\Projects\MachineLearning\Laptop-Price-Predictor-System\data"
        self.filename_list = []
        self.folder_path = os.path.join(self.project_path, folder)

    # Method: load the dataset
    def load(self, filename: str) -> pd.DataFrame:
        # Prepare the path string of the filename in combination wtih the selected folder 
        file = os.path.join(self.folder_path, filename)
        self.filename_list.append(filename)

        # check if folder exist
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path, exist_ok=True)
        
        # check if file contains extension .csv
        if file.endswith(".csv"):
            print("File accepted")
        else:
            raise FileNotFoundError(f"File is not accepted/missing an extension. File {file} is not a csv file")

        # Load the dataset
        dataset = pd.read_csv(file, index_col=0)
        return dataset
    
    # Method 2: reload the extisting filename
    def reload(self, exist_filename: str): 
        # check if filename exist in the filename list
        if exist_filename in self.filename_list:
            existed_file = os.path.join(self.folder_path, exist_filename)
            dataset = pd.read_csv(existed_file, index_col=0)
        else: 
            raise FileNotFoundError("Filename not recognised by the loader. Please specify the name of the file.")
        
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