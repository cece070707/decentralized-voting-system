import streamlit as st

# Initialiser les variables de votes (pour la première session de l'application)
if "votes_A" not in st.session_state:
    st.session_state.votes_A = 0
    st.session_state.votes_B = 0

# Fonction pour calculer le pourcentage de votes
def get_percentage(candidate_votes, total_votes):
    if total_votes == 0:
        return 0
    return (candidate_votes / total_votes) * 100

# Affichage du titre et de l'instruction
st.title("Élection : Monsieur/Madame A vs Monsieur/Madame B")
st.write("Choisissez votre candidat et nous afficherons le suivi des votes.")

# Création des boutons pour voter
vote_option = st.radio(
    "Qui souhaitez-vous choisir ?",
    ("Monsieur/Madame A", "Monsieur/Madame B")
)

# Button to vote
if st.button("Voter"):
    if vote_option == "Monsieur/Madame A":
        st.session_state.votes_A += 1
    elif vote_option == "Monsieur/Madame B":
        st.session_state.votes_B += 1

# Affichage du suivi des votes
total_votes = st.session_state.votes_A + st.session_state.votes_B
percent_A = get_percentage(st.session_state.votes_A, total_votes)
percent_B = get_percentage(st.session_state.votes_B, total_votes)

# Affichage des résultats
st.subheader("Suivi des votes")
st.write(f"Nombre total de votes : {total_votes}")
st.write(f"Monsieur/Madame A : {st.session_state.votes_A} votes ({percent_A:.2f}%)")
st.write(f"Monsieur/Madame B : {st.session_state.votes_B} votes ({percent_B:.2f}%)")

# Un peu de style pour rendre l'interface plus jolie
st.markdown("""
    <style>
    .css-1d391kg {
        background-color: #f0f4f8;
    }
    .css-1d391kg .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
    }
    .css-1d391kg .stRadio>div>label>div {
        font-size: 20px;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)
