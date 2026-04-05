import streamlit as st
import requests

# CONFIG PAGE
st.set_page_config(page_title="Weather App", layout="centered")

# BACKGROUND CSS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .weather-card {
        background: rgba(255,255,255,0.1);
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# TITLE
st.markdown('<div class="title">🌤 Weather App</div>', unsafe_allow_html=True)

# INPUT
city = st.text_input("Enter city name")

API_KEY = "YOUR_API_KEY"

# API FUNCTION
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    return requests.get(url).json()

# DISPLAY
if city:
    data = get_weather(city)

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]

        st.markdown(
            f"""
            <div class="weather-card">
                <h2>{city}</h2>
                <img src="http://openweathermap.org/img/wn/{icon}@2x.png">
                <h1>{temp}°C</h1>
                <p>{desc}</p>
                <p>💧 Humidity: {humidity}%</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("City not found")