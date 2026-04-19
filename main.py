        import streamlit as st
        import requests
        import pandas as pd
        import matplotlib.pyplot as plt
        from datetime import datetime
        import pydeck as pdk
        import streamlit.components.v1 as components

        # ================= CONFIG =================
        st.set_page_config(page_title="Weather Super App", layout="wide")
        API_KEY = "YOUR_NEW_API_KEY"   # ← THAY KEY MỚI

        # ================= STYLE =================
        st.markdown("""
        <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg,#1e3c72,#2a5298);
            color:white;
        }
        .card {
            background:rgba(255,255,255,0.15);
            padding:20px;
            border-radius:15px;
            backdrop-filter:blur(10px);
        }
        </style>
        """, unsafe_allow_html=True)

        # ================= SIDEBAR =================
        st.sidebar.title("⚙ Settings")

        unit = st.sidebar.radio("Unit", ["Celsius","Fahrenheit"])
        unit_api = "metric" if unit=="Celsius" else "imperial"
        unit_sym = "°C" if unit=="Celsius" else "°F"

        mode = st.sidebar.radio("Theme", ["Dark","Light"])
        if mode == "Light":
            st.markdown("""
            <style>
            [data-testid="stAppViewContainer"] { background:white; color:black; }
            </style>
            """, unsafe_allow_html=True)

        # ================= FUNCTIONS =================
        def get_weather(city):
            return requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={unit_api}"
            ).json()

        def get_forecast(city):
            return requests.get(
                f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={unit_api}"
            ).json()

        # ================= INPUT =================
        st.title("🌦 Weather Super App")
        city = st.text_input("Enter city", "London")

        # ================= MAIN =================
        if city:
            data = get_weather(city)

            if str(data.get("cod")) == "200":

                # ===== BASIC INFO =====
                temp = data["main"]["temp"]
                feels = data["main"]["feels_like"]
                humidity = data["main"]["humidity"]
                pressure = data["main"]["pressure"]
                wind = data["wind"]["speed"]
                desc = data["weather"][0]["description"]
                icon = data["weather"][0]["icon"]

                lat = data["coord"]["lat"]
                lon = data["coord"]["lon"]

                sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M")
                sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")

                # ===== UI =====
                col1, col2 = st.columns([2,1])

                with col1:
                    st.markdown(f"""
                    <div class='card'>
                        <h2>{city}</h2>
                        <img src='https://openweathermap.org/img/wn/{icon}@2x.png'>
                        <h1>{temp}{unit_sym}</h1>
                        <p>{desc}</p>
                        <p>Feels like: {feels}{unit_sym}</p>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    st.metric("Humidity", f"{humidity}%")
                    st.metric("Pressure", f"{pressure} hPa")
                    st.metric("Wind", f"{wind} {'m/s' if unit_api=='metric' else 'mph'}")
                    st.write(f"🌅 {sunrise} | 🌇 {sunset}")

                # ===== FORECAST =====
                forecast = get_forecast(city)

                if str(forecast.get("cod")) == "200":

                    temps, humidity_list, wind_list, dates = [], [], [], []

                    for item in forecast["list"][:8]:
                        temps.append(item["main"]["temp"])
                        humidity_list.append(item["main"]["humidity"])
                        wind_list.append(item["wind"]["speed"])
                        dates.append(item["dt_txt"][11:16])

                    # ===== LINE CHART =====
                    st.subheader("📈 Weather Trend")
                    fig, ax = plt.subplots()
                    ax.plot(dates, temps, label="Temp")
                    ax.plot(dates, humidity_list, label="Humidity")
                    ax.plot(dates, wind_list, label="Wind")
                    ax.legend()
                    st.pyplot(fig)

                    # ===== BAR CHART =====
                    st.subheader("📊 Temperature Bar Chart")
                    fig2, ax2 = plt.subplots()
                    ax2.bar(dates, temps)
                    st.pyplot(fig2)

                    # ===== PIE =====
                    st.subheader("🥧 Weather Ratio")
                    fig3, ax3 = plt.subplots()
                    ax3.pie([temps[0], humidity_list[0], wind_list[0]],
                            labels=["Temp","Humidity","Wind"],
                            autopct="%1.1f%%")
                    st.pyplot(fig3)

                # ===== MAP =====
                st.subheader("🗺 Location Map")
                st.pydeck_chart(pdk.Deck(
                    initial_view_state=pdk.ViewState(
                        latitude=lat, longitude=lon, zoom=10
                    ),
                    layers=[
                        pdk.Layer(
                            "ScatterplotLayer",
                            data=[{"lat":lat,"lon":lon}],
                            get_position="[lon, lat]",
                            get_radius=500,
                            get_color="[255,0,0]"
                        )
                    ]
                ))

                # ===== RADAR =====
                st.subheader("🌧 Rain Radar")
                components.iframe(
                    f"https://embed.windy.com/embed2.html?lat={lat}&lon={lon}&overlay=rain",
                    height=400
                )

                # ===== WIND MAP =====
                st.subheader("🌀 Wind Map")
                components.iframe(
                    f"https://embed.windy.com/embed2.html?lat={lat}&lon={lon}&overlay=wind",
                    height=400
                )

                # ===== AQI =====
                aqi = requests.get(
                    f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
                ).json()

                st.subheader("🌫 Air Quality")
                st.write("AQI:", aqi["list"][0]["main"]["aqi"])

                # ===== DOWNLOAD =====
                df = pd.DataFrame({
                    "Time": dates,
                    "Temp": temps,
                    "Humidity": humidity_list,
                    "Wind": wind_list
                })

                st.download_button("Download CSV", df.to_csv(index=False), "weather.csv")

            else:
                st.error("❌ City not found or API key not active")