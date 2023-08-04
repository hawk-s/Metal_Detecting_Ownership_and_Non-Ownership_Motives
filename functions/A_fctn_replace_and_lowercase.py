import pandas as pd

def replace_special_characters(dataset, column, new_column=None):
    """
    Removes and replaces special characters in a specific column with their equivalents.

    Args:
        dataset (pandas.DataFrame): The dataset containing the column.
        column (str): The name of the column to be processed.
        new_column (str, optional): The name of the new column to be created. Defaults to None.

    Returns:
        pandas.DataFrame: The dataset with the specified column modified.

    Example:
        >>> data = {'Text': ['Ěščřžýáíéďťňóúů', 'Example', 'Příklad']}
        >>> df = pd.DataFrame(data)
        >>> replace_special_characters(df, 'Text')
               Text
        0  escrzyaiedtnouu
        1           Example
        2          Příklad
        >>> replace_special_characters(df, 'Text', 'ModifiedText')
               Text       ModifiedText
        0  Ěščřžýáíéďťňóúů  escrzyaiedtnouu
        1           Example           example
        2          Příklad          priklad
    """
    replacements = {
        'ě': 'e',
        'š': 's',
        'č': 'c',
        'ř': 'r',
        'ž': 'z',
        'ý': 'y',
        'á': 'a',
        'í': 'i',
        'é': 'e',
        'ď': 'd',
        'ť': 't',
        'ň': 'n',
        'ó': 'o',
        'ú': 'u',
        'ů': 'u'
    }

    modified_column = dataset[column].astype(str).apply(
        lambda x: ''.join(replacements.get(c, c) for c in x.lower())
    )

    if new_column:
        dataset[new_column] = modified_column
    else:
        dataset[column] = modified_column

    return dataset
