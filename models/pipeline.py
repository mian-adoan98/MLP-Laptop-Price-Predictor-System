# Model Developer 
# Implement functionalities for building ml pipeline 
import os 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split

# Concept for applying functionalities for running machine learning pipeline
"""Overview of functionalities to make model development process convenient: 
    - Pipeline: a development workflow that streamlines ml phases starting from model building to model evaluation
    - Evaluator: class that encompasses functionalities for applying hyperparamter tuning, visualising model performance in terms of
    accuracy, loss, complexity"""

"""Pipeline: 

    - Model building: building the model 
    - Model training: training the model
    - Model validation: evaulate the model performance 

"""

# Implement class Pipeline
class Pipeline: 
    # Define attributes for streamline the machine learning pipeline
    def __init__(self, model, data, test_size):
        self.model = model 
        self.dataset = data
        self.test_size = test_size
        self.system_metrics = self.model.metrics
        self.validated_data = [] # contain training and testing set

    # Method: run the machine learning pipeline
    def run(self):
        # Data Preparation:
        training, testing = data_preparation(self.dataset,
                                             target="PRICE", 
                                             test_size=self.test_size)
        xtrain, ytrain = training
        xtest, ytest = testing

        # Model building
        self.model.build(xtrain, ytrain)
        predictions = self.model.predict(xtest)
        self.model.evaluate(xtest, ytest)

        # Save validated data 
        self.validated_data.append((xtrain, ytrain))
        self.validated_data.append((xtest, ytest))

    # Method: visualise model performance
    def visualise(self, input_feature: str):
         # Prepare data from testing set 
        (xtrain, ytrain), (xtest, ytest) = self.validated_data
        feature_train_data = xtrain[[input_feature]]
        feature_test_data = xtest[[input_feature]]

        # Build the model 
        self.model.build(feature_train_data, ytrain)
        predictions = self.model.predict(feature_test_data)

        # Visualise relationship using scatterplot 
        fig, axes = plt.subplots(1,2, figsize=(14,6))
        axes[0].scatter(feature_test_data, ytest, color="blue")
        axes[1].scatter(feature_test_data, ytest, color="purple")
        axes[1].plot(feature_test_data, predictions, color="black")

        # Plot 1: linear regression distribution before evaluation
        axes[0].set_title("Model Performance: Before Evaluation")
        axes[0].set_xlabel(f"{input_feature}")
        axes[0].set_ylabel("Price range($)")
        
        # Plot 2: linear regression distribution after evaluation
        axes[1].set_title("Model PerformanceAfter Evaluation")
        axes[1].set_xlabel(f"{input_feature}")
        axes[1].set_ylabel("Price range($)")
        

"""Functionalities that need to move to script file model_dev.py: 
    - data_preparation()
    - """
# Implement function: data_preparation()
def data_preparation(dataset: pd.DataFrame, 
                     target: str,
                     test_size: float = 0.25) -> tuple[tuple, tuple]:
    # Prepare the data
    predictors = dataset.drop(columns=[target], axis=1)
    target_var = dataset[target]

    # Data Splitting: training and testing sets
    xtrain, xtest, ytrain, ytest = train_test_split(predictors, target_var, test_size=test_size, random_state=1234)
    return (xtrain, ytrain), (xtest, ytest)


# Implement function: building model summary
def build_model_summary(mlsystems: list[object]):
    # Define a model collection list
    models = []
    model_metrics = {}
    # Extract all base models 
    for i,system in enumerate(mlsystems):
        # Extract the base model from the system
        base_model = system.model
        model_name = f"Model_PT{i}"     # Model_PT = Model Prototype
        
        # Extract metrics 
        model_metric = system.system_metrics
        model_metrics[model_name] = model_metric
    
    # Build a dataframe based on the given parameters
    return model_metrics
