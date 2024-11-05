import streamlit as st
from streamlit_lottie import st_lottie
import json

# Function to load the rocket animation from the JSON file
def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load the Rocket Lottie animation
rocket_animation = load_lottie_file("Rocket.json")

# Display the Rocket Lottie animation
st_lottie(rocket_animation, key="rocket", height=300, width=300)

# Set up the Streamlit dashboard
st.title("Rocket Sound Perception by Different Urban Animals")
st.write("Set off the rocket to simulate how different animals perceive rocket sounds.")

# Dropdown for animal selection
animal = st.selectbox(
    "Choose an animal to hear how they perceive the rocket sound:",
    ["Human", "Cat", "Dog", "Cow"]
)

# Dictionary to map animals to sound files (ensure these are in the same directory)
sound_files = {
    "Human": "rocket_human.wav",
    "Cat": "Rocket_cat.wav",
    "Dog": "rocket_dog.wav",
    "Cow": "rocket_cow.wav"
}

# Display the Rocket Lottie animation and simulate the click
clicked = st.button("🚀 Set off the Rocket")  # Display a button with a rocket icon

if clicked:
    sound_file = sound_files[animal]
    # Use Streamlit's st.audio to play the sound directly
    st.audio(sound_file, format="audio/wav", start_time=0)

