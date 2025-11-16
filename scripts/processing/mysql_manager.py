# MySQL Manager
from abc import ABC, abstractmethod

# Import libraries for data cleaning
import numpy as np 
import pandas as pd 
import os 


# Implement abstract class Processor
class Processor(ABC):
    # Initialise dataset
    def __init__(self, full_dataset: pd.DataFrame):
        self.dataset = full_dataset

    # Method 1: create new features, columns, etc.
    @abstractmethod
    def create(self) -> pd.DataFrame:
        pass 

# Implement class MySQL_ID_Creator
class MySQL_ID_Creator(Processor):
    # Initialise dataset
    def __init__(self, full_dataset: pd.DataFrame):
        super().__init__(full_dataset)
        
    # Method 1: Convert id into dataframe
    def create(self, feature_id: str) -> pd.DataFrame:
        # Initialise dataframe
        feature_id_df = pd.DataFrame()

        # Retrieve IDs
        id_arrays = self.build_id_feature(feature_id)
        feature_id_df[feature_id] = id_arrays

        return feature_id_df
    
    # Implement function: build unique feature id
    def build_id_feature(self, feature: str) -> np.ndarray:
        # Determine prefix
        prefix = feature[:1]
        
        # Number of column records 
        records = self.dataset.shape[0]

        # Build new unique primary key columns
        feature_id = [f"{prefix}{code_id}"for code_id in np.arange(0, records)]
        feature_id_arr = np.array(feature_id)

        return feature_id_arr

# Implement class MySQL_Table_Creator
class MySQL_Table_Creator(Processor):
    # Initialise attributes
    def __init__(self, full_dataset: pd.DataFrame):
        self.full_dataset = full_dataset
        
    # Method 1: Create a table based on input features
    def create(self, features: list) -> pd.DataFrame:
        # Create dataset on given features
        formed_df = self.full_dataset[features]   # constructive dataset by selection 
        return formed_df
    
    # Method: combine id feature data with selected dataset
    def combine(self, feature_id_df: pd.DataFrame, features: str) -> pd.DataFrame:
        # Provide created dataset 
        provided_df = self.create(features)

        # Combine feature id with selected dataset
        combination = [feature_id_df, provided_df]
        combined_df = pd.concat(combination, axis=1)

        return combined_df

# Example code 
if __name__ == "__main__":
    pass 