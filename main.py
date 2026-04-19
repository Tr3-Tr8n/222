import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Weather Lite", layout="wide")

API_KEY = "e86853326847343e8313ca9b65fe7bbc"   # ← thay key

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
       
forecast = get_forecast(city)

if str(forecast.get("cod")) == "200":

    # ===== PREPARE DATA =====
    dates = []
    temps = []

    for item in forecast["list"]:
        date = item["dt_txt"].split(" ")[0]
        temp = item["main"]["temp"]

        dates.append(date)
        temps.append(temp)

    df = pd.DataFrame({"date": dates, "temp": temps})

    # ===== GROUP BY DAY =====
    daily = df.groupby("date").mean().reset_index()

    # ===== CONVERT TO X, Y =====
    daily["day_num"] = range(len(daily))
    X = daily["day_num"]
    Y = daily["temp"]

    # ===== LINEAR REGRESSION (manual) =====
    n = len(X)
    mean_x = X.mean()
    mean_y = Y.mean()

    numerator = ((X - mean_x) * (Y - mean_y)).sum()
    denominator = ((X - mean_x)**2).sum()

    m = numerator / denominator   # slope
    b = mean_y - m * mean_x       # intercept

    # ===== PREDICT NEXT DAYS =====
    future_days = []
    future_temps = []

    last_day = X.iloc[-1]

    for i in range(2):  # thêm 2 ngày → tổng 7 ngày
        new_x = last_day + i + 1
        pred = m * new_x + b

        future_days.append(f"Day+{i+1}")
        future_temps.append(pred)

    pred_df = pd.DataFrame({
        "date": list(daily["date"]) + future_days,
        "temp": list(daily["temp"]) + future_temps
    })

    # ===== DISPLAY =====
    st.subheader(" AI 7-Day Prediction")
    st.line_chart(pred_df.set_index("date"))

    st.dataframe(pred_df)

    # ===== ACCURACY (simple confidence) =====
    error = abs(Y - (m*X + b)).mean()
    confidence = max(0, 100 - error*5)

   