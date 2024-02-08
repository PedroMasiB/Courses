import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    fix, ax = plt.subplots(figsize=(12,8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    
    # Create first line of best fit
    linregress_1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_1 = pd.Series([i for i in range(1880, 2051)])
    y_1 = linregress_1.slope * x_1 + linregress_1.intercept
    ax.plot(x_1, y_1, 'r')


    # Create second line of best fit
    df_2 = df.loc[df['Year'] >= 2000]
    linregress_2 = linregress(df_2['Year'], df_2['CSIRO Adjusted Sea Level'])
    x_2 = pd.Series([i for i in range(2000, 2051)])
    y_2 = linregress_2.slope * x_2 + linregress_2.intercept
    ax.plot(x_2, y_2, 'g')
                              

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()