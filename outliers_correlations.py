import numpy as np


def outlier_removal(df, cut_off = 3):
    # remove outliers at defined cut_off point
    for i in range(len(df.columns)):
        if df[df.columns[i]].dtype == 'int64' or df[df.columns[i]].dtype == 'float':
            # get mean and std
            std = df[df.columns[i]].std()
            mean = df[df.columns[i]].mean()
            # cut-off
            cut_off = std * cut_off
            # lower bound
            lower = mean - cut_off
            # upper bound
            upper = mean + cut_off
            # trimmed df
            df = df[(df[df.columns[i]] < upper) & (df[df.columns[i]] > lower)]
    return df


def correlated_data_dropout(df, target: str, threshold = .75):
    # Create correlation matrix
    corr_matrix = df.corr().abs()
    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
    # Find features with correlation greater than 0.95
    to_drop = [column for column in upper.columns if any(upper[column] > threshold) 
               and (column != target)]
               # and (column != features to keep)]
    # Drop features 
    df = df.drop(to_drop, axis=1, inplace=True)
    
    return df, to_drop