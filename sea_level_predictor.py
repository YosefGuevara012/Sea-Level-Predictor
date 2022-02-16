import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot

    X = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    plt.scatter(X,y)
    plt.show()
    
    
    # Create first line of best fit
    
    ln_model_1 = linregress(X, y)


    # Create second line of best fit
    y_2050 = range(df["Year"].min(),2051)

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()