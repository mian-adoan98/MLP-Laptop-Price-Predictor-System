# Models
from abc import ABC, abstractmethod
import os 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# Implement functionalities from scikit-learn
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Implement abstract class: Model
class MLModel(ABC): 
    # Method 1: building a model 
    @abstractmethod
    def build(self, xtrain:pd.DataFrame, ytrain: np.ndarray):
        pass 

    # Method 2: make predictions on actual input data
    @abstractmethod
    def predict(self, ytrain: np.ndarray) -> np.ndarray:
        pass 
    
    # Method 3: evaluating the model performance
    @abstractmethod
    def evaluate(self, ytest: np.ndarray, ypred: np.ndarray):
        pass 

# Implement two classes: RegressModel, ClassModel 
# Implement class model 1: RegressModel
class RegressModel(MLModel):
    def __init__(self, base_model, lr = 0.01):
        self.base_model = base_model
        self.lr = lr 
        self.metrics = {}

    # Method 1: Build a model 
    def build(self, xtrain:pd.DataFrame, ytrain: np.ndarray):
        # Fit the base model 
        self.base_model = self.base_model.fit(xtrain, ytrain)
        return self.base_model 
    
    # Method 2: make predictions on actual input data
    def predict(self, xtest: np.ndarray) -> np.ndarray:
        ypred = self.base_model.predict(xtest)
        return ypred
    
    # Method 3: evaluating the model performance
    def evaluate(self, xtest:pd.DataFrame, ytest: np.ndarray):
        # Retrieve prediction data
        ypred = self.predict(xtest)

        # Compute the metrics for one-parameter regression model
        mae = mean_absolute_error(ytest, ypred)
        mse = mean_squared_error(ytest, ypred)
        r2s = r2_score(ytest, ypred)

        # Store metrics into dictionary
        self.metrics["Mean Absolute Error"] = mae
        self.metrics["Mean Squared Error"] = mse
        self.metrics["R2 Score"] = r2s

        print(f"Mean Absolute Error: {mae}")
        print(f"Mean Squared Error: {mse}")
        print(f"R2 Score: {r2s} \n ")

# Implement class model 2: ClassModel 
class ClassModel(MLModel):
    pass 

# Example code 
if __name__ == "__main__":
    pass 
