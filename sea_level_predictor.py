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
 
    
    
    # Create first line of best fit
  
    ln_reg_1 = linregress(X, y)
    X_1 = pd.Series([i for i in range(1880,2051)])
    y_hat_1 = ln_reg_1.intercept + ln_reg_1.slope * X_1

    plt.plot(X_1, y_hat_1)


    # Create second line of best fit
    df_2000= df[df["Year"] >= 2000]

    X_2 = df_2000["Year"]
    y_2 = df_2000["CSIRO Adjusted Sea Level"]
    
    ln_reg_2 = linregress(X_2, y_2)
    X_3  = pd.Series([i for i in range(2000,2051)])
    
    y_hat_2 = ln_reg_2.intercept + ln_reg_2.slope * X_3
    
    plt.plot(X_3, y_hat_2)
  
    

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
  

  