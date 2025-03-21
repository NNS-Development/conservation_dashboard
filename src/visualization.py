import matplotlib.pyplot as plt
import seaborn as sns

def plot_population_trends(data, species_column, population_column):
    """
    Plots the population trend of species over time.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='eventDate', y=population_column, hue=species_column, data=data)
    plt.title("Species Population Trends")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_correlation_with_factors(data, factor_column, population_column):
    """
    Plots the correlation between environmental factors and species population.
    """
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=factor_column, y=population_column, data=data)
    plt.title(f"Correlation between {factor_column} and Population")
    plt.xlabel(factor_column)
    plt.ylabel("Population")
    plt.tight_layout()
    plt.show()

