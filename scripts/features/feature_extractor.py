# Feature Extractor script

# Import functionalities for extracting features 
from abc import ABC, abstractmethod

# Import libraries for processing
import numpy as np 
import pandas as pd 

# Implement abstract class Extractor
class Extractor(ABC):
    # Initialize attributes 
    def __init__(self, dataset: pd.DataFrame, feature: str):
        pass

    # Abstract method 1: extract data 
    @abstractmethod
    def extract(self):
        pass 

# Implement abstract class FeatureExtractor
class FeatureExtractor(Extractor):
    # Initialize attributes 
    def __init__(self, dataset: pd.DataFrame, feature: str):
        self.feature_data = dataset[feature]
        self.feature_name = feature
    
    # Method: extract data 
    def extract(self, extracting_value: str) -> pd.DataFrame:
        # Initialise new feature_data & Extract value from selected feature data
        created_feature_df = pd.DataFrame()
        created_feature_df = self.feature_data.apply(lambda text_value: "YES" if extracting_value in text_value else "NO")

        return created_feature_df
    
# Example code 
if __name__ == "__main__":

    # Features values
    feature_values = ["Touchscreen", "Bluetooth", "Wi-Fi(Built-In)", "Webcam", "Microphone", "Display(Built-In)"]