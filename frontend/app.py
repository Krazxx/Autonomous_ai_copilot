import streamlit as st
import base64
import requests
import os
from pypdf import PdfReader

st.set_page_config(
    page_title="Autonomous AI Copilot",
    layout="wide"
)

# ---------- LOAD CSS ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
css_path = os.path.join(BASE_DIR, "static", "style.css")

with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---------- LOAD BACKGROUND VIDEO ----------
video_path = os.path.join(BASE_DIR, "static", "bg.mp4")

with open(video_path, "rb") as video_file:
    video_bytes = video_file.read()

video_base64 = base64.b64encode(video_bytes).decode()

video_html = f"""
<div class="video-container">
    <video autoplay muted loop playsinline>
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
    </video>
</div>

<div class="overlay"></div>
"""

st.markdown(video_html, unsafe_allow_html=True)


# ---------- HERO ----------
st.markdown("""
<div class="hero">
<h1>KrazxX AI Copilot</h1>
<p>AI system with agents, workflows and automation</p>
</div>
""", unsafe_allow_html=True)


# ---------- STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ FIX 1: initialize pdf flag
if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False


# ---------- INPUT ----------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    with st.form(key="chat_form", clear_on_submit=True):
        prompt = st.text_input(
            "Ask AI",
            placeholder="Ask KrazxX..."
        )
        submit = st.form_submit_button("Send")


# ---------- HANDLE MESSAGE (ONLY ONE BLOCK) ----------
if submit and prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    try:
        
        res = requests.post(
            "https://autonomousaicopilot-production.up.railway.app/api/chat",
            json={"message": prompt},
            timeout=30
        )

        data = res.json()
        response = data.get("response")

        # 🎵 handle music response
        if isinstance(response, dict) and response.get("type") == "music":
            response = f"🎵 Play here: {response['url']}"

    except Exception as e:
        response = f"Error: {str(e)}"

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


# ---------- CHAT DISPLAY ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# ---------- PDF UPLOAD ----------
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file and not st.session_state.pdf_uploaded:
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content

    if text:
        try:
            requests.post(
                "https://autonomousaicopilot-production.up.railway.app/api/upload",
                json={"text": text},
                timeout=60
            )
            st.session_state.pdf_uploaded = True
            st.success("PDF uploaded & processed ✅")
        except:
            st.error("Failed to upload PDF ❌")


            