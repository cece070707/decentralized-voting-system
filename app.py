import streamlit as st

# Initialiser les variables de votes (si ce n'est pas déjà fait)
if "votes_A" not in st.session_state:
    st.session_state.votes_A = 0
    st.session_state.votes_B = 0
if "has_voted" not in st.session_state:
    st.session_state.has_voted = False  # Variable pour s'assurer qu'on ne vote qu'une seule fois

# Fonction pour calculer le pourcentage de votes
def get_percentage(candidate_votes, total_votes):
    if total_votes == 0:
        return 0
    return (candidate_votes / total_votes) * 100

# Affichage du titre et de l'instruction
st.title("Élection : Monsieur/Madame A vs Monsieur/Madame B")
st.write("Choisissez votre candidat et nous afficherons le suivi des votes après votre vote.")

# Si l'utilisateur a déjà voté, ne pas lui permettre de revoter
if st.session_state.has_voted:
    st.write("Vous avez déjà voté ! Voici les résultats des élections :")
    total_votes = st.session_state.votes_A + st.session_state.votes_B
    percent_A = get_percentage(st.session_state.votes_A, total_votes)
    percent_B = get_percentage(st.session_state.votes_B, total_votes)

    # Afficher les résultats
    st.subheader("Suivi des votes")
    st.write(f"Nombre total de votes : {total_votes}")
    st.write(f"Monsieur/Madame A : {st.session_state.votes_A} votes ({percent_A:.2f}%)")
    st.write(f"Monsieur/Madame B : {st.session_state.votes_B} votes ({percent_B:.2f}%)")

else:
    # Création des boutons pour voter (uniquement si l'utilisateur n'a pas voté)
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

        # Marquer que l'utilisateur a voté pour empêcher de revoter
        st.session_state.has_voted = True

        # Après le vote, afficher les résultats
        total_votes = st.session_state.votes_A + st.session_state.votes_B
        percent_A = get_percentage(st.session_state.votes_A, total_votes)
        percent_B = get_percentage(st.session_state.votes_B, total_votes)

        # Afficher les résultats
        st.subheader("Suivi des votes")
        st.write(f"Nombre total de votes : {total_votes}")
        st.write(f"Monsieur/Madame A : {st.session_state.votes_A} votes ({percent_A:.2f}%)")
        st.write(f"Monsieur/Madame B : {st.session_state.votes_B} votes ({percent_B:.2f}%)")

        # Afficher un message de confirmation du vote
        st.success("Merci pour votre vote !")
