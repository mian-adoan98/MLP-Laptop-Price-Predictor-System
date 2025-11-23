# Feature Selector 
# Import functionalities for selecting  features 
from abc import ABC, abstractmethod

# Import libraries for processing
import numpy as np 
import pandas as pd 
import seaborn as sn 


# Implement abstract class Selector
class Selector(ABC):
    # Initialise attributes 
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset
        self.rows = dataset.shape[0]
        self.columns = dataset.columns.values 

    # Abstract method 1: 
    @abstractmethod
    def select(self, feature_list: list) -> list:
        # Extract feature from the dataset
        # Pass the feature dataset 
        pass 

# Implement class FeatureSelector 
class FeatureSelector(ABC):
    # Initialise attributes 
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset
        self.rows = dataset.shape[0]
        self.columns = dataset.columns.values 

    # Method 1
    def select(self, feature_list: list) -> list:
        # Extract feature from the dataset
        feature_sel_df = self.dataset[feature_list]

        # Pass the feature dataset 
        print(f"Number of features selected: {len(feature_list)}")
        return  feature_sel_df

# Example code 
if __name__ == "__main__":
    pass 
