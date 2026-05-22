# Model Development: ML Pipeline

# Import libraries 
import numpy as np 
import pandas as pd 
import os 
import sys 

# Set up system configuration enable efficient file manipulation 
sys.path.append(os.path.abspath(".."))

# Import models from model script file
from models.models import RegressModel
# from scripts.model_dev.model_registor import 

# Build a machine learning pipeline that covers certain phases 
#   - data preparation 
#   - model training
#   - model validation 
#   - model registry #

class MLPipeline:
    # Attributes of MLPipeline class
    def __init__(self, model):
        pass 
