import streamlit as st
import requests

st.set_page_config(page_title="Weather Pro", layout="wide")

# ================= BACKGROUND DYNAMIC =================
def set_bg(condition):
    if "cloud" in condition:
        bg = "linear-gradient(135deg, #757f9a, #d7dde8)"
    elif "rain" in condition:
        bg = "linear-gradient(135deg, #314755, #26a0da)"
    elif "clear" in condition:
        bg = "linear-gradient(135deg, #56ccf2, #2f80ed)"
    else:
        bg = "linear-gradient(135deg, #1e3c72, #2a5298)"

    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: {bg};
        color: white;
    }}
    </style>
    """, unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.title("⚙️ Settings")

unit = st.sidebar.radio("Unit", ["°C", "°F"])
unit_api = "metric" if unit == "°C" else "imperial"

# ================= NAVBAR =================
st.markdown("""
<h1 style='text-align:center;'>🌤 Weather Dashboard</h1>
""", unsafe_allow_html=True)

# ================= INPUT =================
city = st.text_input("Search city...", "Houston")

API_KEY = "YOUR_API_KEY"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={unit_api}"
    return requests.get(url).json()

def get_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={unit_api}"
    return requests.get(url).json()

# ================= MAIN =================
if city:
    data = get_weather(city)

    if data["cod"] == 200:
        condition = data["weather"][0]["main"].lower()
        set_bg(condition)

        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        desc = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]

        col1, col2 = st.columns([2,1])

        with col1:
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.15);
                        padding:30px;
                        border-radius:20px;
                        backdrop-filter:blur(10px)">
                <h2>{city}</h2>
                <img src="http://openweathermap.org/img/wn/{icon}@2x.png">
                <h1>{temp}{unit}</h1>
                <p>{desc}</p>
                <p>Feels like: {feels}{unit}</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.metric("Humidity", f"{humidity}%")
            st.metric("Wind", f"{wind} {'m/s' if unit_api=='metric' else 'mph'}")

        # ================= FORECAST =================
        st.subheader("5-Day Forecast")

        forecast = get_forecast(city)

        if forecast["cod"] == "200":
            cols = st.columns(5)

            for i, col in enumerate(cols):
                item = forecast["list"][i*8]  # mỗi ngày
                t = item["main"]["temp"]
                icon = item["weather"][0]["icon"]

                col.markdown(f"""
                <div style="text-align:center">
                    <img src="http://openweathermap.org/img/wn/{icon}.png">
                    <p>{t}{unit}</p>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.error("City not found")