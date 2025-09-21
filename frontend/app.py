import joblib
import streamlit as st
import pandas as pd

# Charger modèle et scaler
model = joblib.load('../ml/model/ridge.pkl')
scaler = joblib.load('..//ml/artifacts/scaler.pkl')  # scaler sauvegardé dans le fichier d'entraînement

# Interface
income = st.number_input("Avg. Area Income", min_value=17796, max_value=107701, value=68583)
age = st.number_input("Avg. Area House Age", min_value=2.64, max_value=9.51, value=5.97)
rooms = st.number_input("Avg. Area Number of Rooms", min_value=3.24, max_value=10.76, value=6.98)
bedrooms = st.number_input("Avg. Area Number of Bedrooms", min_value=2.0, max_value=6.5, value=3.98)
population = st.number_input("Area Population", min_value=172, max_value=69621, value=36163)

if st.button("Prédire le prix"):
    input_df = pd.DataFrame([[income, age, rooms, bedrooms, population]],
                            columns=['Avg. Area Income','Avg. Area House Age',
                                     'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms',
                                     'Area Population'])
    
    # Normaliser avec le même scaler que pour l'entraînement
    input_scaled = scaler.transform(input_df)
    
    # Prédiction
    prediction = model.predict(input_scaled)[0]
    st.success(f"Le prix prédit de la maison est : ${prediction:,.2f}")
