import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Температурен помощник", page_icon="🌡️")
st.title("🌡️ Температурен помощник с AI Анимации")

# Функция за зареждане на Lottie анимация от мрежата
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# AI-генерирани Lottie анимации за различните състояния на времето
lottie_cold = load_lottieurl("https://lottiefiles.com") # Снежинка/Зима
lottie_cool = load_lottieurl("https://lottiefiles.com")  # Вятър/Есен
lottie_warm = load_lottieurl("https://lottiefiles.com")  # Слънчево/Приятно
lottie_hot  = load_lottieurl("https://lottiefiles.com")  # Пустиня/Жега

# Поле за въвеждане на температура
temperature = st.number_input(
    "Въведи температурата в °C:",
    min_value=-50,
    max_value=60,
    value=20
)

st.metric(label="Текуща температура", value=f"{temperature} °C")

# Динамична промяна на съветите и анимациите в реално време
if temperature < 10:
    st.info("Студено е! Облечи топло яке. 🧥")
    if lottie_cold:
        st_lottie(lottie_cold, height=200, key="cold")

elif temperature < 20:
    st.warning("Прохладно е. Подходящо е леко яке. 🧣")
    if lottie_cool:
        st_lottie(lottie_cool, height=200, key="cool")

elif temperature < 30:
    st.success("Приятно топло е! ☀️")
    if lottie_warm:
        st_lottie(lottie_warm, height=200, key="warm")

else:
    st.error("Много е горещо! Пий повече вода. 💧")
    if lottie_hot:
        st_lottie(lottie_hot, height=200, key="hot")
