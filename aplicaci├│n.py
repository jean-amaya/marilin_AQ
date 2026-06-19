import base64
from pathlib import Path
from urllib.parse import quote

import streamlit as st

# =====================================================
# DATOS DEL NEGOCIO
# =====================================================
BUSINESS_NAME = "Marilin Amaya"
PROFESSION = "Psicóloga"
BRAND_LINE = "Te acompaño en tu proceso de bienestar emocional y desarrollo personal."
PHONE_DISPLAY = "+51 934 386 532"
PHONE_WHATSAPP = "51934386532"
SCHEDULE = "Lunes a sábado | 9:00 a. m. - 6:00 p. m."
CITY = "Perú"

# Cambiar cuando tenga los enlaces reales:
INSTAGRAM_URL = "https://www.instagram.com/"
FACEBOOK_URL = "https://www.facebook.com/"

WA_TEXT = quote("Hola Marilin, deseo información para agendar una cita de asesoramiento psicológico.")
WHATSAPP_URL = f"https://wa.me/{PHONE_WHATSAPP}?text={WA_TEXT}"

# =====================================================
# CONFIGURACIÓN STREAMLIT
# =====================================================
st.set_page_config(
    page_title="Marilin Amaya | Psicología y Bienestar",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =====================================================
# BÚSQUEDA ROBUSTA DE ARCHIVOS
# Evita FileNotFoundError aunque cambie la ubicación o extensión.
# Según tu GitHub:
# - logo_b64.jpeg = portada
# - logo_marilin_amaya.png = logo principal
# =====================================================
BASE_DIR = Path(__file__).resolve().parent


def find_file(file_names: list[str]) -> Path | None:
    """Busca archivos en la raíz y carpetas comunes. También compara sin distinguir mayúsculas/minúsculas."""
    folders = [
        BASE_DIR,
        BASE_DIR / "assets",
        BASE_DIR / "imagenes",
        BASE_DIR / "images",
        BASE_DIR / "img",
        BASE_DIR / "static",
    ]

    # Búsqueda exacta
    for folder in folders:
        for file_name in file_names:
            path = folder / file_name
            if path.exists() and path.is_file():
                return path

    # Búsqueda tolerante a mayúsculas/minúsculas
    desired = {name.lower() for name in file_names}
    for folder in folders:
        if folder.exists() and folder.is_dir():
            for item in folder.iterdir():
                if item.is_file() and item.name.lower() in desired:
                    return item

    return None


def get_mime_type(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in [".jpg", ".jpeg"]:
        return "image/jpeg"
    if suffix == ".webp":
        return "image/webp"
    if suffix == ".svg":
        return "image/svg+xml"
    return "image/png"


def image_to_data_uri(path: Path | None) -> str:
    """Convierte imagen a data URI. Si no existe, devuelve vacío y la app continúa."""
    if path is None or not path.exists() or not path.is_file():
        return ""
    try:
        encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
        return f"data:{get_mime_type(path)};base64,{encoded}"
    except Exception:
        return ""


# Nombres reales de tu repositorio + nombres alternativos por seguridad
PORTADA_PATH = find_file([
    "logo_b64.jpeg",      # PORTADA según tu GitHub
    "logo_b64.jpg",
    "logo_b64.png",
    "portada_marilin_amaya.png",
    "portada_marilin_amaya.jpg",
    "portada.png",
    "portada.jpg",
])

LOGO_PATH = find_file([
    "logo_marilin_amaya.png",  # LOGO principal según tu GitHub
    "logo_marilin_amaya.jpg",
    "logo_marilin_amaya.jpeg",
    "logo.png",
    "logo.jpg",
])

PORTADA_URI = image_to_data_uri(PORTADA_PATH)
LOGO_URI = image_to_data_uri(LOGO_PATH)

# =====================================================
# CSS
# =====================================================
st.markdown(
    """
    <style>
    :root {
        --cream: #fffaf4;
        --bg: #f7f2ec;
        --sage: #8c9b78;
        --sage-dark: #667356;
        --lilac: #a991b3;
        --gold: #c8a14a;
        --text: #3d3935;
        --muted: #716c66;
        --card: rgba(255, 250, 244, 0.92);
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(140,155,120,0.22), transparent 34%),
            radial-gradient(circle at bottom right, rgba(169,145,179,0.18), transparent 36%),
            var(--bg);
        color: var(--text);
    }

    header[data-testid="stHeader"] { background: transparent; }

    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 4rem;
        max-width: 1180px;
    }

    .hero-card {
        background: linear-gradient(135deg, rgba(255,250,244,0.96), rgba(244,239,230,0.92));
        border: 1px solid rgba(200,161,74,0.28);
        border-radius: 32px;
        padding: 1.15rem;
        box-shadow: 0 18px 45px rgba(61,57,53,0.08);
        overflow: hidden;
    }

    .portada-img {
        width: 100%;
        max-height: 360px;
        object-fit: cover;
        border-radius: 24px;
        border: 1px solid rgba(140,155,120,0.16);
        display: block;
    }

    .portada-fallback {
        min-height: 300px;
        border-radius: 24px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        background:
            radial-gradient(circle at top left, rgba(140,155,120,0.26), transparent 35%),
            radial-gradient(circle at bottom right, rgba(169,145,179,0.22), transparent 38%),
            linear-gradient(135deg, #fffaf4, #f4efe6);
        border: 1px solid rgba(140,155,120,0.16);
    }

    .portada-fallback h1 {
        color: var(--lilac);
        font-family: Georgia, 'Times New Roman', serif;
        font-size: clamp(2.4rem, 7vw, 5rem);
        letter-spacing: 0.11em;
        margin: 0;
    }

    .portada-fallback p {
        color: var(--sage-dark);
        font-size: 1.15rem;
        margin-top: 0.7rem;
    }

    .hero-content {
        display: grid;
        grid-template-columns: 170px 1fr;
        gap: 1.5rem;
        align-items: center;
        padding: 1.4rem 1rem 0.7rem 1rem;
    }

    .logo-img {
        width: 160px;
        height: 160px;
        object-fit: cover;
        border-radius: 999px;
        border: 5px solid #fffaf4;
        box-shadow: 0 12px 30px rgba(61,57,53,0.14);
        background: white;
    }

    .logo-fallback {
        width: 160px;
        height: 160px;
        border-radius: 999px;
        border: 5px solid #fffaf4;
        background: white;
        box-shadow: 0 12px 30px rgba(61,57,53,0.14);
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--lilac);
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 3.6rem;
        font-weight: 500;
    }

    .eyebrow {
        color: var(--sage-dark);
        text-transform: uppercase;
        letter-spacing: 0.18em;
        font-size: 0.78rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .hero-title {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: clamp(2.2rem, 5vw, 4.8rem);
        line-height: 0.98;
        font-weight: 500;
        letter-spacing: 0.08em;
        color: var(--lilac);
        margin: 0;
        text-transform: uppercase;
    }

    .hero-subtitle {
        margin-top: 0.45rem;
        font-size: clamp(1rem, 2vw, 1.35rem);
        color: var(--sage-dark);
        letter-spacing: 0.22em;
        text-transform: uppercase;
        font-weight: 600;
    }

    .hero-text {
        font-size: 1.08rem;
        color: var(--muted);
        max-width: 760px;
        margin-top: 0.9rem;
        line-height: 1.7;
    }

    .cta-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
        margin-top: 1.25rem;
    }

    .btn-primary, .btn-secondary {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        text-decoration: none !important;
        border-radius: 999px;
        padding: 0.86rem 1.35rem;
        font-weight: 700;
        border: 1px solid transparent;
    }

    .btn-primary {
        background: var(--sage);
        color: white !important;
        box-shadow: 0 12px 24px rgba(102,115,86,0.22);
    }

    .btn-secondary {
        color: var(--sage-dark) !important;
        border-color: rgba(102,115,86,0.26);
        background: rgba(255,255,255,0.58);
    }

    .section-title {
        font-size: clamp(1.7rem, 3vw, 2.35rem);
        margin: 2.4rem 0 0.7rem 0;
        color: var(--text);
        font-weight: 750;
    }

    .section-intro {
        color: var(--muted);
        max-width: 900px;
        line-height: 1.7;
        font-size: 1.03rem;
        margin-bottom: 1.2rem;
    }

    .cards-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }

    .service-card, .info-card, .step-card, .contact-card {
        background: var(--card);
        border: 1px solid rgba(200,161,74,0.18);
        border-radius: 24px;
        padding: 1.2rem;
        box-shadow: 0 14px 30px rgba(61,57,53,0.06);
        height: 100%;
    }

    .service-icon { font-size: 1.9rem; margin-bottom: 0.5rem; }

    .service-card h3, .info-card h3, .step-card h3 {
        margin: 0 0 0.5rem 0;
        color: var(--sage-dark);
        font-size: 1.1rem;
    }

    .service-card p, .info-card p, .step-card p {
        color: var(--muted);
        line-height: 1.6;
        margin: 0;
        font-size: 0.98rem;
    }

    .two-col {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin-top: 1rem;
    }

    .quote-box {
        margin-top: 2rem;
        padding: 2rem;
        border-radius: 28px;
        background: linear-gradient(135deg, rgba(140,155,120,0.20), rgba(169,145,179,0.16));
        border: 1px solid rgba(200,161,74,0.18);
        text-align: center;
    }

    .quote-box h2 {
        font-family: Georgia, 'Times New Roman', serif;
        color: var(--lilac);
        font-size: clamp(1.8rem, 4vw, 3rem);
        font-weight: 500;
        margin-bottom: 0.6rem;
    }

    .contact-card {
        margin-top: 2rem;
        border-radius: 32px;
        padding: 1.6rem;
    }

    .contact-grid {
        display: grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 1.2rem;
        align-items: center;
    }

    .contact-number {
        font-size: clamp(1.6rem, 3vw, 2.35rem);
        color: var(--sage-dark);
        font-weight: 800;
        margin: 0.4rem 0;
    }

    .notice {
        background: rgba(255,255,255,0.62);
        border-left: 4px solid var(--gold);
        padding: 1rem 1.1rem;
        border-radius: 18px;
        color: var(--muted);
        line-height: 1.55;
        font-size: 0.95rem;
    }

    .footer {
        text-align: center;
        color: var(--muted);
        font-size: 0.9rem;
        margin-top: 2rem;
        padding-bottom: 1rem;
    }

    @media (max-width: 900px) {
        .hero-content, .two-col, .contact-grid { grid-template-columns: 1fr; }
        .cards-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .logo-img, .logo-fallback { width: 130px; height: 130px; }
    }

    @media (max-width: 560px) {
        .cards-grid { grid-template-columns: 1fr; }
        .hero-card, .contact-card { border-radius: 22px; padding: 0.8rem; }
        .hero-content { padding: 1rem 0.4rem 0.4rem 0.4rem; }
        .hero-subtitle { letter-spacing: 0.15em; }
        .cta-row a { width: 100%; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# HTML DINÁMICO SIN ERROR POR ARCHIVOS FALTANTES
# =====================================================
if PORTADA_URI:
    portada_html = f'<img class="portada-img" src="{PORTADA_URI}" alt="Portada de Marilin Amaya Psicóloga">'
else:
    portada_html = f'''
    <div class="portada-fallback">
        <div>
            <div class="eyebrow">Psicología y bienestar</div>
            <h1>{BUSINESS_NAME}</h1>
            <p>{BRAND_LINE}</p>
        </div>
    </div>
    '''

if LOGO_URI:
    logo_html = f'<img class="logo-img" src="{LOGO_URI}" alt="Logo de Marilin Amaya Psicóloga">'
else:
    logo_html = '<div class="logo-fallback">MA</div>'

# =====================================================
# PORTADA
# =====================================================
st.markdown(
    f"""
    <section class="hero-card">
        {portada_html}
        <div class="hero-content">
            <div>{logo_html}</div>
            <div>
                <div class="eyebrow">Psicología y bienestar</div>
                <h1 class="hero-title">{BUSINESS_NAME}</h1>
                <div class="hero-subtitle">{PROFESSION}</div>
                <p class="hero-text">
                    {BRAND_LINE} Atención orientada a la escucha, la confidencialidad y el acompañamiento profesional.
                </p>
                <div class="cta-row">
                    <a class="btn-primary" href="{WHATSAPP_URL}" target="_blank">Agendar cita por WhatsApp</a>
                    <a class="btn-secondary" href="#servicios">Ver servicios</a>
                </div>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# SERVICIOS
# =====================================================
st.markdown('<h2 class="section-title" id="servicios">Servicios de asesoramiento psicológico</h2>', unsafe_allow_html=True)
st.markdown(
    '<p class="section-intro">Espacio profesional dirigido a fortalecer el bienestar emocional, el autoconocimiento y las estrategias personales para afrontar situaciones cotidianas.</p>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="cards-grid">
        <div class="service-card">
            <div class="service-icon">🌿</div>
            <h3>Bienestar emocional</h3>
            <p>Orientación para reconocer emociones, ordenar pensamientos y fortalecer el equilibrio personal.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">🧘</div>
            <h3>Estrés y ansiedad</h3>
            <p>Acompañamiento para identificar detonantes y aplicar estrategias de manejo cotidiano.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">🤍</div>
            <h3>Autoestima</h3>
            <p>Fortalecimiento de la seguridad personal, autovaloración y toma de decisiones conscientes.</p>
        </div>
        <div class="service-card">
            <div class="service-icon">🤝</div>
            <h3>Relaciones saludables</h3>
            <p>Orientación para mejorar comunicación, límites, vínculos y resolución de conflictos.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# ENFOQUE
# =====================================================
st.markdown('<h2 class="section-title">Enfoque de atención</h2>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="two-col">
        <div class="info-card">
            <h3>Espacio seguro y confidencial</h3>
            <p>La atención se realiza desde una comunicación respetuosa, ética y centrada en la persona.</p>
        </div>
        <div class="info-card">
            <h3>Atención previa cita</h3>
            <p>Las sesiones se coordinan por WhatsApp, según disponibilidad horaria y modalidad de atención.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="quote-box">
        <h2>Escucha. Comprende. Acompaña.</h2>
        <p>Un proceso psicológico puede ayudarte a mirar con mayor claridad lo que sientes, piensas y necesitas.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# PASOS
# =====================================================
st.markdown('<h2 class="section-title">¿Cómo agendar una cita?</h2>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="cards-grid">
        <div class="step-card">
            <h3>1. Escribe por WhatsApp</h3>
            <p>Solicita información sobre disponibilidad, horarios y modalidad de atención.</p>
        </div>
        <div class="step-card">
            <h3>2. Indica tu motivo de consulta</h3>
            <p>Comparte información general para orientar la coordinación inicial.</p>
        </div>
        <div class="step-card">
            <h3>3. Coordina fecha y hora</h3>
            <p>Se confirma la cita según disponibilidad y condiciones del servicio.</p>
        </div>
        <div class="step-card">
            <h3>4. Inicia tu proceso</h3>
            <p>Recibe orientación profesional en un espacio de escucha y acompañamiento.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# CONTACTO
# =====================================================
st.markdown(
    f"""
    <section class="contact-card" id="contacto">
        <div class="contact-grid">
            <div>
                <div class="eyebrow">Contacto</div>
                <h2 class="section-title" style="margin-top:0.2rem;">Agenda tu cita</h2>
                <p class="section-intro" style="margin-bottom:0.4rem;">Comunícate directamente por WhatsApp para consultar disponibilidad y recibir información del servicio.</p>
                <p class="contact-number">{PHONE_DISPLAY}</p>
                <p style="color:var(--muted);"><strong>Horario:</strong> {SCHEDULE}<br><strong>Ubicación:</strong> {CITY}</p>
                <div class="cta-row">
                    <a class="btn-primary" href="{WHATSAPP_URL}" target="_blank">Enviar mensaje</a>
                    <a class="btn-secondary" href="{INSTAGRAM_URL}" target="_blank">Instagram</a>
                    <a class="btn-secondary" href="{FACEBOOK_URL}" target="_blank">Facebook</a>
                </div>
            </div>
            <div class="notice">
                <strong>Nota importante:</strong><br>
                Este sitio permite coordinar información y citas. No reemplaza servicios de emergencia. Si existe una situación de riesgo inmediato, acude al centro de emergencia más cercano o comunícate con una línea de ayuda local.
                <br><br>
                <strong>Dato profesional sugerido:</strong><br>
                Agregar N.° de colegiatura y condición de habilitación cuando corresponda.
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="footer">
        © {BUSINESS_NAME} | Psicología y bienestar emocional. Página web desarrollada en Python con Streamlit.
    </div>
    """,
    unsafe_allow_html=True,
)
