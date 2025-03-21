from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pandas as pd

def train_population_model(data, feature_columns, target_column):
    """
    Trains a machine learning model to predict species population based on environmental factors.
    """
    X = data[feature_columns]
    y = data[target_column]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate performance
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Model trained. Mean Absolute Error: {mae:.2f}")

    return model

def predict_population(model, new_data):
    """
    Predicts the population of species based on new input data.
    """
    return model.predict(new_data)

