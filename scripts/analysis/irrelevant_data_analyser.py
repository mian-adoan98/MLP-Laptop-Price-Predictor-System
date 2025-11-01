## Irrelevant Data Analyser 

# Import fuctionalities to build abstract class 
from abc import ABC, abstractmethod

# Import libraries 
import numpy as np 
import pandas as pd 
import os 


# Implement abstract class IRD_Inspector 
class IRD_Inspector(ABC):
    # Initialise attributes 
    def __init__(self, dataset):
        self.dataset = dataset

    # Method 1: Inspect number of nullvalues 
    @abstractmethod
    def inspect(self, feature:str) -> pd.DataFrame:
        pass 

# Implement class NullInspector
class NullInspector(ABC): 
    # Initialise attributes 
    def __init__(self, dataset):
        self.dataset = dataset
        self.null_counts = 0

    # Method 1: Inspect number of nullvalues 
    def inspect(self) -> pd.DataFrame:
        # Create a dataframe 
        null_df = pd.DataFrame()

        # Check if data contains nullvalues and how many nullvalues are there 
        null_count_list = []
        for feature in self.dataset.columns: 
            # Analyse number of nullvalues 
            feature_data = self.dataset[feature].values 

            nullval_checks = pd.isnull(feature_data)
            nullval_count = nullval_checks.sum()

            # Store count in nullvalue count list
            null_count_list.append(nullval_count)
        
        # Add nullvalue count list into null_df dataframe
        column_names = [column for column in self.dataset.columns]
        null_df["Features"] = column_names
        null_df["Nullvalues"] = null_count_list

        return null_df
    
# Implement InconInspector 
class InconInspector(ABC): 
    # Initialise attributes to find inconsistencies 
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset
        self.incon_counts = 0

    # Method 1: detect inconsistent values 
    def inspect(self) -> pd.DataFrame:
        # Create an inconsistent dataframe 
        incon_df = pd.DataFrame()  
        incons_list = []

        # Iteration 1: loop all existing features 
        for feature in self.dataset.columns: 
            # Extract feature from dataset 
            feature_arr = self.dataset[feature].values
            
            # detect inconsistencies for each feature 
            incon_arr = self.detect(feature_arr)
            self.incon_count = incon_arr.shape[-1] 
            incons_list.append(self.incon_count)

        # Convert arrays into dataset
        incon_df["Features"] = [feature for feature in self.dataset.columns]
        incon_df["Inconsistencies"] = incons_list

        return incon_df
        # return incons_list (correction/testing)
    
    # Method 2: detect inconsistent data for one feature 
    def detect(self, feature_arr: np.ndarray) -> list: 
        # Detect inconsistent data
        incons_list = []
        real_list = []
        
        # Iteration 2: loop all existing values (including inconsistent values)
        for feature_value in feature_arr:
            try:
                # Check if value is numeric
                checked_value = float(feature_value)
                real_list.append(checked_value)

            except ValueError:
                # Store inconsistencies into list 
                incon_value = feature_value
                incons_list.append(incon_value) 
                incon_arr = np.array(incons_list)
        
        return incon_arr 
    
# Example Code 
if __name__ == "__main__": 
    pass 
        