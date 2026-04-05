import streamlit as st
import requests

# ================= CONFIG =================
st.set_page_config(page_title="Weather App", layout="centered")

API_KEY = "5acebb423e01618e9844c9fcd180e9f9"

# ================= BACKGROUND =================
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    color: white;
}

section.main > div {
    background: transparent;
}

.weather-card {
    background: rgba(255,255,255,0.15);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    backdrop-filter: blur(10px);
}

input {
    background-color: rgba(255,255,255,0.2) !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ================= SETTINGS =================
st.sidebar.title("⚙️ Settings")

unit = st.sidebar.radio("Temperature Unit", ["Celsius (°C)", "Fahrenheit (°F)"])

unit_api = "metric" if "Celsius" in unit else "imperial"
unit_symbol = "°C" if "Celsius" in unit else "°F"

# ================= MAIN =================
st.title("🌤 Weather App")

city = st.text_input("Enter city", "London")

# ================= API FUNCTION =================
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={unit_api}"
    return requests.get(url).json()

# ================= DISPLAY =================
if city:
    data = get_weather(city)

    # DEBUG (có thể xóa sau)
    st.write(data)

    if str(data.get("cod")) == "200":
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels = data["main"]["feels_like"]
        desc = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
        wind = data["wind"]["speed"]

        st.markdown(f"""
        <div class="weather-card">
            <h2>{city}</h2>
            <img src="http://openweathermap.org/img/wn/{icon}@2x.png">
            <h1>{temp}{unit_symbol}</h1>
            <p>{desc}</p>
            <p>🌡 Feels like: {feels}{unit_symbol}</p>
            <p>💧 Humidity: {humidity}%</p>
            <p>🌬 Wind: {wind} {"m/s" if unit_api=="metric" else "mph"}</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("❌ City not found or API not active yet")