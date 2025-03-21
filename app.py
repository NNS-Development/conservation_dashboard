import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
import seaborn as sns
from streamlit_folium import folium_static
from src.utils import haversine
# Streamlit app layout
st.title("Migration Analysis Dashboard")

# Load and preprocess the dataset
@st.cache_data
def load_data():
    bird_data = pd.read_csv("src/data/migration_original.csv")
    bat_data = pd.read_csv("src/data/Hammer-headed fruit bats (Hypsignathus monstrosus) in the Republic of Congo-acc.csv")  # Assuming this is the second dataset
    
    # Process bird data
    bird_data['timestamp'] = pd.to_datetime(bird_data['timestamp'])
    bird_data['date'] = bird_data['timestamp'].dt.date
    bird_data['month'] = bird_data['timestamp'].dt.month
    bird_data['hour'] = bird_data['timestamp'].dt.hour
    
    # Process bat data - adjust these based on your actual bat dataset columns
    bat_data['timestamp'] = pd.to_datetime(bat_data['timestamp'])
    bat_data['date'] = bat_data['timestamp'].dt.date
    
    # Parse acceleration data
    def parse_acceleration(acc_str):
        values = [float(x) for x in acc_str.split()]
        return pd.DataFrame({
            'x': values[::3],
            'y': values[1::3],
            'z': values[2::3]
        })
    
    bat_data['acceleration'] = bat_data['eobs:accelerations-raw'].apply(parse_acceleration)
    return bird_data, bat_data

bird_data, bat_data = load_data()

# Dataset selector
dataset_type = st.sidebar.radio("Select Dataset", ["Bird Migration", "Bat Activity"])

if dataset_type == "Bird Migration":
    data = bird_data

    # Sidebar filters
    st.sidebar.header("Filters")
    selected_bird = st.sidebar.selectbox("Select Bird ID", data['individual-local-identifier'].unique())

    # Bird Information Section
    st.header("Bird Information")
    filtered_data = data[data['individual-local-identifier'] == selected_bird]
    coordinates = list(zip(filtered_data['location-lat'], filtered_data['location-long']))

    # Using a single column for species name to give it more space
    st.subheader(filtered_data['individual-taxon-canonical-name'].iloc[0])

    # Other metrics in columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Days", f"{(filtered_data['date'].nunique())} days")
        total_distance = sum([haversine(coordinates[i], coordinates[i+1]) 
                            for i in range(len(coordinates)-1)])
        st.metric("Total Distance", f"{total_distance:.0f} km")

    with col2:
        st.metric("Start Date", filtered_data['timestamp'].min().strftime('%Y-%m-%d'))
        st.metric("End Date", filtered_data['timestamp'].max().strftime('%Y-%m-%d'))

    with col3:
        avg_speed = total_distance / filtered_data['date'].nunique()
        st.metric("Avg. Daily Distance", f"{avg_speed:.1f} km/day")
        st.metric("Tag ID", filtered_data['tag-local-identifier'].iloc[0])

    # Main content
    st.header("Migration Analysis")

    # 1. Map Visualization
    st.subheader("Migration Route")
    filtered_data = data[data['individual-local-identifier'] == selected_bird]

    m = folium.Map(location=[filtered_data['location-lat'].mean(), 
                            filtered_data['location-long'].mean()], 
                zoom_start=5)

    # Add points to map
    coordinates = list(zip(filtered_data['location-lat'], 
                        filtered_data['location-long']))
    for i in range(len(coordinates)-1):
        # Draw lines between consecutive points
        folium.PolyLine(
            locations=[coordinates[i], coordinates[i+1]],
            weight=2,
            color='red',
            opacity=0.8
        ).add_to(m)

    folium_static(m)

    # 2. Movement Analysis
    st.subheader("Movement Analysis")
    col1, col2 = st.columns(2)

    with col1:
        # Daily distance traveled
        st.write("Daily Distance Traveled")
        daily_distances = []
        dates = filtered_data['date'].unique()
        
        for date in dates:
            day_data = filtered_data[filtered_data['date'] == date]
            if len(day_data) > 1:
                # Calculate distance between consecutive points
                coords = list(zip(day_data['location-lat'], day_data['location-long']))
                distance = sum([haversine(coords[i], coords[i+1]) 
                            for i in range(len(coords)-1)])
                daily_distances.append((date, distance))
        
        if daily_distances:
            distances_df = pd.DataFrame(daily_distances, columns=['Date', 'Distance'])
            fig, ax = plt.subplots()
            ax.plot(distances_df['Date'], distances_df['Distance'])
            ax.set_xlabel('Date')
            ax.set_ylabel('Distance (km)')
            plt.xticks(rotation=45)
            st.pyplot(fig)

    with col2:
        # Environmental factors correlation
        st.write("Environmental Factors Impact")
        env_columns = ['ECMWF Interim Full Daily Invariant Low Vegetation Cover',
                    'ECMWF Interim Full Daily Invariant High Vegetation Cover']
        
        corr_data = filtered_data[env_columns].corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr_data, annot=True, ax=ax)
        st.pyplot(fig)

    # 3. Time Pattern Analysis
    st.subheader("Movement Patterns")
    hourly_activity = filtered_data.groupby('hour').size()
    fig, ax = plt.subplots()
    ax.bar(hourly_activity.index, hourly_activity.values)
    ax.set_xlabel('Hour of Day')
    ax.set_ylabel('Number of Movements')
    st.pyplot(fig)

else:  # Bat Activity
    data = bat_data
    st.header("Bat Acceleration Analysis")
    
    # Sidebar filters for bat data
    selected_bat = st.sidebar.selectbox("Select Bat ID", data['individual-local-identifier'].unique())
    filtered_data = data[data['individual-local-identifier'] == selected_bat]
    
    # Bat Information Section
    st.subheader(filtered_data['individual-taxon-canonical-name'].iloc[0])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Recording Duration", f"{filtered_data['date'].nunique()} days")
        st.metric("Total Measurements", len(filtered_data))
    
    with col2:
        st.metric("Start Time", filtered_data['timestamp'].min().strftime('%Y-%m-%d %H:%M'))
        st.metric("End Time", filtered_data['timestamp'].max().strftime('%Y-%m-%d %H:%M'))
    
    # Acceleration Analysis
    st.subheader("Movement Analysis")
    
    # Sample selection
    selected_timestamp = st.selectbox(
        "Select Timestamp for Detailed Analysis",
        filtered_data['timestamp']
    )
    
    selected_sample = filtered_data[filtered_data['timestamp'] == selected_timestamp].iloc[0]
    acc_data = selected_sample['acceleration']
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Plot acceleration patterns
        st.write("Acceleration Pattern")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(acc_data['x'], label='X')
        ax.plot(acc_data['y'], label='Y')
        ax.plot(acc_data['z'], label='Z')
        ax.set_xlabel('Sample')
        ax.set_ylabel('Acceleration (raw units)')
        ax.legend()
        st.pyplot(fig)
    
    with col2:
        # Movement intensity analysis
        st.write("Movement Intensity")
        intensity = np.sqrt(acc_data['x']**2 + acc_data['y']**2 + acc_data['z']**2)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(intensity)
        ax.set_xlabel('Sample')
        ax.set_ylabel('Movement Intensity')
        st.pyplot(fig)
    
    # Daily activity pattern
    st.subheader("Daily Activity Pattern")
    hourly_samples = filtered_data.groupby(filtered_data['timestamp'].dt.hour).size()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(hourly_samples.index, hourly_samples.values)
    ax.set_xlabel('Hour of Day')
    ax.set_ylabel('Number of Measurements')
    ax.set_title('Activity Distribution Throughout Day')
    st.pyplot(fig)
    
    # Movement characteristics
    st.subheader("Movement Characteristics")
    if st.checkbox("Show Movement Statistics"):
        all_intensities = []
        for _, row in filtered_data.iterrows():
            acc = row['acceleration']
            intensity = np.sqrt(acc['x']**2 + acc['y']**2 + acc['z']**2)
            all_intensities.extend(intensity)
            
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(all_intensities, bins=50, ax=ax)
        ax.set_xlabel('Movement Intensity')
        ax.set_ylabel('Count')
        ax.set_title('Distribution of Movement Intensities')
        st.pyplot(fig)

