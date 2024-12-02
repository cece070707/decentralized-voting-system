import streamlit as st
from web3 import Web3

# Connexion à Ethereum via Web3 (assurez-vous d'utiliser votre propre provider, comme Infura ou Alchemy)
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID"))

# Adresse du contrat déployé sur le testnet (par exemple, Rinkeby)
contract_address = "VOTRE_ADRESSE_CONTRAT"
abi = [...]  # Le ABI de votre contrat, vous devez le remplacer ici

# Initialisation du contrat
contract = w3.eth.contract(address=contract_address, abi=abi)

# Interface Streamlit
st.title("Système de Vote Décentralisé")

# Affichage des candidats
candidates = contract.functions.getCandidates().call()  # Exemple pour récupérer les candidats
for candidate in candidates:
    st.write(f"{candidate[0]} : {candidate[1]} votes")

# Choisir un candidat pour voter
selected_candidate = st.selectbox("Choisissez un candidat", [candidate[0] for candidate in candidates])

if st.button('Voter'):
    account = w3.eth.accounts[0]  # Utiliser l'adresse de l'utilisateur (assurez-vous que l'utilisateur est connecté à un portefeuille comme MetaMask)
    tx_hash = contract.functions.vote(selected_candidate).transact({'from': account})

    st.write("Vote enregistré !", tx_hash)
    st.write(f"Suivez la transaction sur [Etherscan](https://rinkeby.etherscan.io/tx/{tx_hash})")

# Suivi de la transaction via le hash
st.subheader("Suivi des résultats")
tx_hash_input = st.text_input("Entrez votre hash de transaction pour suivre votre vote :")
if tx_hash_input:
    receipt = w3.eth.getTransactionReceipt(tx_hash_input)
    if receipt:
        st.write("Transaction confirmée !")
    else:
        st.write("Transaction en attente.")
