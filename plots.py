import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
sns.set_style('whitegrid')


def plot_outliers(matrix, cut_off = 3):
    # give a single feature
    # can visualize outlirs at cut_off point of 3 std
    mean, std = np.mean(matrix), np.std(matrix)
    z_score = np.abs((matrix - mean) / std)
    threshold = cut_off
    good_data = z_score < threshold
    print(f"Rejection {(~good_data).sum()} points")
    #print(f"z-score of 3 corresponds to a prob of {100 * 2 * norm.sf(threshold):0.2f}%")

    visual_scatter = np.random.normal(size=matrix.size)
    plt.scatter(matrix[good_data], visual_scatter[good_data], s=2, label="Data", color="#4CAF50")
    plt.scatter(matrix[~good_data], visual_scatter[~good_data], s=8, label="Outlier", color="#F44336")
    plt.legend();

    
def plot_numeric_features(df, feature: str, target: str):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(30, 5), dpi=110)
    sns.distplot(df[feature], fit=norm, ax=ax1)
    sns.scatterplot(df[feature], df[target], ax=ax2)
    sns.boxplot(df[feature], ax=ax3, orient='v', width=0.2)
     
    plt.show


def plot_categorical_features(df, feature1, feature2, target):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (30, 5), dpi = 110)
    sns.boxplot(df[feature1], df[target], ax=ax1)
    sns.boxplot(df[feature2], df[target], ax=ax2)
    
    plt.show()