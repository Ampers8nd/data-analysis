import pandas as pd

def load_data(filepath, sheet_name):
    """Load data from an Excel file."""
    data = pd.read_excel(filepath, sheet_name=sheet_name)
    return data

def clean_data(data, x_column, y_column):
    """Clean data by removing entries where x or y values are zero."""
    x_clean = data[x_column][data[y_column] != 0].tolist()
    y_clean = data[y_column][data[y_column] != 0].tolist()
    return x_clean, y_clean

def linear_regression(x, y):
    """Perform linear regression and return slope, intercept, and r_squared."""
    N = len(x)
    x_sum = sum(x)
    y_sum = sum(y)
    xy_sum = sum(x_i * y_i for x_i, y_i in zip(x, y))
    x_sq_sum = sum(x_i ** 2 for x_i in x)

    x_avg = x_sum / N
    y_avg = y_sum / N

    a = ((xy_sum - x_sum * y_sum / N) / 
         (x_sq_sum - x_sum ** 2 / N))
    b = y_avg - a * x_avg

    y_hat = [a * x_i + b for x_i in x]

    ss_regression = sum((y_i - y_hat_i) ** 2 for y_i, y_hat_i in zip(y, y_hat))
    ss_total = sum((y_i - y_avg) ** 2 for y_i in y)
    r_squared = 1 - (ss_regression / ss_total)

    return a, b, r_squared

def main():
    # Example file path and sheet name
    filepath = "C:/Users/dysto/OneDrive/Documents/ChemLab2Table1.xlsx" # adjust as necessary
    sheet_name = "Sheet1"

    # Load and clean data
    data = load_data(filepath, sheet_name)
    x_clean, y_clean = clean_data(data, "Molarity", "Absorbance")  # Assume columns 0 and 1 are x and y

    # Perform linear regression
    a, b, r_squared = linear_regression(x_clean, y_clean)

    # Print results
    print(f"y = {a:.3g}x + {b:.3g}")
    print(f"r^2 = {r_squared:.3g}")

if __name__ == "__main__":
    main()
