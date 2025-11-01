import pandas as pd
import numpy as np
def find_outliers_zscore(data, threshold=3):
    """
    Identifies outliers in a dataset using the Z-score method.

    Parameters:
    - data: list or array of numerical values
    - threshold: Z-score threshold to classify outliers (default is 3)

    Returns:
    - outliers: list of outlier values
    """
    data = np.array(data)  # Ensure data is a NumPy array for vectorized operations
    mean = np.mean(data)
    std_dev = np.std(data)
    z_scores = (data - mean) / std_dev
    print(z_scores)
    print(np.abs(z_scores))
    outliers = data[np.abs(z_scores) > threshold]
    return outliers.tolist()

# Example usage
data = [10, 12, 13, 12, 11, 14, 13, 100, 12, 11, 13, 5000]
outliers = find_outliers_zscore(data)
print("Outliers:", outliers)