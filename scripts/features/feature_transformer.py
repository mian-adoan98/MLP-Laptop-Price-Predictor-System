# Feature Selector 
# Import functionalities for selecting  features 
from abc import ABC, abstractmethod

# Import libraries for processing
import numpy as np 
import pandas as pd 
import os 

# Implement abstract class FeatureTransformer
class FeatureTransformer(ABC):
    # Method 1: scaling a feature based on gives properties
    @abstractmethod
    def transform(self): 
        pass 
    
    # Method 2: apply feature scaler on selected dataset
    @abstractmethod
    def apply(self, transformer):
        pass 

# Implement class Normalizer: includes StandardScaler, MinMax, Z_Score
class Normalizer(FeatureTransformer):
    pass 

# Test code environment
# Example code 
if __name__ == "__main__":
    pass 


