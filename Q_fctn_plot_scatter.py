'''
import pandas as pd
import matplotlib.pyplot as plt

def plot_scatter(dataframe, dependent_var, independent_vars):
    """
    Create scatter plots between a dependent variable and multiple independent variables from a dataframe.
    
    Parameters:
        dataframe (pandas.DataFrame): The dataframe containing the variables.
        dependent_var (str): The column name of the dependent variable.
        independent_vars (list): List of column names of the independent variables.
    
    Returns:
        None (displays the scatter plots)
    """
    # Extract the dependent variable values from the dataframe
    dependent_values = dataframe[dependent_var]
    
    # Create scatter plots for each independent variable
    for independent_var in independent_vars:
        independent_values = dataframe[independent_var]
        
        # Create the scatter plot
        plt.scatter(independent_values, dependent_values, alpha=0.5)
        plt.xlabel(independent_var)
        plt.ylabel(dependent_var)
        plt.title(f"Scatter Plot: {dependent_var} vs {independent_var}")
        plt.grid(True)
        
        # Show the scatter plot
        plt.show()
'''
'''
##with trendline:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_scatter(dataframe, dependent_var, independent_vars):
    """
    Create scatter plots between a dependent variable and multiple independent variables from a dataframe,
    including a trendline.
    
    Parameters:
        dataframe (pandas.DataFrame): The dataframe containing the variables.
        dependent_var (str): The column name of the dependent variable.
        independent_vars (list): List of column names of the independent variables.
    
    Returns:
        None (displays the scatter plots)
    """
    # Extract the dependent variable values from the dataframe
    dependent_values = dataframe[dependent_var]
    
    # Create scatter plots for each independent variable
    for independent_var in independent_vars:
        independent_values = dataframe[independent_var]
        
        # Create the scatter plot
        plt.scatter(independent_values, dependent_values, alpha=0.5)
        plt.xlabel(independent_var)
        plt.ylabel(dependent_var)
        plt.title(f"Scatter Plot: {dependent_var} vs {independent_var}")
        plt.grid(True)
        
        # Fit a linear regression line
        slope, intercept = np.polyfit(independent_values, dependent_values, 1)
        trendline_x = np.array([min(independent_values), max(independent_values)])
        trendline_y = slope * trendline_x + intercept
        plt.plot(trendline_x, trendline_y, color='red')
        
        # Show the scatter plot with the trendline
        plt.show()
'''


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_scatter(dataframe, dependent_var, independent_vars):
    """
    Create scatter plots between a dependent variable and multiple independent variables from a dataframe,
    including a trendline.
    
    Parameters:
        dataframe (pandas.DataFrame): The dataframe containing the variables.
        dependent_var (str): The column name of the dependent variable.
        independent_vars (list): List of column names of the independent variables.
    
    Returns:
        None (displays the scatter plots)
    """
    # Extract the dependent variable values from the dataframe
    dependent_values = dataframe[dependent_var]
    
    # Create scatter plots for each independent variable
    for independent_var in independent_vars:
        independent_values = dataframe[independent_var]
        
        # Create the scatter plot
        plt.scatter(independent_values, dependent_values, alpha=0.5)
        plt.xlabel(independent_var)
        plt.ylabel(dependent_var)
        plt.title(f"Scatter Plot: {dependent_var} vs {independent_var}")
        plt.grid(True)
        
        # Fit a linear regression line
        slope, intercept = np.polyfit(independent_values, dependent_values, 1)
        trendline_x = np.array([min(independent_values), max(independent_values)])
        trendline_y = slope * trendline_x + intercept
        plt.plot(trendline_x, trendline_y, color='red')
        
        # Show the scatter plot with the trendline
        plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_scatter_all(dataframe, dependent_var, independent_vars):
    """
    Create scatter plots between a dependent variable and multiple independent variables from a dataframe,
    including a trendline.

    Parameters:
        dataframe (pandas.DataFrame): The dataframe containing the variables.
        dependent_var (str): The column name of the dependent variable.
        independent_vars (list): List of column names of the independent variables.

    Returns:
        None (displays the scatter plots)
    """
    # Extract the dependent variable values from the dataframe
    dependent_values = dataframe[dependent_var]

    # Determine the number of independent variables
    num_vars = len(independent_vars)

    # Calculate the number of rows and columns for subplots
    num_rows = int(np.ceil(np.sqrt(num_vars)))
    num_cols = int(np.ceil(num_vars / num_rows))

    # Create a new figure and subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))
    fig.suptitle(f"Scatter Plots: {dependent_var} vs Independent Variables", fontsize=16)

    # Flatten the axes array
    axes = np.ravel(axes)

    # Create scatter plots for each independent variable
    for i, independent_var in enumerate(independent_vars):
        # Select the current axis
        ax = axes[i]

        independent_values = pd.Series(dataframe[independent_var])

        # Create the scatter plot
        ax.scatter(independent_values, dependent_values, alpha=0.5)
        ax.set_xlabel(independent_var)
        ax.set_ylabel(dependent_var)
        #ax.set_title(f"Scatter Plot: {dependent_var} vs {independent_var}")
        ax.grid(True)

        # Fit a linear regression line
        slope, intercept = np.polyfit(independent_values, dependent_values, 1)
        trendline_x = np.array([min(independent_values), max(independent_values)])
        trendline_y = slope * trendline_x + intercept
        ax.plot(trendline_x, trendline_y, color='red')

    # Adjust the layout and spacing of subplots
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Show the scatter plots
    plt.show()






'''
#the last attempt:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_scatter(dataframe, dependent_var, independent_vars):
    """
    Create scatter plots between a dependent variable and multiple independent variables from a dataframe,
    including a trendline.
    
    Parameters:
        dataframe (pandas.DataFrame): The dataframe containing the variables.
        dependent_var (str): The column name of the dependent variable.
        independent_vars (list): List of column names of the independent variables.
    
    Returns:
        None (displays the scatter plots)
    """
    # Extract the dependent variable values from the dataframe
    dependent_values = dataframe[dependent_var]
    
    # Create scatter plots for each independent variable
    for independent_var in independent_vars:
        independent_values = dataframe[independent_var]
        
        # Create the scatter plot with trendline
        sns.lmplot(x=independent_var, y=dependent_var, data=dataframe)
        plt.title(f"Scatter Plot: {dependent_var} vs {independent_var}")
        
        # Show the scatter plot with the trendline
        plt.show()
'''