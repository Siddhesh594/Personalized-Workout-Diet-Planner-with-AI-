import streamlit as st
from utils import generate_fitness_plan

# Page setup
st.set_page_config(
    page_title="AI Fitness Planner",
    page_icon="💪",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for better design
st.markdown("""
    <style>
    body {
        background-color: #f7f9fc;
    }
    .main {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #ff4b4b;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 20px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #e63946;
        transform: scale(1.05);
    }
    .css-1d391kg, .css-1q8dd3e {
        background: #f7f9fc;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.title("💪 AI Fitness Planner")
st.markdown("<h5 style='text-align:center; color:grey;'>Your personal AI coach for smarter workouts & diet plans</h5>", unsafe_allow_html=True)
st.divider()

# Input Section
st.markdown("### 🧠 Enter Your Details")

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", 10, 100, 25)
    height = st.number_input("Height (cm)", 50, 250, 170)
    activity = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "High"])

with col2:
    weight = st.number_input("Weight (kg)", 20, 200, 65)
    goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Maintenance"])
    diet = st.selectbox("Diet Preference", ["Vegetarian", "Vegan", "Non-Vegetarian", "Keto", "Other"])

# Generate Button
st.markdown("### 🚀 Generate Your Personalized Plan")
if st.button("Get My Plan"):
    user_input = (
        f"Create a detailed, structured fitness and diet plan.\n"
        f"Age: {age}\nWeight: {weight} kg\nHeight: {height} cm\n"
        f"Goal: {goal}\nActivity: {activity}\nDiet: {diet}.\n"
        "Include workouts, nutrition, and lifestyle tips."
    )

    with st.spinner("🤖 Crafting your fitness plan..."):
        plan = generate_fitness_plan(user_input)

    st.divider()
    st.markdown("### 🏋️ Your AI-Generated Fitness Plan")
    st.write(plan)
    st.success("✨ Plan generated successfully!")

# Footer
st.markdown("<br><hr><center>Made with ❤️ using Gemini AI</center>", unsafe_allow_html=True)
