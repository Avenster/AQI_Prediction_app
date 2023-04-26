import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the saved model
with open('gb.pkl', 'rb') as file:
    rf = pickle.load(file)

# Define a function to predict AQI
def predict_aqi(pm2, pm10, no, no2, nox, nh3, co, so2, o3, benzene, toluene, xylene):
    input_data = np.array([[pm2, pm10, no, no2, nox, nh3, co, so2, o3, benzene, toluene, xylene]])
    aqi_pred = rf.predict(input_data)[0]
    if aqi_pred >= 0 and aqi_pred <= 50:
        label = "Good"
    elif aqi_pred <= 100:
        label = "Satisfactory"
    elif aqi_pred <= 200:
        label = "Moderately polluted"
    elif aqi_pred <= 300:
        label = "Poor"
    elif aqi_pred <= 400:
        label = "Very poor"
    else:
        label = "Severe"
    
    return aqi_pred, label
   

# Create a web app using Streamlit
def main():
    st.markdown(
    """
    <div style='text-align: left;'>
        <h1 style='font-size: 36px; color:magenta ;font-weight: bold; font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;'>AQI Prediction App</h1>
    </div>
    """,
    unsafe_allow_html=True)
    
    st.markdown(
    """
    <div style='text-align: left;'>
        <h1 style='font-size: 15px;color:pink ;font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;'>This app predicts the AQI (Air Quality Index) based on various input features.</h1>
    </div>
    """,
    unsafe_allow_html=True
    )
   

    # Add input features
    pm2 = st.slider("PM2.5", min_value=0.0, max_value=1000.0, value=15.02)
    pm10 = st.slider("PM10", min_value=0.0, max_value=1000.0, value=50.94)
    no = st.slider("NO", min_value=0.0, max_value=400.0, value=7.68)
    no2 = st.slider("NO2", min_value=0.0, max_value=400.0, value=25.06)
    nox = st.slider("NOx", min_value=0.0, max_value=1000.0, value=19.54)
    nh3 = st.slider("NH3", min_value=0.0, max_value=1000.0, value=12.47)
    co = st.slider("CO", min_value=0.0, max_value=1000.0, value=0.47)
    so2 = st.slider("SO2", min_value=0.0, max_value=1000.0, value=8.55)
    o3 = st.slider("O3", min_value=0.0, max_value=1000.0, value=23.30)
    benzene = st.slider("Benzene", min_value=0.0, max_value=1000.0, value=2.24)
    toluene = st.slider("Toluene", min_value=0.0, max_value=1000.0, value=12.07)
    xylene = st.slider("Xylene", min_value=0.0, max_value=1000.0, value=0.73)
    

    # Predict AQI
    if st.button("Predict AQI"):
        aqi_pred, label = predict_aqi(pm2, pm10, no, no2, nox, nh3, co, so2, o3, benzene, toluene, xylene)
        st.success(f"The predicted AQI is {round(aqi_pred)}. The air quality is {label}.")

    
    
if __name__ == '__main__':
    main()
