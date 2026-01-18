# Model Packaging: register models in folder 
# Import libraries
import numpy as np 
import pandas as pd 
import joblib as job
import os 
import sys 

# System Configuration
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

# Import functionalities: test the model packaging algorithm 
from models.models import RegressModel
from models.pipeline import Pipeline
from scripts.collection.ingestor import FileIngestor
from sklearn.linear_model import LinearRegression

# Implement class ModelRegistor: registor models in the correct folder 
class ModelRegistor: 
    """
    Docstring for ModelRegistor
    Params: 

    - model: base model or a pipeline with pre-built model
    - select_folder: folder where all model packages are stored for deployment or validation
    - model_path: path of the model package useful for finding the location of the model package

    Return: the class does not return the model, but perform a task where the model package is created in the selected folder
    
    """
    # Specify attributes for building a registor object
    def __init__(self, model, folder: str):
        self.model = model      
        self.select_folder = folder
        # self.model_path = r"C:\Development\Projects\MachineLearning\Laptop-Price-Predictor-System\models"
        self.model_path = os.path.join(PROJECT_ROOT, "models")

    # Method: save the model in the folder 
    def save(self, name: str):
        # Check if the path location exists in the project folder 
        register_folder = os.path.join(self.model_path, self.select_folder)
        if os.path.exists(register_folder): 
            os.makedirs(register_folder, exist_ok=True)

        # Save the model using joblib 
        model_name = f"{name}.pkl"
        model_file_path = os.path.join(register_folder, model_name)
        job.dump(self.model, model_file_path)

        print(f"Model {model_name}: packaging successful. File in path {register_folder}")


# Example code (Test Environment)
if __name__ == "__main__":
    # Load the dataset 
    ingestor = FileIngestor(folder="training", filename="processed_lp_data.csv")
    datasets = ingestor.ingest()

    # Build ml model
    ml_model1 = Pipeline(RegressModel(LinearRegression, "linear_regression"), datasets, test_size=0.25)

    # Package the model 
    packager = ModelRegistor(ml_model1, folder="model_registry")
    packager.save("lr_model")

""" 
TO DOs: (indicate line of code with red dot)

    - modification on line 33/39: model parameter should be moved to save() method to avoid multiple registor objects
    - ...

"""