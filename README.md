# Migration analysis

## Overview

This is an interactive tool used for analyzing and visualizing wildlife migration patterns and behavioral data. It can help conservation researchers and wildlife biologists look at animal tracking data more easily, helping to inform conservation strategies and habitat protection efforts.

## Features

- **Migration Route Visualization** - Interactive maps showing animal movement patterns over time
- **Movement Analysis** - Calculation of daily distances, speed, and patterns of movement
- **Environmental Factor Correlation** - Analysis of how habitat and environmental variables impact movement
- **Multi-species Support** - Supports birdd migration and bat activities 
- **Temporal Analysis** - Time-based patterns of animal activity and movement
- **Interactive Dashboard**
## Demo Video
[Demo Video](https://youtu.be/EojvVNg-Qgk)
## Current datasets

The dashboard currently supports analysis of:
- Bird migration tracking data (timestamp, location, environmental factors)
- Hammer-headed fruit bat acceleration data from Congo (movement patterns and activity)

## Tech stack

- **Programming Language:** Python 3.x
- **Data Libraries:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn, Folium
- **Web Framework:** Streamlit
- **Data Fetching:** gdown (for retrieving datasets from Google Drive)
- **Version Control:** Git

## Usage

### Requirements

- Python 3.8+
- pip
- Git
- gdown

### Quickstart

```sh
git clone https://github.com/NNS-Development/conservation_dashboard.git
cd conservation_dashboard
```

run the app using the script
```sh
./run.sh
```

### Manual setup

If you prefer to set up manually:

Clone the repository
```sh
git clone https://github.com/NNS-Development/conservation_dashboard.git
cd conservation_dashboard
```

Create a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install dependencies
```sh
pip install -r requirements.txt
```

Create data directory
```sh
mkdir -p src/data
```

Download datasets (requires gdown)
```sh
gdown 1AZFTkhZfRt_pJiLuP14Yr7SpjDgnuyFj -O src/data/hammer_headed_fruit_bats_congo.csv
gdown 1yCSSjXz4RMVkT8LxdLOjrxnlKw4QqAP_ -O src/data/migration_original.csv
```

Launch the app
```sh
streamlit run app.py
```

## Project Structure

```
conservation_dashboard/
│── app.py               # Main Streamlit application
│── build.sh             # Setup and build script
│── requirements.txt     # Dependencies
│── LICENSE              # License information
│── README.md            # Project documentation
│── src/                 # Source code
│   ├── data/            # Dataset storage (created at build time)
│   │   ├── migration_original.csv
│   │   ├── hammer_headed_fruit_bats_congo.csv
│   ├── utils.py         # Utility functions (e.g., distance calculations)
│   ├── visualization.py # Visualization functions
│── out/                 # Output directory
│   ├── models/          # For any trained models
│   ├── plots/           # For exported visualizations
│── venv/                # Virtual environment (created at build time)
```

## Usage

The dashboard has two main analysis modes:

1. **Bird Migration**
   - Select bird ID from the sidebar
   - View migration routes on interactive map
   - Analyze daily movement distances
   - Examine environmental factor correlations
   - View movement patterns by time of day

2. **Bat Activity**
   - Select bat ID from the sidebar
   - Analyze acceleration data across three axes
   - Examine movement intensity patterns
   - View daily activity distributions
   - Generate movement statistics

## Roadmap

- Support for additional species and tracking data types
- Advanced machine learning models for behavior prediction
- Habitat range estimation tools
- Environmental impact analysis
- Conservation priority area recommendations

## License
Look at LICENSE for details
