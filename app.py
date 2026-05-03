import streamlit as st
import pickle
import numpy as np

# Load model
model_path = os.path.join(os.path.dirname(__file__), "model", "soh_model.pkl")
# Page config
st.set_page_config(page_title="Battery SoH Predictor", layout="centered")

# Title
st.markdown("## ⚙️ Manual Battery Prediction")

# Create 2 columns
col1, col2 = st.columns(2)

with col1:
    voltage = st.number_input("⚡ Voltage (V)", value=3.60, step=0.1)
    current = st.number_input("🔌 Current (A)", value=0.90, step=0.1)
    temperature = st.number_input("🌡 Temperature (°C)", value=28.0, step=0.5)

with col2:
    capacity = st.number_input("🔋 Capacity (Ah)", value=2.50, step=0.1)
    cycle = st.number_input("🔄 Charge Cycle", value=1, step=1)

# Button
st.markdown("")

if st.button("🔍 Predict Battery SoH"):
    input_data = np.array([[voltage, capacity, current, cycle, temperature]])
    prediction = model.predict(input_data)

    soh = prediction[0]

    # Result styling
    if soh > 80:
        status = "✅ Good Health"
    elif soh > 50:
        status = "⚠️ Moderate Health"
    else:
        status = "❌ Poor Health"

    st.success(f"### Predicted SoH: {soh:.2f}%")
    st.info(f"### Status: {status}")
