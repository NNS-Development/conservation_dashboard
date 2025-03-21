import streamlit as st
from src.data_loader import load_iucn_data, load_gbif_data
from src.visualization import plot_population_trends, plot_correlation_with_factors
from src.prediction import train_population_model

# Streamlit app layout
st.title("Conservation Impact Dashboard")

# Load datasets
st.sidebar.header("Dataset Upload")
iucn_file = st.sidebar.file_uploader("Upload IUCN Data", type=["csv"])
gbif_file = st.sidebar.file_uploader("Upload GBIF Data", type=["csv"])

if iucn_file:
    iucn_data = load_iucn_data(iucn_file)
    st.write(iucn_data.head())

if gbif_file:
    gbif_data = load_gbif_data(gbif_file)
    st.write(gbif_data.head())

# Data Visualizations
if st.sidebar.button('Show Population Trends'):
    if iucn_file:
        plot_population_trends(iucn_data, 'species', 'population')
    else:
        st.warning("Please upload the IUCN dataset first.")

if st.sidebar.button('Show Correlation with Environmental Factors'):
    if gbif_file:
        plot_correlation_with_factors(gbif_data, 'eventDate', 'population')
    else:
        st.warning("Please upload the GBIF dataset first.")

# Machine Learning
if st.sidebar.button('Train Population Prediction Model'):
    if iucn_file:
        model = train_population_model(iucn_data, ['factor1', 'factor2'], 'population')
        st.success("Model trained successfully!")
    else:
        st.warning("Please upload the IUCN dataset first.")

