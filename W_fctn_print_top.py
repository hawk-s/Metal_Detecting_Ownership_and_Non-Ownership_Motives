import pandas as pd

def print_top_observations(df, columns, num_observations=5):
    """
    Prints the top few largest observations for specified columns in the DataFrame.

    Parameters:
        - df (pandas DataFrame): The DataFrame to analyze.
        - columns (list): List of columns to consider.
        - num_observations (int): Number of top observations to print for each column. Default is 5.
    """

    selected_df = df[columns]  # Select only the specified columns
    for column in selected_df.columns:
        top_observations = selected_df.nlargest(num_observations, column)
        print(f"Top {num_observations} observations for column '{column}':")
        print(top_observations)
        print()


# Example usage
'''
data = {
    'experience': [10, 20, 30, 40, 50],
    'contributions': [5, 15, 25, 35, 45],
    'comments': [100, 200, 300, 400, 500],
    'artifacts': [1, 2, 3, 4, 5],
    'real_net_monetary_index': [0.5, 0.8, 0.7, 0.9, 0.6],
    'localities_rate': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)
selected_columns = ['experience', 'contributions', 'comments', 'artifacts', 'real_net_monetary_index', 'localities_rate']
print_top_observations(df, columns=selected_columns, num_observations=3)
'''