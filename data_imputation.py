import random
import numpy as np

def categorical_imputation(df, percent_missing = .75):
    # Get column name with missing values more than 80% missing values NAN
    # d_missing = df.isna()
    # get percentage of missing values in df per columns
    # get sum of missing values in True False
    # devide that by total observations
        # total_missing = d_missing.sum()
        # total_missing / len(df)
    # simple model
        # df.isna().mean()
    for i in range(len(df.isna().mean().round(4))):
        total_missing_values = df.isna().mean()
        if total_missing_values[i]  > percent_missing:
            #print(i, df.columns[i])  ## print column names and index
            df[df.columns[i]].replace(np.nan, '0', inplace = True)
    
    for i in range(len(df.columns)):
        if df[df.columns[i]].dtype == 'object':
            mode = df[df.columns[i]].mode()
            value = mode[0]
            df[df.columns[i]] = df[df.columns[i]].fillna(value = value)
    
    return df

def statistical_imputation(df, imputed_value):
    df1 = df.copy()
    for i in range(len(df1.columns)):
        if df1[df1.columns[i]].dtype == 'int64' or df1[df1.columns[i]].dtype == 'float':
            if imputed_value == 'mean':
                value = df1[df1.columns[i]].mean()
            elif imputed_value == 'median':
                value = df1[df1.columns[i]].median()
        df1[df1.columns[i]] = df1[df1.columns[i]].fillna(value = value)
        
    return df1

## Random Categorical Imputation ##        
def random_imputation(df):
    df1 = df.copy()
    random_percentage = []
    running_sum = 0
    # check for column value, apply imputation if values is int64 or float
    # get frequency and total frequency of series
    for i in range(len(df1.columns)):
        if df1[df1.columns[i]].dtype == 'object':
            frequency = df1[df1.columns[i]].value_counts(dropna = True)
            total_frequency = sum(frequency)          
            # loop ove frequency and obtain individual percentage for values

            for key in frequency.keys():
                percentage = frequency[key] / total_frequency
                running_sum += percentage
                random_percentage.append((key, running_sum))          
           
            random_value = random.random()
            for key, value in random_percentage:
                if random_value < value:
                    #import pdb; pdb.set_trace()
                    df1[df1.columns[i]] = df1[df1.columns[i]].fillna(value = key)
                    break
    return df1

def bianary_encoder(matrix):
    two_variables = {}
    value_list = []
    for index, value in enumerate(matrix):
        two_variables[value] = 0
        if len(two_variables) > 2:
            raise Exception('Column has more than 2 variables, cannot use bianary_encoder')
        elif len(two_variables) == 2:
            for key, value in two_variables.items():
                value_list.append(key)
    matrix.replace(value_list[0], 0, inplace = True)
    matrix.replace(value_list[1], 1, inplace = True)
  #  import pdb; pdb.set_trace()
    return matrix