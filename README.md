

## Air Quality Prediction using Random Forest and Streamlit

Welcome to the Air Quality Prediction project! In this repository, we’ve developed a robust machine learning model to predict air quality based on various environmental factors. Our model utilizes features such as particulate matter (PM), nitrogen dioxide (NO2), and ozone (O3) levels to make accurate predictions. Let’s explore the details!

> Table of Contents
``` Introduction
Data Preprocessing
Feature Engineering
Model Building
Deployment with Streamlit
Results
Usage
Contributing
License
Introduction
Air quality affects our health and well-being. Predicting air quality accurately can help individuals and policymakers take necessary actions. Our goal is to create a reliable model that assesses air quality levels and provides actionable insights.
```
### Data Preprocessing
We followed essential data preprocessing steps:

Data Cleaning: Removed duplicates, handled missing values, and corrected inconsistencies.
Feature Scaling: Ensured all features were on the same scale.
Data Splitting: Separated the dataset into training and testing subsets.

### Feature Engineering
Feature engineering enhances model performance. Here’s what we did:

Feature Extraction: Extracted relevant features from raw data.
Temporal Features: Created features based on time of day, week, and month.
Lagged Features: Included lagged values of air quality indicators.
### Model Building
We experimented with various machine learning algorithms:

Linear Regression: A baseline model for comparison.
Random Forest: Our final choice due to its high accuracy (around 90%) on test data.
Deployment with Streamlit
We deployed our model using Streamlit, a Python library for creating interactive web applications. Users can input environmental parameters, and our model will predict air quality levels.

### Results
Our Random Forest model achieved an impressive R-squared value of 0.90 on the test data. This accuracy ensures reliable predictions for real-world scenarios.

### Usage
Clone this repository.
Install the necessary dependencies (e.g., pip install streamlit).
Run the Streamlit app (streamlit run app.py).
