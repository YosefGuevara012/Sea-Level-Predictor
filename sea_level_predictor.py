import pandas as pd
import numpy as np
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
  
    ln_reg_1 = linregress(X, y)
    X_2050 = np.array(range(df["Year"].min(),2051))
    y_hat_1 = ln_reg_1.intercept + ln_reg_1.slope * X_2050

    plt.scatter(X,y)
    plt.plot(X_2050, y_hat_1)
    plt.show()

    # Create second line of best fit
    df_XX = df[df["Year"] >= 2000]

    X_1 = df_XX["Year"]
    y_1 = df_XX["CSIRO Adjusted Sea Level"]
    
    ln_reg_2 = linregress(X_1, y_1)
    X_2_2050 = np.array(range(df_XX["Year"].min(),2051))
    y_hat_1 = ln_reg_2.intercept + ln_reg_2.slope * X_2_2050
    
    plt.scatter(X_1,y_1)
    plt.plot(X_2_2050, y_hat_1)
    plt.show()

    # Add labels and title
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

  
  

  