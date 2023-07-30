import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import MaxNLocator

def create_histograms_all(df, columns=None):
    """
    Create histograms for each column of a pandas DataFrame, with special handling for zero values,
    displayed in one figure with subplots.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        columns (list, optional): List of column names to create histograms for. If not specified, histograms will be created for all columns. Default is None.

    Returns:
        None
    """

    if columns is None:
        columns = df.columns
    
    # Calculate the number of rows and columns for subplots
    num_vars = len(columns)
    num_rows = int(np.ceil(np.sqrt(num_vars)))
    num_cols = int(np.ceil(num_vars / num_rows))
    
    # Create a new figure and subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))
    fig.suptitle("Histograms", fontsize=16)
    
    # Flatten the axes array
    axes = np.ravel(axes)
    
    for i, column in enumerate(columns):
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

            # Select the current axis
            ax = axes[i]

            # Plot the original data histogram excluding zeros
            sns.histplot(numeric_values_no_zeros, bins=np.arange(numeric_values.min(), numeric_values.max() + original_bin_width, original_bin_width), ax=ax)
            ax.set_title(f'Histogram of {column} (Original Data)')

            # Add the zero count as a text annotation within the histogram
            ax.text(0.8, 0.8, f'Zeros: {zero_count}', transform=ax.transAxes, ha='right')
        else:
            # Select the current axis
            ax = axes[i]

            # Create a histogram without any special considerations
            sns.histplot(df[column], kde=True, bins=20, ax=ax)

            # Set the title
            ax.set_title(f'Histogram of {column}')

        # Set common labels
        ax.set_xlabel(column)
        ax.set_ylabel('Count')

        # Set the tick locators for both x and y axes
        ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
        ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
    
    # Adjust the layout and spacing of subplots
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Show the histograms
    plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import MaxNLocator

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import MaxNLocator

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import MaxNLocator
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import MaxNLocator

def create_log_transformed_histograms(df, columns=None):
    """
    Create log-transformed histograms for each column of a pandas DataFrame, with special handling for zero values.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        columns (list, optional): List of column names to create histograms for. If not specified, histograms will be created for all columns. Default is None.

    Returns:
        None
    """

    if columns is None:
        columns = df.columns
    
    # Calculate the number of rows and columns for subplots
    num_vars = len(columns)
    num_rows = int(np.ceil(np.sqrt(num_vars)))
    num_cols = int(np.ceil(num_vars / num_rows))
    
    # Create a new figure and subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))
    fig.suptitle("Log-Transformed Histograms", fontsize=16)
    
    # Flatten the axes array
    axes = np.ravel(axes)
    
    for i, column in enumerate(columns):
        # Convert the column values to numeric
        numeric_values = pd.to_numeric(df[column], errors='coerce')
        numeric_values = numeric_values.dropna()

        # Apply the logarithmic transformation log(x+1) to all values in the column
        transformed_values = np.log(numeric_values.values + 1)

        # Check if there are any zeros in the column
        if (df[column] == 0).any():
            # Count the number of zeros in the column
            zero_count = (df[column] == 0).sum()

            # Exclude zeros from plotting
            transformed_values = transformed_values[transformed_values != 0]

            # Select the current axis
            ax = axes[i]

            # Plot the log-transformed data histogram excluding zeros
            sns.histplot(transformed_values, kde=True, bins=20, ax=ax, color='orange')
            ax.set_title(f'Log-Transformed Histogram of {column}')

            # Add the zero count as a text annotation within the histogram
            ax.text(0.8, 0.8, f'Zeros: {zero_count}', transform=ax.transAxes, ha='right')
    
        else:
            # Select the current axis
            ax = axes[i]

            # Create a histogram without any special considerations
            sns.histplot(transformed_values, kde=True, bins=20, ax=ax, color='orange')

            # Set the title
            ax.set_title(f'Log-Transformed Histogram of {column}')

        # Set common labels
        ax.set_xlabel(column)
        ax.set_ylabel('Count')

        # Set the tick locators for both x and y axes
        ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
        ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
    
    # Adjust the layout and spacing of subplots
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Show the histograms
    plt.show()
