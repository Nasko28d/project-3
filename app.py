import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Температурни Ефекти", page_icon="🌡️", layout="centered")

st.title("🌡️ Температурен асистент с AI Ефекти")

# Поле за температура
temperature = st.number_input(
    "Въведи температурата в °C:",
    min_value=-50,
    max_value=60,
    value=20
)

# Настройка на ефектите спрямо температурата
if temperature < 10:
    st.info("❄️ Студено е! Облечи топло яке.")
    bg_gradient = "linear-gradient(135deg, #1e3a8a, #3b82f6)" # Студено синьо
    emoji = "❄️"
    speed = 1.5
    direction = "down"

elif temperature < 20:
    st.warning("🍃 Прохладно е. Подходящо е леко яке.")
    bg_gradient = "linear-gradient(135deg, #2d3748, #4a5568)" # Есенно сиво-зелено
    emoji = "🍃"
    speed = 2.5
    direction = "down"

elif temperature < 35:
    st.success("☀️ Приятно топло е!")
    bg_gradient = "linear-gradient(135deg, #15803d, #22c55e)" # Свежо пролетно зелено
    emoji = "☀️"
    speed = 0.8
    direction = "down"

else:
    st.error("🔥 Много е горещо! Пий повече вода.")
    bg_gradient = "linear-gradient(135deg, #7f1d1d, #ef4444)" # Горещо червено
    emoji = "🔥"
    speed = 4.0
    direction = "up"

# Пълна интеграция на HTML + CSS анимация за фон и плаващи емоджита
animation_html = f"""
<style>
    /* Динамичен преливащ фон за цялата страница */
    body, html {{
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        background: {bg_gradient};
        overflow: hidden;
        font-family: sans-serif;
    }}
    
    /* Контейнер за анимацията */
    .animation-container {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1;
        pointer-events: none;
    }}

    /* Стил за плаващите емоджи частици */
    .particle {{
        position: absolute;
        font-size: 24px;
        user-select: none;
        opacity: 0.8;
    }}
</style>

<div class="animation-container" id="container"></div>

<script>
    const container = document.getElementById('container');
    const emojiSymbol = "{emoji}";
    const moveSpeed = {speed};
    const moveDirection = "{direction}";
    const particleCount = 40;

    class FloatingEmoji {{
        constructor() {{
            this.element = document.createElement('div');
            this.element.className = 'particle';
            this.element.innerText = emojiSymbol;
            container.appendChild(this.element);
            this.reset();
            // Разхвърляме ги първоначално по екрана за по-естествен старт
            this.y = Math.random() * window.innerHeight; 
        }}

        reset() {{
            this.x = Math.random() * window.innerWidth;
            this.y = moveDirection === 'up' ? window.innerHeight + 50 : -50;
            this.size = Math.random() * 20 + 15; // Различен размер за дълбочина
            this.element.style.fontSize = this.size + 'px';
            this.speedFactor = Math.random() * 1 + 0.5;
            this.wobble = Math.random() * 2;
            this.wobbleSpeed = Math.random() * 0.02 + 0.01;
        }}

        update() {{
            // Движение нагоре или надолу
            if (moveDirection === 'up') {{
                this.y -= moveSpeed * this.speedFactor;
            }} else {{
                this.y += moveSpeed * this.speedFactor;
            }}

            // Леко криволичене (wobble) настрани за по-жива анимация
            this.wobble += this.wobbleSpeed;
            this.x += Math.sin(this.wobble) * 0.5;

            // Прилагане на новите координати
            this.element.style.transform = `translate(${{this.x}}px, ${{this.y}}px)`;

            // Проверка дали елементът е излязъл извън екрана
            if (moveDirection === 'up' && this.y < -50) this.reset();
            if (moveDirection === 'down' && this.y > window.innerHeight + 50) this.reset();
        }}
    }}

    const particles = [];
    for (let i = 0; i < particleCount; i++) {{
        particles.push(new FloatingEmoji());
    }}

    function animate() {{
        particles.forEach(p => p.update());
        requestAnimationFrame(animate);
    }}

    animate();

    // Преизчисляване при преоразмеряване на прозореца
    window.addEventListener('resize', () => {{
        particles.forEach(p => p.reset());
    }});
</script>
"""

# Инжектираме HTML/CSS ефекта като пълен фонов тапет
components.html(animation_html, height=1000, scrolling=False)
