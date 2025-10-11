# Data Transformation
from abc import ABC, abstractmethod

# Import libraries for data cleaning
import numpy as np 
import pandas as pd 
import os 

# Implement abstract class DataTransformer
class DataTransformer(ABC):
    # Initialise datasets
    def __init__(self, dataset1: pd.DataFrame, dataset2: pd.DataFrame):
        self.dataset1 = dataset1
        self.dataset2 = dataset2

    # Abstract Tranform Method: combingin different dataset
    @abstractmethod
    def combine(self, feature1: str, feature2: str) -> pd.DataFrame:
        # Initialise feature dataframe
        # Check the numbers of rows for each dataset
        # Combine dataset row-wisely -> combine_method is row-wised
        # Combine dataset column-wisely -> combine_method is column-wised
        pass 

    # Abstract Transform Method: transform 
    @abstractmethod
    def transform(self) -> pd.DataFrame:
        # Contains all possible transformation
        pass 

# Implement class StatTransformer
class StatTransformer(DataTransformer):
    # Initialise datasets
    def __init__(self, dataset1: pd.DataFrame, dataset2: pd.DataFrame):
        self.dataset1 = dataset1
        self.dataset2 = dataset2

    # Transformer method
    def combine(self, feature1: str, feature2:str) -> pd.DataFrame:
        # Initialise feature dataframe
        feature_df1 = self.dataset1[feature1]
        feature_df2 = self.dataset2[feature2]

        # Check the numbers of rows for each dataset
        
        # Combine dataset row-wisely -> combine_method is row-wised
        # Combine dataset column-wisely -> combine_method is column-wised

    # Transformer method 2: transform null values into 
    def transform(self):
        # Create a new dataframe
        transformed_df = pd.DataFrame()
        
        # transform data into: nullvalues, data types and number of unique values 
        transformed_df["Nullvalues"] = self.dataset1.isnull().sum()
        transformed_df["DataTypes"] = self.dataset1.dtypes
        transformed_df["UniqueVals"] = self.dataset1.nunique()

        return transformed_df

# Example code 
if __name__ == "__main__":
    pass 