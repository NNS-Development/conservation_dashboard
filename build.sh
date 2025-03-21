#!/bin/bash

# Create and activate a venv 
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

streamlit run app.py
