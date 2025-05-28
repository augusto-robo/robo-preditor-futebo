import streamlit as st
from previsor import prever_resultado
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

st.set_page_config(page_title="Robô AUGUSTO MB", page_icon="⚽", layout="centered")
st.markdown("## ⚽ ROBÔ PREDITOR AUGUSTO MB")
st.markdown("### 🙏 VOCÊ É ABENÇOADO E PONTO FINAL")

time_casa = st.text_input("🏠 Time da Casa").strip()
time_fora = st.text_input("🚩 Time Visitante").strip()

if st.button("🔍 Prever Resultado"):
    if time_casa and time_fora:
        previsao = prever_resultado(time_casa, time_fora)
        st.markdown("### 📊 Previsão do Robô:")
        st.markdown(previsao)
    else:
        st.warning("⚠️ Preencha os dois times para prever.")