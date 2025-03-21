#!/bin/bash

# Create and activate a venv 
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

# Download data files from Google Drive
FOLDER="src/data"
mkdir -p $FOLDER

# Download fruit bat migration data
FILE_ID="1AZFTkhZfRt_pJiLuP14Yr7SpjDgnuyFj"
FILE_NAME="hammer_headed_fruit_bats_congo.csv"
gdown $FILE_ID -O $FOLDER/$FILE_NAME

# Download additional data
FILE_ID="1yCSSjXz4RMVkT8LxdLOjrxnlKw4QqAP_"
FILE_NAME="migration_original.csv"
gdown $FILE_ID -O $FOLDER/$FILE_NAME

# Run the Streamlit app
streamlit run app.py