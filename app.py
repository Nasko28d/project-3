import streamlit as st

st.set_page_config(page_title="Температурни Ефекти", page_icon="🌡️", layout="centered")

st.title("🌡️ Температурен асистент с AI Ефекти")

# Поле за температура
temperature = st.number_input(
    "Въведи температурата в °C:",
    min_value=-50,
    max_value=60,
    value=20
)

# Изчисляване на процента за запълване на термометъра (скала от -50 до 60 градуса = 110 единици диапазон)
min_temp = -50
max_temp = 60
percentage = ((temperature - min_temp) / (max_temp - min_temp)) * 100
# Ограничаваме процента между 0% и 100% за безопасност на визуализацията
percentage = max(0, min(100, percentage))

# Конфигурация на ефектите спрямо температурата
if temperature < 10:
    st.info("❄️ Студено е! Облечи топло яке.")
    bg_gradient = "linear-gradient(135deg, #1e3a8a, #3b82f6)"
    thermometer_color = "#3b82f6" # Синя течност
    emoji = "❄️"
    speed = "10s"
    direction = "normal"

elif temperature < 20:
    st.warning("🍃 Прохладно е. Подходящо е леко яке.")
    bg_gradient = "linear-gradient(135deg, #2d3748, #4a5568)"
    thermometer_color = "#94a3b8" # Сива течност
    emoji = "🍃"
    speed = "7s" 
    direction = "normal"

elif temperature < 35:
    st.success("☀️ Приятно топло е!")
    bg_gradient = "linear-gradient(135deg, #15803d, #22c55e)"
    thermometer_color = "#22c55e" # Зелена течност
    emoji = "☀️"
    speed = "12s" 
    direction = "normal"

else:
    st.error("🔥 Много е горещо! Пий повече вода.")
    bg_gradient = "linear-gradient(135deg, #7f1d1d, #ef4444)"
    thermometer_color = "#ef4444" # Червена течност
    emoji = "🔥"
    speed = "4s"
    direction = "reverse"

# Визуализация на графичния термометър в самото приложение
st.markdown(f"""
<div style="display: flex; flex-direction: column; align-items: center; margin: 30px 0; background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; backdrop-filter: blur(5px);">
    <h3 style="color: white; margin-bottom: 15px;">Графичен Термометър</h3>
    <div style="width: 40px; height: 250px; background: #e2e8f0; border-radius: 20px; border: 4px solid #cbd5e1; position: relative; overflow: hidden; display: flex; align-items: flex-end;">
        <div style="width: 100%; height: {percentage}%; background: {thermometer_color}; transition: height 0.5s ease-in-out; border-radius: 0 0 12px 12px;"></div>
    </div>
    <div style="color: white; font-size: 24px; font-weight: bold; margin-top: 15px;">{temperature} °C</div>
</div>
""", unsafe_allow_html=True)

# Инжектиране на CSS за глобалния фон и летящите емоджита
st.markdown(f"""
<style>
    .stApp {{
        background: {bg_gradient} !important;
        transition: background 0.5s ease-in-out;
    }}
    
    h1, p, label, .stMarkdown {{
        color: white !important;
    }}
    
    .animation-holder {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 0;
        pointer-events: none;
        overflow: hidden;
    }}

    .falling-emoji {{
        position: absolute;
        top: -50px;
        font-size: 30px;
        animation: fly {speed} linear infinite;
        animation-direction: {direction};
    }}

    @keyframes fly {{
        0% {{
            transform: translateY(-50px) rotate(0deg);
            opacity: 1;
        }}
        100% {{
            transform: translateY(105vh) rotate(360deg);
            opacity: 0.2;
        }}
    }}
    
    .e1 {{ left: 10%; animation-delay: 0s; }}
    .e2 {{ left: 25%; animation-delay: 2s; font-size: 20px; }}
    .e3 {{ left: 40%; animation-delay: 4s; font-size: 35px; }}
    .e4 {{ left: 55%; animation-delay: 1s; }}
    .e5 {{ left: 70%; animation-delay: 5s; font-size: 22px; }}
    .e6 {{ left: 85%; animation-delay: 3s; font-size: 40px; }}
</style>

<div class="animation-holder">
    <div class="falling-emoji e1">{emoji}</div>
    <div class="falling-emoji e2">{emoji}</div>
    <div class="falling-emoji e3">{emoji}</div>
    <div class="falling-emoji e4">{emoji}</div>
    <div class="falling-emoji e5">{emoji}</div>
    <div class="falling-emoji e6">{emoji}</div>
</div>
""", unsafe_allow_html=True)
