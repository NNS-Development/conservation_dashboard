import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_population_trends(data, species_column, population_column):
    """
    Plots the population trend of species over time.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='eventDate', y=population_column, hue=species_column, data=data, ax=ax)
    ax.set_title("Species Population Trends")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)  # Pass the figure to Streamlit

def plot_correlation_with_factors(data, factor_column, population_column):
    """
    Plots the correlation between environmental factors and species population.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x=factor_column, y=population_column, data=data, ax=ax)
    ax.set_title(f"Correlation between {factor_column} and Population")
    ax.set_xlabel(factor_column)
    ax.set_ylabel("Population")
    plt.tight_layout()
    st.pyplot(fig)  # Pass the figure to Streamlit

