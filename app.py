import streamlit as st
import pandas as pd
from itinerary import generate_itinerary
from budget import estimate_budget
from maps import show_map
from weather import get_weather
from streamlit_folium import st_folium

# Page Config
st.set_page_config(page_title="TripMate AI", page_icon="✈️", layout="wide")

# Modern Styling
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; white-space: pre-wrap; background-color: #f0f2f6;
        border-radius: 10px 10px 0px 0px; gap: 1px; padding: 10px;
    }
    .stTabs [aria-selected="true"] { background-color: #ff4b4b !important; color: white !important; }
    .itinerary-card { border-left: 5px solid #ff4b4b; padding: 15px; background: #ffffff; border-radius: 5px; margin-bottom: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); color: black; }
    .gallery-img { width: 100%; border-radius: 10px; transition: 0.3s; }
    .gallery-img:hover { transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

# Persistence
if 'trip' not in st.session_state:
    st.session_state.trip = None

# Sidebar
with st.sidebar:
    st.header("🗺️ Plan Your Escape")
    dest = st.text_input("Where to?", "Bali")
    days = st.slider("Duration (Days)", 1, 30, 3)
    group_size = st.number_input("Number of Travelers", 1, 20, 1)
    budget_limit = st.number_input("Total Budget (INR)", 5000, 500000, 30000)
    style = st.selectbox("Travel Style", 
                         options=["Backpacker (Ultra Cheap)", "Budget", "Balanced", "Luxury", "Digital Nomad", "Adventure/Active"])
    interests = st.multiselect(
        "Primary Interests",
        ["Nature & Parks", "Nightlife & Party", "History & Culture", "Food & Cafes", "Shopping", "Adventure Sports", "Museums"],
        default=["Nature & Parks", "Food & Cafes"]
    )
    transport_pref = st.radio("How will you move?", ["Public Transport", "Rental (Scooter/Car)", "Walking & Cabs"])
    
    if st.button("🚀 Generate Full Plan", use_container_width=True):
        with st.spinner("AI is crafting your custom student itinerary..."):
            res = generate_itinerary(dest, days, budget_limit, style, interests, transport_pref, group_size)
            if "Error" in res or "permission" in res.lower():
                res = f"### 📍 Day 1: Arrival in {dest}\nCheck into your hostel and explore local street food.\n\n### 📍 Day 2: Exploration\nFocusing on your interests."
            
            st.session_state.trip = {
                "itinerary": res,
                "weather": get_weather(dest),
                "budget": estimate_budget(days),
                "dest": dest,
                "days": days
            }

# Main UI Logic
if st.session_state.trip:
    t = st.session_state.trip
    
    # Header Metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Destination", t['dest'])
    c2.metric("Days", t['days'])
    c3.metric("Temp", t['weather'])
    c4.metric("Est. Total", f"₹{t['budget']['Total']}")

    # Added "🏠 Home" to the tabs list
    tab_home, tab1, tab2, tab3 = st.tabs(["🏠 Home", "📑 Detailed Itinerary", "💰 Budget Breakdown", "🌍 Exploration Map"])

    with tab_home:
        st.subheader("🎒 Student Travel Inspiration")
        st.write("Explore the world without breaking the bank. Here are some glimpses of student adventures!")
        
        # Inspirational Gallery
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://images.unsplash.com/photo-1527631746610-bca00a040d60?auto=format&fit=crop&w=400&q=80", caption="Backpacking through Europe")
            st.image("https://images.unsplash.com/photo-1539635278303-d4002c07eae3?auto=format&fit=crop&w=400&q=80", caption="Group Hiking Trips")
        with col2:
            st.image("https://images.unsplash.com/photo-1501504905252-473c47e087f8?auto=format&fit=crop&w=400&q=80", caption="Digital Nomad Workstations")
            st.image("https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?auto=format&fit=crop&w=400&q=80", caption="Student Street Food Tours")
        with col3:
            st.image("https://images.unsplash.com/photo-1523906834658-6e24ef2386f9?auto=format&fit=crop&w=400&q=80", caption="Exploring Venice on a Budget")
            st.image("https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=400&q=80", caption="Meeting New People at Hostels")

    with tab1:
        col_left, col_right = st.columns([2, 1])
        with col_left:
            st.markdown("### 📅 Personalized Schedule")
            st.markdown(f'<div class="itinerary-card">{t["itinerary"]}</div>', unsafe_allow_html=True)
            st.download_button("📩 Download PDF Itinerary", t['itinerary'], file_name=f"Trip_to_{t['dest']}.txt")
        with col_right:
            st.info("💡 **Student Tip:** Hostels are not just for sleeping—they are the best place to meet travel partners!")
            st.image("https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=400&q=80")

    with tab2:
        st.subheader("Financial Overview")
        df = pd.DataFrame(t['budget'].items(), columns=["Category", "Amount (INR)"])
        st.table(df)
        st.bar_chart(df.set_index("Category"))

    with tab3:
        st.subheader(f"Interactive Map of {t['dest']}")
        m = show_map([t['dest']])
        st_folium(m, width=1000, height=450)
else:
    # Initial Landing Page
    st.markdown("## ✨ Your next adventure starts here.")
    st.write("Enter your destination and details in the sidebar to create a full student-optimized travel plan.")
    st.image("https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1200&q=80", use_column_width=True)