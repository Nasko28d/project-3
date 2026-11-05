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

# Конфигурация на ефектите спрямо температурата
if temperature < 10:
    st.info("❄️ Студено е! Облечи топло яке.")
    bg_gradient = "linear-gradient(135deg, #1e3a8a, #3b82f6)" # Студено синьо
    emoji = "❄️"
    speed = "10s" # По-бавно падане
    direction = "normal"

elif temperature < 20:
    st.warning("🍃 Прохладно е. Подходящо е леко яке.")
    bg_gradient = "linear-gradient(135deg, #2d3748, #4a5568)" # Есенно сиво-зелено
    emoji = "🍃"
    speed = "7s" 
    direction = "normal"

elif temperature < 35:
    st.success("☀️ Приятно топло е!")
    bg_gradient = "linear-gradient(135deg, #15803d, #22c55e)" # Свежо пролетно зелено
    emoji = "☀️"
    speed = "12s" 
    direction = "normal"

else:
    st.error("🔥 Много е горещо! Пий повече вода.")
    bg_gradient = "linear-gradient(135deg, #7f1d1d, #ef4444)" # Горещо червено
    emoji = "🔥"
    speed = "4s" # Бързо летене нагоре
    direction = "reverse" # Обръщаме посоката (нагоре)

# Инжектиране на CSS анимация директно в главното приложение на Streamlit
st.markdown(f"""
<style>
    /* Промяна на основния фон на Streamlit */
    .stApp {{
        background: {bg_gradient} !important;
        transition: background 0.5s ease-in-out;
    }}
    
    /* Промяна на текстовете, за да се четат на тъмен фон */
    h1, p, label, .stMarkdown {{
        color: white !important;
    }}
    
    /* Контейнер за падащите/летящите емоджита */
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

    /* CSS анимация за движение */
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
    
    /* Различни стартови позиции и закъснения за емоджитата */
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
