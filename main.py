import streamlit as st
import requests

# ===== CONFIG =====
API_KEY = "YOUR_API_KEY"

st.set_page_config(page_title="Weather App", layout="wide")

# ===== CSS (cho đẹp giống hình) =====
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #4facfe, #00f2fe);
        color: white;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        background: rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ===== TITLE =====
st.title("🌤 Weather App")

# ===== SEARCH =====
city = st.text_input("🔍 Enter city:", "Hanoi")

# ===== FUNCTION =====
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    return res.json()

# ===== MAIN =====
if city:
    data = get_weather(city)

    if data.get("cod") == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        # ===== DISPLAY =====
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="card">
                <h2>{city}</h2>
                <h1>{temp}°C</h1>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="card">
                <h3>💧 Humidity</h3>
                <h2>{humidity}%</h2>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="card">
                <h3>🌬 Wind</h3>
                <h2>{wind} m/s</h2>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.error("❌ City not found!")