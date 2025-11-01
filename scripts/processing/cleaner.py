# Data Cleaning
from abc import ABC, abstractmethod

# Import libraries for data cleaning
import numpy as np 
import pandas as pd 
import os 

# Implement class Cleaner
class DataCleaner(ABC):
    # Intialise dataset 
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset

    # Abstract Method remove data that are: inconsistent, duplicated, nulls
    @abstractmethod
    def clean(self, feature: str):
        pass 

# Implement Cleaner 
class NullRemover(DataCleaner): 
    # Intialise dataset 
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset

    # Method 1: remove null values data 
    def clean(self, feature: str):
        # Check the datatype
        # Check number of null values
        num_nulls = self.dataset[feature].isnull().sum()
        feature_dtype = self.dataset[feature].dtype

        if feature_dtype == object and num_nulls != 0:
            self.dataset[feature] = self.dataset[feature].fillna("unknown data")

        elif (feature_dtype == int or feature_dtype == float) and num_nulls != 0:
            # Compute number of unique values 
            num_uniques = self.dataset[feature].nunique()

            if num_uniques < 100:
                # Identify median
                median = self.dataset[feature].median()

                # Remove the null values by replacing its mean
                self.dataset[feature] = self.dataset[feature].fillna(median)

            else:
                # Identify median
                mean = self.dataset[feature].mean()

                # Remove the null values by replacing its mean
                self.dataset[feature] = self.dataset[feature].fillna(mean)

# Implement class to remove inconsistencies
class InconRemover(DataCleaner):
    # Intialise dataset 
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset

    # Initialise dataset
    """ For analysing inconsistent data there are several case scenario's to make a distinguish: 
        - scenario 1: features that contains one unique categorical value                   --> inconsistent : detect_duplicates(self)
        - scenario 2: features that supposed to be numeric, but it has special characters   --> inconsistent: detect_incons(self)
        - scenario 3: features that are categorical, but contain data that are not familiar --> inconsistent: ? """
    
    # Methode 1: remove inconsistent data after detection 
    def clean(self, feature: str):
        # Retrieve inconsistent data from detection
        incons_data = self.detect_incon(feature)

        # Iteration: Replace all inconsistent values 
        for incons in incons_data:
            # Replace inconsistent by zero
            self.dataset[feature] = self.dataset[feature].str.replace(incons, "0")

    # Method 2: detect inconsistent data based on given scenario's
    def detect_incon(self, feature: str) -> list:
        # Convert the dataframe to numpy array
        feature_array = self.dataset[feature].to_numpy()
        # Detect inconsistent data
        incons_list = []
        real_list = []

        for feature_value in feature_array:
            try:
                # Check if value is numeric
                checked_value = float()
                real_list.append(checked_value)
            except ValueError:
                # Store inconsistencies into list 
                incon_value = feature_value
                incons_list.append(incon_value)
        # Analyse number of inconsistencies
        num_incons = len(incons_list)
        print(f"Feature {feature}: {num_incons} inconsistent data has been detected.")
        
        return incons_list


# Example code 
if __name__ == "__main__":
    pass 