import streamlit as st
import pandas as pd

from radar_simulation import generate_radar_data
from classification import classify_object
from environment import get_environment

st.set_page_config(
    page_title="High Altitude Aerial Monitoring",
    layout="wide"
)

st.title("📡 High Altitude Anti-Drone Detection System")
st.write("AI-Based Aerial Object Monitoring Simulation")

st.sidebar.header("Environmental Conditions")

altitude = st.sidebar.slider(
    "Altitude (meters)", 0, 5000, 1000
)

temperature, pressure = get_environment(altitude)

st.sidebar.metric("Temperature", f"{temperature:.1f} °C")
st.sidebar.metric("Pressure", f"{pressure:.1f} hPa")

st.subheader("📡 Simulated Radar Data")

data = generate_radar_data()

st.dataframe(data)

st.subheader("🔍 Object Classification")

results = []

for _, row in data.iterrows():
    object_type = classify_object(row["doppler"])

    results.append({
        "Distance": row["distance"],
        "Doppler": row["doppler"],
        "Classification": object_type
    })

results_df = pd.DataFrame(results)

st.dataframe(results_df)

if "Drone" in results_df["Classification"].values:
    st.warning("⚠️ Simulated Drone Detection Alert!")

st.subheader("📊 Radar Visualization")

st.scatter_chart(data, x="distance", y="doppler")
