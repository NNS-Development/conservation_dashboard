# Conservation Impact Dashboard

## Overview

The **Conservation Impact Dashboard** is an interactive web-based tool that analyzes and predicts species recovery trends based on historical data. This project helps conservationists, researchers, and policymakers assess the effectiveness of conservation efforts, habitat restoration, and environmental changes in improving biodiversity.

## Features

**Species Recovery Trends** – Visualize population changes of endangered species over time.

**Conservation Strategy Analysis** – Compare the effectiveness of different conservation efforts.

**Environmental Factor Correlation** – Analyze how climate, habitat restoration, and human activities impact species.

**Predictive Modeling** – Use machine learning to forecast species population trends.

**Interactive Dashboard** – Built with Streamlit for easy user interaction.

## Tech Stack

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **Web Framework:** Streamlit
- **Version Control:** GitHub

## Datasets & APIs

- **IUCN Red List** (Threatened species data): [https://www.iucnredlist.org/](https://www.iucnredlist.org/)
- **GBIF (Global Biodiversity Information Facility)** (Species occurrence records): [https://www.gbif.org/](https://www.gbif.org/)
- **World Bank Biodiversity Indicators** (Environmental data): [https://data.worldbank.org/topic/environment](https://data.worldbank.org/topic/environment)
- **NASA EarthData** (Satellite-based environmental changes): [https://earthdata.nasa.gov/](https://earthdata.nasa.gov/)

## Installation & Setup

### Prerequisites

- Python 3.8+
- pip
- Git

### Steps to Run Locally

```sh
# Clone the repository
git clone https://github.com/NNS-Development/conservation_dashboard.git
cd conservation_dashboard

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit dashboard
streamlit run app.py
```

## Project Structure

```
conservation_dashboard/
│── data/                # Store local dataset (if needed)
│── src/                 # Source files for processing and visualization
│   ├── data_loader.py    # Handles data fetching & preprocessing
│   ├── visualization.py  # Visualization functions
│   ├── prediction.py     # Machine learning model
│── app.py               # Main Streamlit application
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
│── .gitignore           # Ignore unnecessary files
```

## Deployment

To deploy this project online, you can use **Streamlit Cloud** or **Hugging Face Spaces**:

```sh
streamlit share
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

##

