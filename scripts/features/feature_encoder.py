# Feature Encoding
from abc import ABC, abstractmethod
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Import libraries for building functional encoding algorithms
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import os 

# Implement abstract class Encoder 
class FeatureEncoder(ABC):
    def __init__(self):
        pass 

    # Method 1: Encode feature 
    @abstractmethod
    def encode(self, feature_data: pd.DataFrame, feature: str) -> pd.DataFrame:
        # Identify type of ordering 
        # Find feature data 
        pass 

# Implement class BinaryEncoding
class BinaryEncoder(FeatureEncoder):
    # Method 1: Encode feature 
    def encode(self, feature_data: pd.Series) -> pd.DataFrame:
        # Identify type of ordering 
        # Find feature data 
        feature_arr = feature_data.values
        num_samples = np.unique(feature_arr).shape[0] 

        # Binary feature encoding: process
        if num_samples == 2:
            feature_data = feature_data.apply(lambda x: 1 if x == "YES" else 0)
        else:
            print(f"Feature is not Binary")
        
        return feature_data

    # Method 2: Identify number of distinct values per feature 
    def identify(self, dataset: pd.DataFrame) -> pd.DataFrame:
        dataframe = pd.DataFrame()
        dataframe["Categorical Features"] = dataset.columns.values
        dataframe["Number of Discrete values"] = dataframe["Categorical Features"].apply(lambda feature: dataset[feature].nunique())
        
        return dataframe
    
    # Method 3: Visualise categorical features 
    def visualise(self): 
        pass 

# Implement class OrdinalEncoder
class OrdinalEncoder(FeatureEncoder):
    def __init__(self):
        """!: Need some refining"""
        self.encoded_dataset = pd.DataFrame()

    # Method 1: Encode feature 
    def encode(self, feature_data: pd.DataFrame) -> pd.DataFrame:
        """!: Need some refining: how to combine the actual value with its encoded value
        for example: {0: yellow, 1: orange, etc. }"""
        encoder = LabelEncoder()
        feature_data = encoder.fit_transform(feature_data)

        return feature_data

    # Method 2: Identify number of distinct values per feature 
    def identify(self, dataset: pd.DataFrame) -> pd.DataFrame:
        dataframe = pd.DataFrame()
        dataframe["Categorical Features"] = dataset.columns.values
        dataframe["Number of Discrete values"] = dataframe["Categorical Features"].apply(lambda feature: dataset[feature].nunique())
        
        return dataframe
    
    # Method 3: Visualise categorical features 
    def visualise(self, feature: str, 
                  dataset: pd.DataFrame, 
                  color: str): 
        feature_data = dataset[feature].value_counts().to_frame(name="COUNTS").reset_index()
        labels = [label.upper() for label in feature_data[feature].values]
        counts = feature_data["COUNTS"].values

        plt.figure(figsize=(14,8))
        bars = plt.bar(labels, counts, color=color)

        for bar in bars:
            bar.set_alpha(0.80)

        plt.xlabel(f"{feature}")
        plt.ylabel("COUNTS")
        plt.title(f"Feature Distribution ({feature.capitalize()})")
        plt.show() 

# Implement class NominalEncoder
class NominalEncoder(FeatureEncoder):
    # Method 1: Encode feature 
    def encode(self, feature_data: pd.DataFrame, feature: str) -> pd.DataFrame:
        """
        Params:
        feature_data[pd.DataFrame]:     df with a selected feature
        encoder[object]:                encoder instantiated from OneHotEncoder() class
        reshaped_feature[np.ndarray]:   feature data is being reshaped with (-1,1)
        encoded_feature[np.ndarray]:    feature data is being encoded

        Return: feature dataframe with encoded values
        """
        # Instantiate an object from OneHotEncoder functionality
        encoder = OneHotEncoder()

        # Prepare constants for performing OneHotEncoding
        reshaped_feature = feature_data.values.reshape((-1,1))
        encoded_feature = encoder.fit_transform(reshaped_feature).toarray()
        
        # Build a dataframe that is sparsed matrix: encoded columns and binary values
        feature_data = pd.DataFrame(encoded_feature, columns=encoder.get_feature_names_out([feature]))
        return feature_data 

    # Method 2: Identify number of distinct values per feature 
    def identify(self, dataset: pd.DataFrame) -> pd.DataFrame:
        dataframe = pd.DataFrame()
        dataframe["Categorical Features"] = dataset.columns.values
        dataframe["Number of Discrete values"] = dataframe["Categorical Features"].apply(lambda feature: dataset[feature].nunique())
        
        return dataframe
    
    # Method 3: Visualise categorical features 
    def visualise(self): 
        pass 

# Example code 
if __name__ == "__main__":
    pass 