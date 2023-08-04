import pandas as pd
import matplotlib.pyplot as plt
'''
def plot_histogram(dataframe, column):
    """
    Create a histogram for a specific column of a dataframe.
    
    Parameters:
        dataframe (pandas.DataFrame): The dataframe containing the column.
        column (str): The column name.
    
    Returns:
        None (displays the histogram)
    """
    # Extract the column values from the dataframe
    values = dataframe[column]
    
    # Create the histogram
    plt.hist(values, bins='auto')
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.title(f"Histogram: {column}")
    plt.grid(True)
    
    # Show the histogram
    plt.show()
'''
'''
import pandas as pd
import matplotlib.pyplot as plt

def plot_histograms(dataframe, columns):
    """
    Create histograms for multiple columns of a dataframe.
    
    Parameters:
        dataframe (pandas.DataFrame): The dataframe containing the columns.
        columns (list): List of column names.
    
    Returns:
        None (displays the histograms)
    """
    # Iterate over each column
    for column in columns:
        # Extract the column values from the dataframe
        values = dataframe[column]
        
        # Create the histogram
        plt.hist(values, bins='auto')
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.title(f"Histogram: {column}")
        plt.grid(True)
        
        # Show the histogram
        plt.show()
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
'''
def plot_histograms(dataframe, columns):
    """
    Create histograms with density distribution for multiple columns of a dataframe.

    Parameters:
        dataframe (pandas.DataFrame): The dataframe containing the columns.
        columns (list): List of column names.

    Returns:
        None (displays the histograms)
    """
    # Iterate over each column
    for column in columns:
        # Extract the column values from the dataframe
        values = dataframe[column]
        
        # Create the figure and axes
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Plot the histogram
        sns.histplot(data=values, ax=ax, kde=False, bins='auto', color='skyblue')
        
        # Plot the density distribution
        sns.kdeplot(data=values, ax=ax, color='red')
        
        # Set labels and title
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency / Density')
        ax.set_title(f'Histogram with Density Distribution: {column}')
        
        # Show the histogram
        plt.show()
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
'''
def plot_histograms(dataframe, columns):
    """
    Create histograms with cumulative distribution plot for multiple columns of a dataframe.

    Parameters:
        dataframe (pandas.DataFrame): The dataframe containing the columns.
        columns (list): List of column names.

    Returns:
        None (displays the histograms)
    """
    # Iterate over each column
    for column in columns:
        # Extract the column values from the dataframe
        values = dataframe[column]
        
        # Create the figure and axes
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Plot the histogram
        sns.histplot(data=values, ax=ax, kde=False, bins='auto', color='skyblue')
        
        # Compute cumulative distribution values
        sorted_values = np.sort(values)
        cumulative = np.arange(len(sorted_values)) / float(len(sorted_values))
        
        # Plot the cumulative distribution
        ax.plot(sorted_values, cumulative, color='red', lw=2)
        
        # Set labels and title
        ax.set_xlabel(column)
        ax.set_ylabel('Cumulative Probability')
        ax.set_title(f'Histogram with Cumulative Distribution: {column}')
        
        # Show the histogram
        plt.show()
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
'''
def plot_histograms(dataframe, columns):
    """
    Create histograms with cumulative distribution plot for multiple columns of a dataframe.

    Parameters:
        dataframe (pandas.DataFrame): The dataframe containing the columns.
        columns (list): List of column names.

    Returns:
        None (displays the histograms)
    """
    # Iterate over each column
    for column in columns:
        # Extract the column values from the dataframe
        values = dataframe[column]
        
        # Create the figure and axes
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Plot the histogram
        n, bins, patches = plt.hist(values, bins='auto', color='skyblue', density=True, alpha=0.7)
        
        # Compute cumulative distribution values
        cumulative = np.cumsum(n) / np.sum(n)
        
        # Plot the cumulative distribution
        ax.plot(bins[:-1], cumulative, color='red', lw=2)
        
        # Set labels and title
        ax.set_xlabel(column)
        ax.set_ylabel('Probability / Cumulative Probability')
        ax.set_title(f'Histogram with Cumulative Distribution: {column}')
        
        # Adjust scale to match histogram height
        ax.set_ylim([0, np.max(n)])
        
        # Show the histogram
        plt.show()
'''
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_histograms(dataframe, columns):
    """
    Create histograms scaled to the second most occurring value for multiple columns of a dataframe.

    Parameters:
        dataframe (pandas.DataFrame): The dataframe containing the columns.
        columns (list): List of column names.

    Returns:
        None (displays the histograms)
    """
    # Iterate over each column
    for column in columns:
        # Extract the column values from the dataframe
        values = dataframe[column]
        
        # Calculate histogram
        hist, bins = np.histogram(values, bins='auto')
        
        # Find the two most frequent values
        most_frequent_values = np.argsort(hist)[-2:]
        
        # Get the corresponding bin indices
        bin_indices = np.digitize(values, bins)
        
        # Create the figure and axes
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Plot the histogram scaled to the second most occurring value
        plt.hist(values, bins='auto', color='skyblue')
        
        # Scale the y-axis to the second most occurring value
        ax.set_ylim([0, hist[most_frequent_values[1]]])
        
        # Add text label for the most frequent value
        most_frequent_count = hist[most_frequent_values[0]]
        plt.text(bins[most_frequent_values[0]], most_frequent_count, str(most_frequent_count),
                 ha='center', va='bottom', color='black', fontsize=10)
        
        # Set labels and title
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        ax.set_title(f'Histogram: {column}')
        
        # Show the histogram
        plt.show()
'''
import pandas as pd
import matplotlib.pyplot as plt
'''
def create_histograms_with_zeros(df):
    for column in df.columns:
        # Check if there are any zeros in the column
        if (df[column] == 0).any():
            # Count the number of zeros in the column
            zero_count = (df[column] == 0).sum()

            # Create a histogram without considering the zeros for scaling
            plt.hist(df[column][df[column] != 0], bins='auto')

            # Add the zero count as a text annotation within the zero bar
            plt.text(0, 0.5, f'Zeros: {zero_count}', transform=plt.gca().transAxes,
                     fontsize=10, va='center', ha='left', color='red')

            # Set the title and labels
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')

            # Show the histogram
            plt.show()
        else:
            # Create a histogram without any special considerations
            plt.hist(df[column], bins='auto')

            # Set the title and labels
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')

            # Show the histogram
            plt.show()
'''
import pandas as pd
import matplotlib.pyplot as plt
'''
def create_histograms_with_zeros(df):
    for column in df.columns:
        # Check if there are any zeros in the column
        if (df[column] == 0).any():
            # Count the number of zeros in the column
            zero_count = (df[column] == 0).sum()

            # Convert the column values to numeric
            numeric_values = pd.to_numeric(df[column], errors='coerce')
            numeric_values = numeric_values.dropna()

            # Create a histogram without considering the zeros for scaling
            plt.hist(numeric_values[numeric_values != 0], bins='auto')

            # Add the zero count as a text annotation within the zero bar
            plt.text(0, 0.5, f'Zeros: {zero_count}', transform=plt.gca().transAxes,
                     fontsize=10, va='center', ha='left', color='red')

            # Set the title and labels
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')

            # Show the histogram
            plt.show()
        else:
            # Create a histogram without any special considerations
            plt.hist(df[column], bins='auto')

            # Set the title and labels
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')

            # Show the histogram
            plt.show()
'''
'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def create_histograms_with_zeros(df, columns=None):
    """
    Create histograms for each column of a pandas DataFrame, with special handling for zero values.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        columns (list, optional): List of column names to create histograms for. If not specified, histograms will be created for all columns. Default is None.

    Returns:
        None
    """

    if columns is None:
        columns = df.columns
    
    for column in columns:
        # Check if there are any zeros in the column
        if (df[column] == 0).any():
            # Count the number of zeros in the column
            zero_count = (df[column] == 0).sum()

            # Convert the column values to numeric
            numeric_values = pd.to_numeric(df[column], errors='coerce')
            numeric_values = numeric_values.dropna()

            # Determine the number of bins for the histogram
            num_bins = min(len(numeric_values.unique()), 20)

            # Create a histogram without considering the zeros for scaling
            plt.hist(numeric_values.values[numeric_values.values != 0], bins=num_bins)

            # Add the zero count as a text annotation within the zero bar
            plt.text(0, 0.5, f'Zeros: {zero_count}', transform=plt.gca().transAxes,
                     fontsize=10, va='center', ha='left', color='red')

            # Set the title and labels
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Count')

            # Set the tick locators for both x and y axes
            plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
            plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

            # Show the histogram
            plt.show()
        else:
            # Create a histogram without any special considerations
            plt.hist(df[column].values, bins=20)

            # Set the title and labels
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Count')

            # Set the tick locators for both x and y axes
            plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
            plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

            # Show the histogram
            plt.show()
'''
'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

def create_histograms_with_zeros(df, columns=None):
    """
    Create histograms for each column of a pandas DataFrame, with special handling for zero values.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        columns (list, optional): List of column names to create histograms for. If not specified, histograms will be created for all columns. Default is None.

    Returns:
        None
    """

    if columns is None:
        columns = df.columns
    
    for column in columns:
        # Check if there are any zeros and values greater than 1 in the column
        if (df[column] == 0).any() and (df[column] > 1).any():
            # Count the number of zeros in the column
            zero_count = (df[column] == 0).sum()

            # Convert the column values to numeric
            numeric_values = pd.to_numeric(df[column], errors='coerce')
            numeric_values = numeric_values.dropna()

            # Determine the number of bins for the histogram
            num_bins = min(len(numeric_values.unique()), 20)

            # Apply the logarithmic transformation log(x+1) to all values in the column
            transformed_values = np.log(numeric_values.values + 1)

            # Create a figure with two subplots
            fig, axs = plt.subplots(1, 2, figsize=(10, 4))

            # Plot the original data histogram excluding zeros
            axs[0].hist(numeric_values.values[numeric_values.values != 0], bins=num_bins, label='Original data')
            axs[0].set_title(f'Histogram of {column} (Original Data)\nZeros: {zero_count}')

            # Plot the log-transformed data histogram excluding zeros
            axs[1].hist(transformed_values[numeric_values.values != 0], bins=num_bins, alpha=0.5, color='orange', label='Log-transformed data')
            axs[1].set_title(f'Histogram of {column} (Log-transformed Data)')

            # Add the zero count as a text annotation within the zero bar in the second subplot
            transformed_zero_count = (transformed_values == 0).sum()
            axs[1].text(0, 0.5, f'Transformed Zeros: {transformed_zero_count}', transform=axs[1].transAxes,
                         fontsize=10, va='center', ha='left', color='red')

            # Set common labels
            for ax in axs.flat:
                ax.set_xlabel(column)
                ax.set_ylabel('Count')

                # Set the tick locators for both x and y axes
                ax.xaxis.set_major_locator(MaxNLocator(integer=True))
                ax.yaxis.set_major_locator(MaxNLocator(integer=True))

            # Add a legend to the first subplot
            axs[0].legend()

            # Adjust the spacing between subplots
            fig.tight_layout()

            # Show the histogram
            plt.show()
        else:
            # Create a histogram without any special considerations
            plt.hist(df[column].values, bins=20)

            # Set the title and labels
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Count')

            # Set the tick locators for both x and y axes
            plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
            plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

            # Show the histogram
            plt.show()
'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
'''
def create_histograms_with_zeros(df, columns=None):
    """
    Create histograms for each column of a pandas DataFrame, with special handling for zero values.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        columns (list, optional): List of column names to create histograms for. If not specified, histograms will be created for all columns. Default is None.

    Returns:
        None
    """

    if columns is None:
        columns = df.columns
    
    for column in columns:
        # Check if there are any zeros in the column
        if (df[column] == 0).any():
            # Count the number of zeros in the column
            zero_count = (df[column] == 0).sum()

            # Convert the column values to numeric
            numeric_values = pd.to_numeric(df[column], errors='coerce')
            numeric_values = numeric_values.dropna()

            # Determine the number of bins for the histogram
            num_bins = min(len(numeric_values.unique()), 20)

            # Exclude zeros from plotting
            numeric_values_no_zeros = numeric_values[numeric_values != 0]

            # Apply the logarithmic transformation log(x+1) to all values in the column
            transformed_values = np.log(numeric_values.values + 1)

            # Create a figure with two subplots
            fig, axs = plt.subplots(1, 2, figsize=(10, 4))

            # Plot the original data histogram excluding zeros
            axs[0].hist(numeric_values_no_zeros, bins=num_bins, label='Original data')
            axs[0].set_title(f'Histogram of {column} (Original Data)\nZeros: {zero_count}')

            # Plot the log-transformed data histogram
            axs[1].hist(transformed_values, bins=num_bins, alpha=0.5, color='orange', label='Log-transformed data')
            axs[1].set_title(f'Histogram of {column} (Log-transformed Data)')

            # Add the zero count as a text annotation within the histogram
            axs[0].text(0, 0.5, f'Zeros: {zero_count}', transform=axs[0].transAxes,
                         fontsize=10, va='center', ha='left', color='red')
            axs[1].text(0, 0.5, f'Zeros: {zero_count}', transform=axs[1].transAxes,
                         fontsize=10, va='center', ha='left', color='red')

            # Set common labels
            for ax in axs.flat:
                ax.set_xlabel(column)
                ax.set_ylabel('Count')

                # Set the tick locators for both x and y axes
                ax.xaxis.set_major_locator(MaxNLocator(integer=True))
                ax.yaxis.set_major_locator(MaxNLocator(integer=True))

            # Add a legend to the first subplot
            axs[0].legend()

            # Adjust the spacing between subplots
            fig.tight_layout()

            # Show the histogram
            plt.show()
        else:
            # Create a histogram without any special considerations
            plt.hist(df[column].values, bins=20)

            # Set the title and labels
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Count')

            # Set the tick locators for both x and y axes
            plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
            plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

            # Show the histogram
            plt.show()
'''
'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

def create_histograms_with_zeros(df, columns=None):
    """
    Create histograms for each column of a pandas DataFrame, with special handling for zero values.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        columns (list, optional): List of column names to create histograms for. If not specified, histograms will be created for all columns. Default is None.

    Returns:
        None
    """

    if columns is None:
        columns = df.columns
    
    for column in columns:
        # Check if there are any zeros in the column
        if (df[column] == 0).any() & (df[column] > 1).any():
            # Count the number of zeros in the column
            zero_count = (df[column] == 0).sum()

            # Convert the column values to numeric
            numeric_values = pd.to_numeric(df[column], errors='coerce')
            numeric_values = numeric_values.dropna()

            # Determine the number of bins for the histogram
            num_bins = min(len(numeric_values.unique()), 20)

            # Exclude zeros and values from 0 to 1 (inclusive) from plotting
            numeric_values_no_zeros = numeric_values[(numeric_values != 0)]

            # Apply the logarithmic transformation log(x+1) to all values in the column
            transformed_values = np.log(numeric_values_no_zeros.values + 1)

            # Create a figure with two subplots
            fig, axs = plt.subplots(1, 2, figsize=(10, 4))

            # Plot the original data histogram excluding zeros
            axs[0].hist(numeric_values_no_zeros, bins=num_bins, label='Original data')
            axs[0].set_title(f'Histogram of {column} (Original Data)\nZeros: {zero_count}')

            # Plot the log-transformed data histogram excluding zeros
            axs[1].hist(transformed_values, bins=num_bins, alpha=0.5, color='orange', label='Log-transformed data')
            axs[1].set_title(f'Histogram of {column} (Log-transformed Data)')

            # Add the zero count as a text annotation within the histogram
            axs[0].text(0, 0.5, f'Zeros: {zero_count}', transform=axs[0].transAxes,
                         fontsize=10, va='center', ha='left', color='red')
            axs[1].text(0, 0.5, f'Zeros: {zero_count}', transform=axs[1].transAxes,
                         fontsize=10, va='center', ha='left', color='red')

            # Set common labels
            for ax in axs.flat:
                ax.set_xlabel(column)
                ax.set_ylabel('Count')

                # Set the tick locators for both x and y axes
                ax.xaxis.set_major_locator(MaxNLocator(integer=True))
                ax.yaxis.set_major_locator(MaxNLocator(integer=True))

            # Add a legend to the first subplot
            axs[0].legend()

            # Adjust the spacing between subplots
            fig.tight_layout()

            # Show the histogram
            plt.show()
    
        else:
            # Create a histogram without any special considerations
            plt.hist(df[column].values, bins=20)

            # Set the title and labels
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Count')

            # Set the tick locators for both x and y axes
            plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
            plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

            # Show the histogram
            plt.show()

'''








'''#the best one so far:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

def create_histograms_with_zeros(df, columns=None):
    """
    Create histograms for each column of a pandas DataFrame, with special handling for zero values.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        columns (list, optional): List of column names to create histograms for. If not specified, histograms will be created for all columns. Default is None.

    Returns:
        None
    """

    if columns is None:
        columns = df.columns
    
    for column in columns:
        # Check if there are any zeros in the column
        if (df[column] == 0).any() and (df[column] > 1).any():
            # Count the number of zeros in the column
            zero_count = (df[column] == 0).sum()

            # Convert the column values to numeric
            numeric_values = pd.to_numeric(df[column], errors='coerce')
            numeric_values = numeric_values.dropna()

            # Determine the number of bins for the histogram
            num_bins = min(len(numeric_values.unique()), 20)

            # Exclude zeros and values from 0 to 1 (inclusive) from plotting
            numeric_values_no_zeros = numeric_values[(numeric_values != 0)]

            # Apply the logarithmic transformation log(x+1) to all values in the column
            transformed_values = np.log(numeric_values_no_zeros.values + 1)

            # Create a figure with two subplots
            fig, axs = plt.subplots(1, 2, figsize=(10, 4))

            # Plot the original data histogram excluding zeros
            axs[0].hist(numeric_values_no_zeros, bins=num_bins, label='Original data')
            axs[0].set_title(f'Histogram of {column} (Original Data)')

            # Plot the log-transformed data histogram excluding zeros
            axs[1].hist(transformed_values, bins=num_bins, alpha=0.5, color='orange', label='Log-transformed data')
            axs[1].set_title(f'Histogram of {column} (Log-transformed Data)')

            # Add the zero count as a text annotation within the histogram
            axs[0].text(0.8, 0.8, f'Zeros: {zero_count}', transform=axs[0].transAxes, ha='right', color='red')
            axs[1].text(0.8, 0.8, f'Zeros: {zero_count}', transform=axs[1].transAxes, ha='right', color='red')

            # Set common labels
            for ax in axs.flat:
                ax.set_xlabel(column)
                ax.set_ylabel('Count')

                # Set the tick locators for both x and y axes
                ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
                ax.yaxis.set_major_locator(MaxNLocator(nbins=6))

            # Add a legend to the first subplot
            axs[0].legend()

            # Adjust the spacing between subplots
            fig.tight_layout()

            # Show the histogram
            plt.show()
    
        else:
            # Create a histogram without any special considerations
            plt.hist(df[column].values, bins=20)

            # Set the title and labels
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Count')

            # Set the tick locators for both x and y axes
            plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6))
            plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6))

            # Show the histogram
            plt.show()
'''
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import MaxNLocator

def create_histograms_with_zeros(df, columns=None):
    """
    Create histograms for each column of a pandas DataFrame, with special handling for zero values.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        columns (list, optional): List of column names to create histograms for. If not specified, histograms will be created for all columns. Default is None.

    Returns:
        None
    """

    if columns is None:
        columns = df.columns
    
    for column in columns:
        # Check if there are any zeros in the column
        if (df[column] == 0).any() and (df[column] > 1).any():
            # Count the number of zeros in the column
            zero_count = (df[column] == 0).sum()

            # Convert the column values to numeric
            numeric_values = pd.to_numeric(df[column], errors='coerce')
            numeric_values = numeric_values.dropna()

            # Determine the number of bins for the histogram
            num_bins = min(len(numeric_values.unique()), 20)

            # Exclude zeros and values from 0 to 1 (inclusive) from plotting
            numeric_values_no_zeros = numeric_values[(numeric_values != 0)]

            # Apply the logarithmic transformation log(x+1) to all values in the column
            transformed_values = np.log(numeric_values_no_zeros.values + 1)

            # Create a figure with two subplots
            fig, axs = plt.subplots(1, 2, figsize=(10, 4))

            # Plot the original data histogram excluding zeros
            sns.histplot(numeric_values_no_zeros, kde=True, ax=axs[0])
            axs[0].set_title(f'Histogram of {column} (Original Data)')

            # Plot the log-transformed data histogram excluding zeros
            sns.histplot(transformed_values, kde=True, ax=axs[1], color='orange')
            axs[1].set_title(f'Histogram of {column} (Log-transformed Data)')

            # Add the zero count as a text annotation within the histogram
            axs[0].text(0.8, 0.8, f'Zeros: {zero_count}', transform=axs[0].transAxes, ha='right', color='red')
            axs[1].text(0.8, 0.8, f'Zeros: {zero_count}', transform=axs[1].transAxes, ha='right', color='red')

            # Set common labels
            for ax in axs.flat:
                ax.set_xlabel(column)
                ax.set_ylabel('Count')

                # Set the tick locators for both x and y axes
                ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
                ax.yaxis.set_major_locator(MaxNLocator(nbins=6))

            # Show the histogram
            plt.show()
    
        else:
            # Create a histogram without any special considerations
            sns.histplot(df[column], kde=True, bins=20)

            # Set the title and labels
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Count')

            # Set the tick locators for both x and y axes
            plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6))
            plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6))

            # Show the histogram
            plt.show()

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import MaxNLocator

def create_histograms_with_zeros(df, columns=None):
    """
    Create histograms for each column of a pandas DataFrame, with special handling for zero values.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        columns (list, optional): List of column names to create histograms for. If not specified, histograms will be created for all columns. Default is None.

    Returns:
        None
    """

    if columns is None:
        columns = df.columns
    
    for column in columns:
        # Check if there are any zeros in the column
        if (df[column] == 0).any() and (df[column] > 1).any():
            # Count the number of zeros in the column
            zero_count = (df[column] == 0).sum()

            # Convert the column values to numeric
            numeric_values = pd.to_numeric(df[column], errors='coerce')
            numeric_values = numeric_values.dropna()

            # Determine the number of bins for the histogram
            num_bins = min(len(numeric_values.unique()), 20)

            # Exclude zeros and values from 0 to 1 (inclusive) from plotting
            numeric_values_no_zeros = numeric_values[(numeric_values != 0)]

            # Apply the logarithmic transformation log(x+1) to all values in the column
            transformed_values = np.log(numeric_values_no_zeros.values + 1)

            # Calculate the bin width for the original data histogram
            original_bin_width = (numeric_values.max() - numeric_values.min()) / num_bins

            # Calculate the bin width for the log-transformed data histogram
            transformed_bin_width = (transformed_values.max() - transformed_values.min()) / num_bins

            # Create a figure with two subplots
            fig, axs = plt.subplots(1, 2, figsize=(10, 4))

            # Plot the original data histogram excluding zeros
            sns.histplot(numeric_values_no_zeros, bins=np.arange(numeric_values.min(), numeric_values.max() + original_bin_width, original_bin_width), ax=axs[0])
            axs[0].set_title(f'Histogram of {column} (Original Data)')

            # Plot the log-transformed data histogram excluding zeros
            sns.histplot(transformed_values, bins=np.arange(transformed_values.min(), transformed_values.max() + transformed_bin_width, transformed_bin_width), kde=True, ax=axs[1], color='orange')
            axs[1].set_title(f'Histogram of {column} (Log-transformed Data)')

            # Add the zero count as a text annotation within the histogram
            axs[0].text(0.8, 0.8, f'Zeros: {zero_count}', transform=axs[0].transAxes, ha='right')
            axs[1].text(0.8, 0.8, f'Zeros: {zero_count}', transform=axs[1].transAxes, ha='right')

            

            # Set common labels
            for ax in axs.flat:
                ax.set_xlabel(column)
                ax.set_ylabel('Count')

                # Set the tick locators for both x and y axes
                ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
                ax.yaxis.set_major_locator(MaxNLocator(nbins=6))

            # Show the histogram
            plt.show()
    
        else:
            # Create a histogram without any special considerations
            sns.histplot(df[column], kde=True, bins=20)

            # Set the title and labels
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Count')

            # Set the tick locators for both x and y axes
            plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6))
            plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6))

            # Show the histogram
            plt.show()



import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

def generate_histograms(data, variables):
    """
    Generate histograms for specified variables in a DataFrame.

    Parameters:
        data (pandas.DataFrame): The DataFrame containing the variables.
        variables (list): A list of variable names to generate histograms for.

    Returns:
        None (displays histograms).

    Example:
        data = pd.DataFrame({'Variable1': [0, 0.5, 0.8, 1],
                             'Variable2': [0.2, 0.3, 0, 0.6],
                             'Variable3': [0, 0, 0.9, 0.4]})
        generate_histograms(data, ['Variable1', 'Variable2', 'Variable3'])
    """

    for var in variables:
        # Filter out zero values
        non_zero_values = data[var][data[var] != 0]

        # Plot histogram
        plt.figure()
        sns.histplot(non_zero_values, kde=True)
        plt.title(f'Histogram of {var}')
        plt.xlabel(var)
        plt.ylabel('Frequency')

        # Count number of zeros
        num_zeros = (data[var] == 0).sum()

        # Annotate number of zeros on the plot
        plt.text(0.8, 0.8, f'Zeros: {num_zeros}', transform=plt.gca().transAxes, ha='right')

        # Adjust x-axis and y-axis ticks
        plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6))
        plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6))

        # Show the plot
        plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

def generate_histograms_with_ones(data, variables):
    """
    Generate histograms for specified variables in a DataFrame.

    Parameters:
        data (pandas.DataFrame): The DataFrame containing the variables.
        variables (list): A list of variable names to generate histograms for.

    Returns:
        None (displays histograms).
    """

    for var in variables:
        # Filter out one values
        non_one_values = data[var][data[var] != 1]

        # Plot histogram
        plt.figure()
        sns.histplot(non_one_values, kde=True)
        plt.title(f'Histogram of {var}')
        plt.xlabel(var)
        plt.ylabel('Frequency')

        # Count number of ones
        num_ones = (data[var] == 1).sum()

        # Annotate number of ones on the plot
        plt.text(0.8, 0.8, f'Ones: {num_ones}', transform=plt.gca().transAxes, ha='right')

        # Adjust x-axis and y-axis ticks
        plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6))
        plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=6))

        # Show the plot
        plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

def generate_histograms_w_log(data, variables):
    """
    Generate histograms for specified variables in a DataFrame.

    Parameters:
        data (pandas.DataFrame): The DataFrame containing the variables.
        variables (list): A list of variable names to generate histograms for.

    Returns:
        None (displays histograms).
    """

    for var in variables:
        # Filter out zero values
        non_zero_values = data[var][data[var] != 0]

        # Calculate the number of bins
        num_bins = min(len(non_zero_values.unique()), 20)

        # Create a figure with two subplots
        fig, axs = plt.subplots(1, 2, figsize=(10, 4))

        # Plot the original data histogram
        sns.histplot(non_zero_values, bins=num_bins, kde=True, ax=axs[0], color='blue')
        axs[0].set_title(f'Histogram of {var} (Original Data)')

        # Plot the log-transformed data histogram
        sns.histplot(np.log(non_zero_values + 1), bins=num_bins, kde=True, ax=axs[1], color='orange')
        axs[1].set_title(f'Histogram of {var} (Log-transformed Data)')

        # Count the number of zeros
        num_zeros = (data[var] == 0).sum()

        # Add the zero count as a text annotation within the histograms
        axs[0].text(0.8, 0.8, f'Zeros: {num_zeros}', transform=axs[0].transAxes, ha='right')
        axs[1].text(0.8, 0.8, f'Zeros: {num_zeros}', transform=axs[1].transAxes, ha='right')

        # Set common labels
        for ax in axs.flat:
            ax.set_xlabel(var)
            ax.set_ylabel('Frequency')

            # Set the tick locators for both x and y axes
            ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
            ax.yaxis.set_major_locator(MaxNLocator(nbins=6))

        # Show the plot
        plt.show()
