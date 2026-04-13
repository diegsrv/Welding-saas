import streamlit as st
import numpy as np

st.title("Welding SaaS Test")

force = st.number_input("Force", 1000)
surface = st.number_input("Surface", 10)

if st.button("Run"):

    stress = force / surface
    score = 100 - stress * 0.01

    st.success(f"Stress: {stress}")
    st.success(f"Score: {score}")
