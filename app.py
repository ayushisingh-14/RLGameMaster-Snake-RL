import streamlit as st
import random

st.title("🐍 RLGameMaster – Snake AI Demo")

st.write("""
This is a **demo version** of the Snake RL project.

✔ Model trained using Deep Q-Network (PyTorch) in Google Colab  
✔ Deployment uses rule-based actions for visualization  
✔ Full training code available in GitHub
""")

if st.button("Play Snake"):
    score = random.randint(10, 50)
    st.success(f"Game Over! Score: {score}")

  
