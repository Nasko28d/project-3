import streamlit as st

st.set_page_config(page_title="Температурни Ефекти", page_icon="🌡️", layout="centered")

st.title("🌡️ AI Температурен асистент")

# 1. Превключване между Целзий и Фаренхайт
unit = st.radio("Избери мерна единица:", ["Целзий (°C)", "Фаренхайт (°F)"], horizontal=True)

# Конфигуриране на границите и стойностите по подразбиране спрямо мерната единица
if unit == "Целзий (°C)":
    min_temp, max_temp, default_temp = -50, 60, 20
    label = "Въведи температурата в °C:"
else:
    min_temp, max_temp, default_temp = -58, 140, 68
    label = "Въведи температурата в °F:"

# Поле за въвеждане на температура
input_temp = st.number_input(label, min_value=min_temp, max_value=max_temp, value=default_temp)

# Превръщане на стойността винаги в Целзий за вътрешната логика на анимациите и скалата
if unit == "Фаренхайт (°F)":
    temp_in_celsius = (input_temp - 32) * 5 / 9
else:
    temp_in_celsius = input_temp

# 2. Изчисляване на процента за запълване на термометъра (базирано на скалата по Целзий -50 до +60)
percentage = ((temp_in_celsius - (-50)) / (60 - (-50))) * 100
percentage = max(0, min(100, percentage))

# 3. Конфигурация на ефектите и съветите спрямо Целзий
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

# Генериране на динамични текстове за деленията на скалата спрямо избраната единица
if unit == "Целзий (°C)":
    ticks = ["60°C", "40°C", "20°C", "0°C", "-20°C", "-40°C"]
else:
    ticks = ["140°F", "104°F", "68°F", "32°F", "-4°F", "-40°F"]

ticks_html = "".join([f'<div style="height: 40px; display: flex; align-items: center; color: white; font-size: 12px; font-weight: bold;">— {t}</div>' for t in ticks])

# 4. Визуализация на графичния термометър със СКАЛА
st.markdown(f"""
<div style="display: flex; flex-direction: column; align-items: center; margin: 30px 0; background: rgba(255,255,255,0.1); padding: 25px; border-radius: 15px; backdrop-filter: blur(5px); box-shadow: 0 8px 32px 0 rgba(0,0,0,0.2);">
    <h3 style="color: white; margin-bottom: 20px;">Графичен Термометър със Скала</h3>
    
    <div style="display: flex; align-items: flex-start; justify-content: center; width: 150px; height: 260px; position: relative;">
        <!-- Стъклено тяло на термометъра -->
        <div style="width: 35px; height: 250px; background: #e2e8f0; border-radius: 20px; border: 4px solid #cbd5e1; position: relative; overflow: hidden; display: flex; align-items: flex-end; z-index: 2;">
            <!-- Течност -->
            <div style="width: 100%; height: {percentage}%; background: {thermometer_color}; transition: height 0.6s cubic-bezier(0.1, 0.8, 0.3, 1); border-radius: 0 0 12px 12px;"></div>
        </div>
        
        <!-- Разчертана скала отстрани -->
        <div style="display: flex; flex-direction: column; justify-content: space-between; height: 240px; margin-left: 10px; padding-top: 5px; z-index: 2;">
            {ticks_html}
        </div>
    </div>
    
    <div style="color: white; font-size: 28px; font-weight: bold; margin-top: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.4);">
        {input_temp:.1f} °{'C' if unit == 'Целзий (°C)' else 'F'}
    </div>
</div>
""", unsafe_allow_html=True)

# 5. Глобален CSS за фон и летящи емоджита
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
