import streamlit as st
import requests

st.set_page_config(page_title="Weather App", layout="centered")

# FORCE BACKGROUND
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1e3c72, #2a5298) !important;
        color: white;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stToolbar"] {
        right: 2rem;
    }

    .weather-card {
        background: rgba(255,255,255,0.15);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        backdrop-filter: blur(15px);
        box-shadow: 0px 8px 25px rgba(0,0,0,0.4);
    }

    h1, h2, h3, p {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# TITLE
st.title("🌤 Weather App")

# INPUT
city = st.text_input("Enter city:")

API_KEY = "YOUR_API_KEY"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    return requests.get(url).json()

if city:
    data = get_weather(city)

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]

        st.markdown(f"""
        <div class="weather-card">
            <h2>{city}</h2>
            <img src="http://openweathermap.org/img/wn/{icon}@2x.png">
            <h1>{temp}°C</h1>
            <p>{desc}</p>
            <p>💧 Humidity: {humidity}%</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("❌ City not found!")