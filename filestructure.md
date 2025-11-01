# Laptop Price Predictor System: File structure


## Data Ingestion
folder: /collection
scripts: ingestor.py, collector.py
notebooks: 
- data_ingestion.ipynb
- data_ingestion2.ipynb

## Data Preparation
folder: /processing
scripts: cleaner.py, processor.py, transformer.py
notebooks: 
- data_preparation.ipynb
- data_preparation2.ipynb
- data_cleaning.ipynb

## Exploratory Data Analysis
folder: /analysis
scripts: descriptive_analysis.py
notebook:  
- exploratory_data_analysis.ipynb


## Feature Engineering
folder: /feature

## Model Development
folder: /model
subfolders: /model_run, /model_register

model_run: contains all the running scripts where the actual training of the model will take palce
model_register: stores and registerd all trained models useful for tracking its performance

## Model Validation
folder: /model 
subfolder: model/model_val, model/test_data

## Model Deployment
folder: app/



# **Later**

## Model Monitoring & Optimization
## Frontend Development