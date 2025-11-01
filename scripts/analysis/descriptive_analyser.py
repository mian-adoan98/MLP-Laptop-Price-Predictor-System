## Descriptive Analysis 
# import libraries to build abstract classes
from abc import ABC, abstractmethod

# import libraries 
import os 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

# Implement an abstract class name for building descriptive analysis 
class DescriptiveAnalysis(ABC):
    # Abstract method 1: build a descrptive analysis table
    @abstractmethod
    def analyse(self, input_data: pd.DataFrame) -> pd.DataFrame:
        # Building a dataframe that shows descriptive features: datatypes, nullvalues, number of unique values
        pass 

    # Abstract method 2: visualise certain data descriptive features
    @abstractmethod
    def visualise(self, charttype: str): 
        # Pass the descriptive dataframe 
        # Analyse the dataframe into feature columns and descriptive data
        # Visualise with perferred charttype
        pass 


# Implement class NumericalAnalysis
class NumericalAnalysis(DescriptiveAnalysis):
    # Initialise attributes
    def __init__(self, data: pd.DataFrame):
        self.data = data 

    # Method 1: Building Numerical Statistical Analysis
    def analyse(self, input_data: pd.DataFrame) -> pd.DataFrame:
        pass 

    # Method 2: Visualise Numerical Statistical Analysis
    def visualise(self):
        pass 

# Implement class CategoricalAnalysis
class CategoricalAnalysis(DescriptiveAnalysis):
    pass 

# Implement class StatisticalAnalysis:
class StatisticalAnalysis(DescriptiveAnalysis): 
    # Method 1: build a clear statistical analysis
    def analyse(self, input_data: pd.DataFrame) -> pd.DataFrame:
        # Identify laptop: build a dataset with all possible identified parameters: nullvalues, dtypes, features, number of unique values
        descr_df = pd.DataFrame()
        stats_df = pd.DataFrame()

        # Build a descriptive dataframe using these parameters: Features, Nullvalues, DataTypes, UniqueValues
        descr_df["Features"] = input_data.columns.tolist()
        descr_df["Nullvalues"] = input_data.isnull().sum().values
        descr_df["DataTypes"] = input_data.dtypes.values
        descr_df["UniqueValues"] = input_data.nunique().values
        
        return descr_df
    
    # Method 2: Visualise descriptive dataframe
    def visualise(self):
        # Initialise columns of descriptive data
        data = self.analyse(self.data)
        descr_columns = [c for c in data.columns]

        # Check if columns only contains numericals
        for column in descr_columns:
            check_column = column 
            if not pd.api.types.is_numeric_dtype(data[check_column]):
                descr_columns.remove(check_column)
    
        # Initialise variables for building descriptive barcharts
        features = data["Features"].to_numpy()

        """ATTENTION 1: Measurement variable: check carefully"""
        # measurements = {x:y for x,y in zip(data.drop(columns=["Features","DataTypes"], axis=1).columns, 
        #                             data.drop(columns=["Features","DataTypes"], axis=1).values.transpose())}
        
        descr_params = ["Nullvalues", "UniqueValues"]
        descr_params_len = len(descr_params)

        # Create subplots 
        fig, ax = plt.subplots(1,descr_params_len, figsize=(15,6))

        # Draw bars using numeric positions
        for i, descr_param in zip(list(range(descr_params_len)), descr_params):
            x = np.arange(len(features))
            rects = ax[i].bar(x, measurements[descr_param], color="black", alpha=0.75)

            ax[i].bar(features, measurements[descr_param], color="black", alpha=0.75)
            ax[i].set_xlabel("Features")
            ax[i].set_ylabel("Counts")
            ax[i].set_title(f"{descr_param} distribution across Features")

            # add numeric labels above each bar
            ax[i].bar_label(rects, padding=3, fmt="%d")

            # Set tick positions and labels, rotate and align to avoid overlap
            # Set tick positions and labels, rotate and align to avoid overlap
            ax[i].set_xticks(x)
            ax[i].set_xticklabels(features, rotation=45, ha="right", fontsize=9)

        fig.tight_layout()


        ## ---------------------------------------------------------------------------------------------------------------------------------------

# Example code 
if __name__ == "__main__":
    pass 