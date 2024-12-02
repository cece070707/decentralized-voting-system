import streamlit as st
import requests

# Affiche un titre
st.title("Interface de mon code GitHub")

# Affiche une section pour montrer le code GitHub
st.subheader("Code GitHub Exécuté")

# Exemple : afficher le contenu d'un fichier sur GitHub
# Remplace par le lien direct vers ton fichier sur GitHub
url = "https://raw.githubusercontent.com/cece070707/decentralized-voting-system/main/app.py"

# Récupère le contenu du fichier via l'URL de GitHub
response = requests.get(url)

# Vérifie si la requête a fonctionné
if response.status_code == 200:
    # Affiche le code Python depuis GitHub (sans l'exécuter)
    st.code(response.text, language='python')  # Affiche le code en tant que texte brut
else:
    st.error("Erreur de chargement du fichier GitHub.")


