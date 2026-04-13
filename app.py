import streamlit as st

st.title("Welding SaaS Test")

st.write("If you see this, Streamlit works")

x = st.slider("Test slider", 0, 100, 50)

st.write("Value:", x)
