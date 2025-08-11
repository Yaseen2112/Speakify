# 📖 PDF to Speech Reader with Voice Selection 🎤

An interactive **Streamlit** web application that allows you to:
- Upload any PDF,
- Select start page,
- Choose a voice (supports Indian accents if available),
- Convert the extracted text into speech using `pyttsx3`,
- Play the generated audio directly in the browser.

The app features a **custom background image** and a **beautiful modern UI** built with CSS.

---

## 🚀 Features
- 📂 Upload any `.pdf` file
- 🔢 Choose start page for reading
- 🗣 Voice selection (including Indian English voices if available)
- 🎧 Plays generated audio in-browser
- 🎨 Custom background image with text overlay for readability

---

## 📂 Project Structure
Speakify/
│
├── main.py # Main application script
├── requirements.txt # Dependencies
├── assets/
│ └── image.png # Background image
└── README.md # This file


---

## 📦 Installation

1️⃣ **Clone this repository** or copy files locally:

git clone https://github.com/Yaseen2112/speakify.git

cd speakify


2️⃣ **Install dependencies**:
pip install -r requirements.txt


3️⃣ **Ensure you have system voices**
- On Windows: Install additional voices via *Settings → Time & Language → Speech → Manage Voices*.
- On macOS: Install extra voices in *System Preferences → Accessibility → Spoken Content .
- On Linux: Configure voices via `espeak` or system TTS.

---

## ▶️ Run the App

streamlit run main.py



This will open the browser interface automatically.

---

## 🖼 Background Image
Add your preferred background image inside `assets/` and name it `image.png`.
The app automatically uses this image as the background.

---

## ⚙️ How to Use
1. **Upload a PDF** via drag-drop or file picker.
2. Choose the **start page**.
3. Select the **voice** from dropdown (Indian voices preferred if available).
4. Click **"Start Reading Aloud"** to extract text & generate audio.
5. Listen to the audio in-browser or download it.

---

## 📌 Requirements
- Python 3.8+
- Internet browser (runs locally after `streamlit run`)

---

## 🏆 Credits
Developed with 💙 using:
- [Streamlit](https://streamlit.io) for UI
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF processing
- [pyttsx3](https://pypi.org/project/pyttsx3/) for offline TTS

---


## 👤 About Me

**Name:** SHAIK YASEEN

**Project:** PDF to Speech Reader — A Streamlit web application that allows users to upload PDFs, select a start page, choose a voice (including Indian voices if available), and listen to the extracted text read aloud with an elegant UI and background image.

**📧 Email:** skyaseen2112@gmail.com

**📞 Contact:** +91-9704330969





