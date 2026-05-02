import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data Loading 
url = "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"

def run_project():
    try:
        # Load data
        df = pd.read_csv(url)

        # Data Cleaning
        df = df[['country', 'year', 'gdpPercap']].dropna()
        
        # Filter 2007 data
        df_latest = df[df['year'] == 2007].nlargest(10, 'gdpPercap')

        # NumPy Operations
        gdp_values = np.array(df_latest['gdpPercap'])
        avg_gdp = np.mean(gdp_values)
        
        print("--- Project Summary ---")
        print(f"Total Countries Analyzed: {len(df_latest)}")
        print(f"Average GDP (2007): {avg_gdp:.2f}\n")

        # Visualization
        plt.figure(figsize=(10, 6))
        plt.bar(df_latest['country'], df_latest['gdpPercap'], color='teal', alpha=0.7)
        
        plt.title('Top 10 Countries by GDP (Gapminder)', fontsize=14)
        plt.xlabel('Country Name', fontsize=12)
        plt.ylabel('GDP Per Cap', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save and Show
        plt.savefig('gdp_analysis_output.png')
        print("Success: Graph created and saved!")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_project()