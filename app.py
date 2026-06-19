import base64
from pathlib import Path

import streamlit as st


# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

st.set_page_config(
    page_title="Marilin Amaya Psicóloga",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent

# Archivos subidos en GitHub
PORTADA_PATH = BASE_DIR / "logo_b64.jpeg"
LOGO_PATH = BASE_DIR / "logo_marilin_amaya.png"

WHATSAPP_NUMBER = "51934386532"
WHATSAPP_TEXT = "Hola, deseo información para agendar una cita."
WHATSAPP_URL = f"https://wa.me/{WHATSAPP_NUMBER}?text={WHATSAPP_TEXT.replace(' ', '%20')}"


# =========================================================
# FUNCIONES
# =========================================================

def image_to_base64(path: Path) -> str | None:
    """Convierte una imagen local a base64. Si no existe, devuelve None."""
    try:
        if path.exists():
            with open(path, "rb") as file:
                return base64.b64encode(file.read()).decode()
        return None
    except Exception:
        return None


portada_b64 = image_to_base64(PORTADA_PATH)
logo_b64 = image_to_base64(LOGO_PATH)


# =========================================================
# ESTILOS
# =========================================================

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(180deg, #f7f1e8 0%, #fbf7ef 100%);
            color: #3d3936;
            font-family: 'Segoe UI', sans-serif;
        }

        header, footer {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
            max-width: 1100px;
        }

        .main-card {
            background: rgba(255, 252, 246, 0.92);
            border: 1px solid #ead8ba;
            border-radius: 24px;
            padding: 18px;
            box-shadow: 0 10px 28px rgba(114, 93, 64, 0.08);
            margin-bottom: 22px;
        }

        .cover-img {
            width: 100%;
            border-radius: 18px;
            display: block;
            border: 1px solid #ead8ba;
        }

        .cover-fallback {
            width: 100%;
            height: 260px;
            border-radius: 18px;
            background: linear-gradient(120deg, #f5eadf, #e8e0d3, #c9b6d5);
            border: 1px solid #ead8ba;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #8e7ca7;
            font-size: 34px;
            font-weight: 600;
            letter-spacing: 2px;
        }

        .profile-row {
            display: flex;
            gap: 28px;
            align-items: center;
            padding: 24px 16px 8px 16px;
        }

        .logo-img {
            width: 120px;
            height: 120px;
            object-fit: cover;
            border-radius: 50%;
            background: white;
            border: 4px solid #ffffff;
            box-shadow: 0 6px 18px rgba(85, 70, 50, 0.15);
        }

        .logo-fallback {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: #f7f1e8;
            border: 4px solid white;
            box-shadow: 0 6px 18px rgba(85, 70, 50, 0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #9b84ae;
            font-size: 42px;
            font-weight: 700;
        }

        .eyebrow {
            color: #89936f;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 10px;
        }

        .title {
            font-size: 34px;
            font-weight: 800;
            letter-spacing: 2px;
            color: #3f3b39;
            margin-bottom: 8px;
        }

        .subtitle {
            color: #605d59;
            font-size: 15px;
            line-height: 1.7;
            max-width: 720px;
            margin-bottom: 18px;
        }

        .btn-row {
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
        }

        .btn-primary {
            background: #8da079;
            color: white !important;
            padding: 12px 22px;
            border-radius: 999px;
            text-decoration: none !important;
            font-weight: 700;
            font-size: 14px;
            box-shadow: 0 6px 14px rgba(94, 110, 76, 0.24);
            display: inline-block;
        }

        .btn-secondary {
            background: white;
            color: #5f664e !important;
            padding: 12px 22px;
            border-radius: 999px;
            text-decoration: none !important;
            font-weight: 700;
            font-size: 14px;
            border: 1px solid #d8c8aa;
            display: inline-block;
        }

        h2 {
            color: #3f3b39;
            font-size: 30px !important;
            font-weight: 800 !important;
            margin-top: 10px !important;
            margin-bottom: 10px !important;
        }

        .section-text {
            color: #625f5b;
            font-size: 15px;
            line-height: 1.7;
            margin-bottom: 22px;
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
            margin-bottom: 16px;
        }

        .service-card {
            background: rgba(255, 252, 246, 0.96);
            border: 1px solid #ead8ba;
            border-radius: 18px;
            padding: 22px 20px;
            min-height: 180px;
            box-shadow: 0 6px 18px rgba(114, 93, 64, 0.06);
        }

        .service-icon {
            font-size: 26px;
            margin-bottom: 18px;
        }

        .service-title {
            color: #4f5540;
            font-weight: 800;
            margin-bottom: 12px;
            font-size: 15px;
        }

        .service-desc {
            color: #67625d;
            font-size: 13.5px;
            line-height: 1.7;
        }

        .focus-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 18px;
            margin-bottom: 20px;
        }

        .focus-card {
            background: rgba(255, 252, 246, 0.96);
            border: 1px solid #ead8ba;
            border-radius: 18px;
            padding: 22px;
            box-shadow: 0 6px 18px rgba(114, 93, 64, 0.05);
        }

        .focus-title {
            color: #4f5540;
            font-weight: 800;
            margin-bottom: 12px;
            font-size: 15px;
        }

        .phrase-box {
            background: linear-gradient(120deg, #e9e5d9 0%, #f3e8e5 50%, #eee1e7 100%);
            border: 1px solid #ead8ba;
            border-radius: 22px;
            padding: 42px 26px;
            text-align: center;
            margin: 28px 0 22px 0;
        }

        .phrase-main {
            color: #b29ac8;
            font-family: Georgia, serif;
            font-size: 38px;
            font-weight: 700;
            margin-bottom: 18px;
        }

        .phrase-sub {
            color: #58534e;
            font-size: 14px;
        }

        .steps-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
        }

        .step-card {
            background: rgba(255, 252, 246, 0.96);
            border: 1px solid #ead8ba;
            border-radius: 18px;
            padding: 22px 20px;
            min-height: 155px;
            box-shadow: 0 6px 18px rgba(114, 93, 64, 0.05);
        }

        .step-title {
            color: #4f5540;
            font-weight: 800;
            margin-bottom: 12px;
            font-size: 14px;
        }

        .step-desc {
            color: #67625d;
            font-size: 13px;
            line-height: 1.7;
        }

        .warning-box {
            background: #fdecec;
            border: 1px solid #f5c8c8;
            color: #7a3b3b;
            border-radius: 14px;
            padding: 14px 18px;
            font-size: 13px;
            line-height: 1.6;
            margin-top: 24px;
        }

        @media (max-width: 900px) {
            .services-grid,
            .steps-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .focus-grid {
                grid-template-columns: 1fr;
            }

            .profile-row {
                align-items: flex-start;
            }

            .title {
                font-size: 28px;
            }
        }

        @media (max-width: 600px) {
            .profile-row {
                flex-direction: column;
                text-align: left;
            }

            .services-grid,
            .steps-grid {
                grid-template-columns: 1fr;
            }

            .phrase-main {
                font-size: 30px;
            }

            .title {
                font-size: 25px;
            }

            .logo-img,
            .logo-fallback {
                width: 100px;
                height: 100px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# PANTALLA ÚNICA
# =========================================================

if portada_b64:
    portada_html = f'<img class="cover-img" src="data:image/jpeg;base64,{portada_b64}" alt="Portada Marilin Amaya Psicóloga">'
else:
    portada_html = '<div class="cover-fallback">MARILIN AMAYA</div>'

if logo_b64:
    logo_html = f'<img class="logo-img" src="data:image/png;base64,{logo_b64}" alt="Logo Marilin Amaya">'
else:
    logo_html = '<div class="logo-fallback">MA</div>'


st.markdown(
    f"""
    <div class="main-card">
        {portada_html}

        <div class="profile-row">
            <div>
                {logo_html}
            </div>

            <div>
                <div class="eyebrow">Psicología y bienestar</div>
                <div class="title">MARILIN AMAYA</div>
                <div class="eyebrow" style="font-size:14px; margin-bottom:6px;">PSICÓLOGA</div>
                <div class="subtitle">
                    Te acompaño en tu proceso de bienestar emocional y desarrollo personal.
                    Atención orientada a la escucha, la confidencialidad y el acompañamiento profesional.
                </div>

                <div class="btn-row">
                    <a class="btn-primary" href="{WHATSAPP_URL}" target="_blank">
                        Agendar cita por WhatsApp
                    </a>
                    <a class="btn-secondary" href="#servicios">
                        Ver servicios
                    </a>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown('<div id="servicios"></div>', unsafe_allow_html=True)
st.markdown("## Servicios de asesoramiento psicológico")
st.markdown(
    """
    <div class="section-text">
        Espacio profesional dirigido a fortalecer el bienestar emocional, el autoconocimiento
        y las estrategias personales para afrontar situaciones cotidianas.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="services-grid">
        <div class="service-card">
            <div class="service-icon">🌿</div>
            <div class="service-title">Bienestar emocional</div>
            <div class="service-desc">
                Orientación para reconocer emociones, ordenar pensamientos y fortalecer el equilibrio personal.
            </div>
        </div>

        <div class="service-card">
            <div class="service-icon">🧘</div>
            <div class="service-title">Estrés y ansiedad</div>
            <div class="service-desc">
                Acompañamiento para identificar detonantes y aplicar estrategias de manejo cotidiano.
            </div>
        </div>

        <div class="service-card">
            <div class="service-icon">🤍</div>
            <div class="service-title">Autoestima</div>
            <div class="service-desc">
                Fortalecimiento de la seguridad personal, autovaloración y toma de decisiones conscientes.
            </div>
        </div>

        <div class="service-card">
            <div class="service-icon">🤝</div>
            <div class="service-title">Relaciones saludables</div>
            <div class="service-desc">
                Orientación para mejorar comunicación, límites, vínculos y resolución de conflictos.
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown("## Enfoque de atención")

st.markdown(
    """
    <div class="focus-grid">
        <div class="focus-card">
            <div class="focus-title">Espacio seguro y confidencial</div>
            <div class="service-desc">
                La atención se realiza desde una comunicación respetuosa, ética y centrada en la persona.
            </div>
        </div>

        <div class="focus-card">
            <div class="focus-title">Atención previa cita</div>
            <div class="service-desc">
                Las sesiones se coordinan por WhatsApp, según disponibilidad horaria y modalidad de atención.
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="phrase-box">
        <div class="phrase-main">Escucha. Comprende. Acompaña.</div>
        <div class="phrase-sub">
            Un proceso psicológico puede ayudarte a mirar con mayor claridad lo que sientes, piensas y necesitas.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown("## ¿Cómo agendar una cita?")

st.markdown(
    """
    <div class="steps-grid">
        <div class="step-card">
            <div class="step-title">1. Escribe por WhatsApp</div>
            <div class="step-desc">
                Solicita información sobre disponibilidad, horarios y modalidad de atención.
            </div>
        </div>

        <div class="step-card">
            <div class="step-title">2. Indica tu motivo de consulta</div>
            <div class="step-desc">
                Comparte información general para orientar la coordinación inicial.
            </div>
        </div>

        <div class="step-card">
            <div class="step-title">3. Coordina fecha y hora</div>
            <div class="step-desc">
                Se confirma la cita según disponibilidad y condiciones del servicio.
            </div>
        </div>

        <div class="step-card">
            <div class="step-title">4. Inicia tu proceso</div>
            <div class="step-desc">
                Recibe orientación profesional en un espacio de escucha y acompañamiento.
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="warning-box">
        <strong>Nota importante:</strong> Este canal es informativo y de coordinación de citas.
        No reemplaza servicios de emergencia. Si existe una situación de riesgo inmediato,
        acude al centro de salud o servicio de emergencia más cercano.
    </div>
    """,
    unsafe_allow_html=True,
)
