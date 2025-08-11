import streamlit as st
import pyttsx3
from PyPDF2 import PdfReader
import tempfile
import os
import base64

# Function to get base64 encoding of the image file
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Path to your background image (relative to this script)
image_path = "assets/image.png"
image_base64 = get_base64(image_path)

# Inject CSS for background image with overlay for readability
st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{image_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            background-color: rgba(255, 255, 255, 0.6);
            z-index: -1;
        }}

        .title {{
            font-size: 40px !important;
            color: #2c3e50;
            text-align: center;
            font-weight: bold;
            margin-bottom: 30px;
        }}
        .stButton>button {{
            background-color: #3498db;
            color: white;
            border-radius: 8px;
            font-size: 18px;
            padding: 8px 16px;
        }}
        .stButton>button:hover {{
            background-color: #2980b9;
        }}
        .uploadedFile {{
            text-align: center;
            font-size: 18px;
            color: #000000;
            margin-bottom: 20px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit page configuration
st.set_page_config(page_title="📚 PDF Reader & Speaker with Voice Selection", page_icon="🎤", layout="centered")

st.markdown('<p class="title">📖 PDF to Speech Reader with Voice Selection</p>', unsafe_allow_html=True)

# Initialize pyttsx3 engine and fetch available voices
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_dict = {voice.id: voice.name for voice in voices}

uploaded_file = st.file_uploader("Upload your PDF 📂", type="pdf")

if uploaded_file:
    st.markdown(f"<p class='uploadedFile'>✅ {uploaded_file.name} uploaded successfully!</p>", unsafe_allow_html=True)
    pdf_reader = PdfReader(uploaded_file)
    total_pages = len(pdf_reader.pages)
    st.info(f"Your PDF has **{total_pages}** pages.")

    start_page = st.number_input("Select start page (0-based index)", min_value=0, max_value=total_pages - 1, value=0)

    # Filter voices for Indian voices if possible
    indian_voices = {vid: vname for vid, vname in voice_dict.items() if 'india' in vname.lower() or 'hindi' in vname.lower()}
    if not indian_voices:
        # If no specifically Indian voice found, fallback to all voices
        indian_voices = voice_dict

    selected_voice_id = st.selectbox("Select Voice", options=list(indian_voices.keys()), format_func=lambda x: indian_voices[x])

    if st.button("🎤 Start Reading Aloud"):
        text_content = ""
        for num in range(start_page, total_pages):
            page = pdf_reader.pages[num]
            text_content += page.extract_text() or ""

        st.text_area("Extracted Text", text_content, height=300)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_path = temp_audio.name

        engine = pyttsx3.init()
        engine.setProperty('voice', selected_voice_id)
        engine.save_to_file(text_content, temp_path)
        engine.runAndWait()

        with open(temp_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")

        os.remove(temp_path)
        st.success("Audio generated successfully! 🎧")

