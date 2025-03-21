import pandas as pd

# Function to load the IUCN dataset
def load_iucn_data(file_path):
    """
    Loads the IUCN species dataset and performs basic cleaning.
    """
    data = pd.read_csv(file_path)
    
    # Example preprocessing: drop NaN values and reset index
    data = data.dropna()
    data.reset_index(drop=True, inplace=True)
    
    print(f"IUCN Data Loaded: {data.shape[0]} rows")
    return data

# Function to load GBIF dataset
def load_gbif_data(file_path):
    """
    Loads the GBIF species occurrence data and performs basic cleaning.
    """
    data = pd.read_csv(file_path)
    
    # Example preprocessing: keep relevant columns and drop NaN values
    data = data[['species', 'decimalLatitude', 'decimalLongitude', 'eventDate']]  # Modify as necessary
    data = data.dropna()
    
    print(f"GBIF Data Loaded: {data.shape[0]} rows")
    return data

