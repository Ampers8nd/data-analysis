import numpy as np
from numpy.linalg import inv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

def load_data(filepath):
    """Load data from an Excel file."""
    data = pd.read_csv(filepath)
    return data

def clean_data(data, x1_column, x2_column, y_column):
    """Clean data by removing entries where x or y values are zero."""
    x1_clean = data[x1_column][data[y_column] != 0].tolist()
    x2_clean = data[x2_column][data[y_column] != 0].tolist()
    y_clean = data[y_column][data[y_column] != 0].tolist()
    return x1_clean, x2_clean, y_clean

def linear_regression(x1, x2, y):
    """Perform linear regression and return slope, intercept, and r_squared."""   
    # assuming x1 and x2 and whatever else has the same length 
    x_matrix = np.asarray([np.ones(len(x1)), x1, x2]).T
    b, a1, a2 = inv(x_matrix.T @ x_matrix) @ x_matrix.T @ y

    return a1, a2, b

def main():
    # Example file path and sheet name
    filepath = "C:/Users/dysto/OneDrive/Documents/dataAnalysis/data/multi-lin-data.csv" #adjust as necessary

    # Load and clean data
    data = load_data(filepath)
    x1_clean, x2_clean, y_clean = clean_data(data, 'x1', 'x2', 'y') 

    # Perform linear regression
    a1, a2, b = linear_regression(x1_clean, x2_clean, y_clean)

    # Print results
    print(f"y = {a1:.3g}x1 + {a2:.3g}x2 + {b:.3g}")
    # print(f"r^2 = {r_squared:.3g}")
    # visualizes our plot using matplotlib (referred to as plt)
    # x_lin_space = np.linspace(0, 7, 100)
    # y_hat = b + a1 * x_lin_space
    # plt.scatter(x1_clean, x2_clean y_clean, marker='x')
    # plt.plot(x_lin_space, y_hat, color='r')
    # plt.show()


if __name__ == "__main__":
    main()