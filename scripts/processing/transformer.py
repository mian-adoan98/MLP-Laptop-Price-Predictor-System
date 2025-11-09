# Data Transformation
# Import functionalities for building algorithm for data transformation
from abc import ABC, abstractmethod
from scripts.collection.collector import DataLoader

# Import libraries for data cleaning
import numpy as np 
import pandas as pd 
import os 
import sys

# System configuration
sys.path.append(os.path.abspath("../.."))

'''
Data Transformation = a process of manipulating colunms and rows through transformation operations (combining, merging, deleting, etc.).
This script contains 3 à 4 transformation functionalities that eases the process along the way. These functionalities are:
    - DataTransformer: abstract class that build blueprints for other transformer classes
    - StatsTransformer: class that transforms statistical features from 2 given datasets
    - ColumnTransformer: class that transforms, combines and delete one or multiple features from 2 given datasets    '''

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

    # Transformer method: combine maximum 2 features
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

# Implement class ColumnTransformer (combining multiple dataframes)
class ColumnTransformer(DataTransformer):
    # Initialise datasets
    def __init__(self, dataset1: pd.DataFrame, dataset2: pd.DataFrame):
        self.dataset1 = dataset1
        self.dataset2 = dataset2

    # Method 1: combine datasets
    def combine(self) -> pd.DataFrame:
        # Initialise new dataframe
        # combined_df = pd.DataFrame()

        # Combine prepared dataframes into one single dataframe
        container = [self.dataset1, self.dataset2]
        combined_df = pd.concat(container, axis=1)

        return combined_df

    # Method 2: transform datasets
    def transform(self):
        pass 

    # Method 3: delete data series
    def delete(self, feature_list:list, select_data: int):
        # Select type of dataset
        if select_data == 1:
            # Check the feature dimension
            if len(feature_list) == 1:
                # Delete a single feature
                self.dataset1 = self.dataset1.drop(columns=feature_list, axis=1) 
            elif len(feature_list) > 1: 
                # Delete a single feature
                self.dataset1 = self.dataset1.drop(columns=feature_list, axis=1)
        
        elif select_data == 2:
            # Check the feature dimension
            if len(feature_list) == 1:
                # Delete a single feature
                self.dataset1 = self.dataset1.drop(columns=feature_list, axis=1)
            elif len(feature_list) > 1: 
                # Delete a single feature
                self.dataset1 = self.dataset1.drop(columns=feature_list, axis=1)

        else:
            raise ValueError(f"Dataset type {select_data} is unknown. Please Specify the dataset")   
# Example code 
if __name__ == "__main__":
    
    # Intialise datasets
    folder = "data/external"
    filename1 = "Laptop_categorical_data.csv"
    filename2 = "Laptop_numerical_data.csv"
    
    # Initialise data loader
    data_loader1 = DataLoader(filename1, folder)
    data_loader2 = DataLoader(filename2, folder)

    dataset1 = data_loader1.load() # Nuermical dataset
    dataset2 = data_loader2.load()  # Categorical dataset
    
    # Instatiate columnTransformer object 
    column_transformer = ColumnTransformer(dataset1, dataset2[["Processor Speed"]])
    dataset3 = column_transformer.combine()

    print(dataset3) # NOTE: EXECUTION FAILED. PLEASE CHECK