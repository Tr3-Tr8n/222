import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Weather Lite", layout="wide")

API_KEY = "YOUR_NEW_API_KEY"   # ← thay key

# ===== STYLE =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg,#1e3c72,#2a5298);
    color:white;
}
</style>
""", unsafe_allow_html=True)

# ===== SETTINGS =====
st.sidebar.title("⚙ Settings")

unit = st.sidebar.radio("Unit", ["Celsius","Fahrenheit"])
unit_api = "metric" if unit=="Celsius" else "imperial"
unit_sym = "°C" if unit=="Celsius" else "°F"

# ===== FUNCTIONS =====
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={unit_api}"
    return requests.get(url).json()

def get_forecast(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={unit_api}"
    return requests.get(url).json()

# ===== UI =====
st.title("🌤 Weather App (Lite)")

city = st.text_input("Enter city", "London")

if city:
    data = get_weather(city)

    if str(data.get("cod")) == "200":

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        desc = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]

        # ===== CURRENT =====
        col1, col2 = st.columns(2)

        with col1:
            st.image(f"https://openweathermap.org/img/wn/{icon}@2x.png")
            st.subheader(f"{city}")
            st.write(f"🌡 {temp}{unit_sym}")
            st.write(desc)

        with col2:
            st.metric("Humidity", f"{humidity}%")
            st.metric("Wind", f"{wind}")

        # ===== FORECAST =====
        forecast = get_forecast(city)

        if str(forecast.get("cod")) == "200":

            temps = []
            times = []

            for item in forecast["list"][:8]:
                temps.append(item["main"]["temp"])
                times.append(item["dt_txt"][11:16])

            df = pd.DataFrame({
                "Time": times,
                "Temperature": temps
            })

            st.subheader("📈 Temperature Trend")
            st.line_chart(df.set_index("Time"))

            st.subheader("📊 Temperature Bar")
            st.bar_chart(df.set_index("Time"))

            st.subheader("📋 Data Table")
            st.dataframe(df)

    else:
        st.warning("❌ City not found or API key not ready")