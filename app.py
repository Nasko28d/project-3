import streamlit as st

st.set_page_config(page_title="Температурни Ефекти", page_icon="🌡️", layout="centered")

st.title("🌡️ AI Температурен асистент")

# 1. Избор на мерна единица
unit = st.radio("Избери мерна единица:", ["Целзий (°C)", "Фаренхайт (°F)"], horizontal=True)

# Защита при смяна на единиците чрез уникален ключ (key)
if unit == "Целзий (°C)":
    min_temp, max_temp, default_temp = -50, 60, 20
    label = "Настройте температурата в °C:"
    input_key = "celsius_slider"
else:
    min_temp, max_temp, default_temp = -58, 140, 68
    label = "Настройте температурата в °F:"
    input_key = "fahrenheit_slider"

# Използваме st.slider вместо st.number_input за максимално улеснено въвеждане
input_temp = st.slider(
    label, 
    min_value=float(min_temp), 
    max_value=float(max_temp), 
    value=float(default_temp), 
    step=0.5,
    key=input_key
)

# Превръщане на стойността в Целзий за логиката на анимацията
if unit == "Фаренхайт (°F)":
    temp_in_celsius = (input_temp - 32) * 5 / 9
else:
    temp_in_celsius = input_temp

# 2. Изчисляване на процента за термометъра
percentage = ((temp_in_celsius - (-50)) / (60 - (-50))) * 100
percentage = max(0, min(100, percentage))

# 3. Конфигурация на ефектите и съветите
if temp_in_celsius < 10:
    st.info(f"❄️ Студено е! Облечи топло яке. ({input_temp:.1f} °{'C' if unit == 'Целзий (°C)' else 'F'})")
    bg_gradient = "linear-gradient(135deg, #1e3a8a, #3b82f6)"
    thermometer_color = "#3b82f6"
    emoji = "❄️"
    speed = "10s"
    direction = "normal"
elif temp_in_celsius < 20:
    st.warning(f"🍃 Прохладно е. Подходящо е леко яке. ({input_temp:.1f} °{'C' if unit == 'Целзий (°C)' else 'F'})")
    bg_gradient = "linear-gradient(135deg, #2d3748, #4a5568)"
    thermometer_color = "#94a3b8"
    emoji = "🍃"
    speed = "7s" 
    direction = "normal"
elif temp_in_celsius < 35:
    st.success(f"☀️ Приятно топло е! ({input_temp:.1f} °{'C' if unit == 'Целзий (°C)' else 'F'})")
    bg_gradient = "linear-gradient(135deg, #15803d, #22c55e)"
    thermometer_color = "#22c55e"
    emoji = "☀️"
    speed = "12s" 
    direction = "normal"
else:
    st.error(f"🔥 Много е горещо! Пий повече вода. ({input_temp:.1f} °{'C' if unit == 'Целзий (°C)' else 'F'})")
    bg_gradient = "linear-gradient(135deg, #7f1d1d, #ef4444)"
    thermometer_color = "#ef4444"
    emoji = "🔥"
    speed = "4s"
    direction = "reverse"

# Динамична скала
if unit == "Целзий (°C)":
    ticks = ["60°C", "40°C", "20°C", "0°C", "-20°C", "-40°C"]
else:
    ticks = ["140°F", "104°F", "68°F", "32°F", "-4°F", "-40°F"]

ticks_html = "".join([f'<div style="height: 40px; display: flex; align-items: center; color: white; font-size: 12px; font-weight: bold;">— {t}</div>' for t in ticks])

# 4. Рендериране на термометъра
st.markdown(f"""
<div style="display: flex; flex-direction: column; align-items: center; margin: 30px 0; background: rgba(255,255,255,0.1); padding: 25px; border-radius: 15px; backdrop-filter: blur(5px); box-shadow: 0 8px 32px 0 rgba(0,0,0,0.2);">
    <h3 style="color: white; margin-bottom: 20px;">Графичен Термометър със Скала</h3>
    <div style="display: flex; align-items: flex-start; justify-content: center; width: 150px; height: 260px; position: relative;">
        <div style="width: 35px; height: 250px; background: #e2e8f0; border-radius: 20px; border: 4px solid #cbd5e1; position: relative; overflow: hidden; display: flex; align-items: flex-end; z-index: 2;">
            <div style="width: 100%; height: {percentage}%; background: {thermometer_color}; transition: height 0.6s cubic-bezier(0.1, 0.8, 0.3, 1); border-radius: 0 0 12px 12px;"></div>
        </div>
        <div style="display: flex; flex-direction: column; justify-content: space-between; height: 240px; margin-left: 10px; padding-top: 5px; z-index: 2;">
            {ticks_html}
        </div>
    </div>
    <div style="color: white; font-size: 28px; font-weight: bold; margin-top: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.4);">
        {input_temp:.1f} °{'C' if unit == 'Целзий (°C)' else 'F'}
    </div>
</div>
""", unsafe_allow_html=True)

# 5. Глобален CSS
st.markdown(f"""
<style>
    .stApp {{
        background: {bg_gradient} !important;
        transition: background 0.7s ease-in-out;
    }}
    
    h1, h3, p, label, .stMarkdown, .stRadio {{
        color: white !important;
    }}
    
    div[data-testid="stRadio"] label p {{
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
        font-size: 32px;
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
            opacity: 0.1;
        }}
    }}
    
    .e1 {{ left: 8%; animation-delay: 0s; }}
    .e2 {{ left: 23%; animation-delay: 2.5s; font-size: 22px; }}
    .e3 {{ left: 38%; animation-delay: 4.5s; font-size: 38px; }}
    .e4 {{ left: 53%; animation-delay: 1.2s; }}
    .e5 {{ left: 68%; animation-delay: 5.2s; font-size: 24px; }}
    .e6 {{ left: 83%; animation-delay: 3.2s; font-size: 42px; }}
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
