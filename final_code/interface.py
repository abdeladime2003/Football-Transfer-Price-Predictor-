import streamlit as st
from PIL import Image
st.title("Football Transfer Price Predictor 📊⚽️💰")
image_path = r"C:\Users\Lenovo\Desktop\projet_baina\nouveau_projet\Capture d’écran 2024-03-20 172927.png"
image = Image.open(image_path)
st.image(image, caption='Capture d’écran', use_column_width=True)
username = st.text_input("Nom d'utilisateur")
password = st.text_input("Mot de passe", type="password")
if st.button("Se connecter"):
    if username == "user" and password == "1253":
        st.success("Connexion réussie!")
    else:
        st.error("Nom d'utilisateur ou mot de passe incorrect")
