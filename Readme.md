# 🎓 AI Travel Budget Planner for Students

An AI-powered chatbot that helps students plan affordable and personalized trips by generating smart itineraries, estimating budgets, showing maps, and providing real-time weather updates.

---

## 🚀 Project Overview

Planning a trip is often confusing and expensive for students. This chatbot acts as a **digital travel assistant** that:

- Creates day-wise itineraries using AI  
- Estimates trip expenses  
- Shows important locations on a map  
- Provides live weather information  
- Suggests student-friendly places and cheap eats

All features are integrated into an easy-to-use Streamlit web application.

---

## ✨ Features

✔ AI-generated personalized itinerary  
✔ Budget calculation with category breakdown  
✔ Group expense split  
✔ Real-time weather updates  
✔ Interactive map visualization  
✔ Downloadable trip plan  
✔ Student-focused suggestions (hostels, free activities, cheap food)

---

## 🛠 Technology Stack

- **Frontend:** Streamlit  
- **AI Model:** Hugging Face LLM  
- **APIs:**  
  - Hugging Face Inference API  
  - OpenWeatherMap API  
- **Libraries:**  
  - Geopy  
  - Folium  
  - Streamlit-Folium  
  - Python Requests  
- **Deployment:** Streamlit Cloud

---

## 📂 Project Structure

AI-Travel-Planner  
│  
├── app.py              → Main Streamlit application  
├── itinerary.py        → AI prompt & itinerary generation  
├── budget.py           → Budget estimation logic  
├── maps.py             → Map visualization module  
├── weather.py          → Weather API integration  
├── utils.py            → Hugging Face API helper  
├── requirements.txt    → Dependencies  
└── .env                → API keys (not pushed to GitHub)


## ⚙ Installation & Setup

### 1. Clone Repository
```bash
git clone <your-repo-link>
cd <repo-folder>

pip install -r requirements.txt

HF_TOKEN=your_huggingface_token
HF_MODEL=your_model_name
WEATHER_API_KEY=your_openweather_key

streamlit run app.py

🧠 How It Works

User enters trip details

Data converted into AI prompt

Hugging Face model generates itinerary

Budget module calculates expenses

Weather & map modules add real-time info

Final plan displayed and downloadable

🌐 Deployment

The application is deployed on Streamlit Cloud and can be accessed from any device without installation.

Steps followed:

Upload code to GitHub

Add environment variables in Streamlit Cloud

Deploy directly from repository

Automatic updates on new commits

📸 Output Includes

Day-wise itinerary

Budget table

Weather report

Interactive map

Download option

🚧 Future Scope

Flight/train booking integration

Voice-based interaction

Multi-language support

Expense tracker

Safety recommendations

📚 References

Hugging Face Docs: https://huggingface.co/docs

Streamlit Docs: https://docs.streamlit.io

OpenWeather API: https://openweathermap.org/api

Geopy: https://geopy.readthedocs.io

Folium: https://python-visualization.github.io/folium/

⭐ If you like this project, give it a star on GitHub!