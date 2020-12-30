import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
sns.set_style('whitegrid')


def min_max_scaler(max_new, min_new, matrix):
    # get current minimum and maximum values
    max_old = np.max(matrix)
    min_old = np.min(matrix)
    # can matrix by max_old+max_new, or with min_old+min_new
    scaled_matrix = ((max_new - min_new) / (max_old-min_old)) * (matrix - max_old) + max_new 
    
    return scaled_matrix


def standard_scaler(matrix):
    # can center data if not divided by std
    # whne divide by std it will convert mean to 0 and std at 1
    # also called Z-score normalization
    target = np.array(matrix)
    target = np.reshape(target, (target.shape[0], 1))
    target_mean = target.mean()
    target_std = target.std()
    target_scaled = (target - target_mean) / target_std
    
    return target_scaled


def check_scaling(matrix_old, matrix_new):
    # compare before-after scaling for target feature
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(30, 5), dpi=110)
    fig.suptitle('Normal vs. Scaled')
    sns.distplot(matrix_old, ax = ax1, fit = norm)
    sns.distplot(matrix_new, ax = ax2, fit = norm)
    
    plt.show()