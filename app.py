import streamlit as st
import datetime
import random
import requests
import matplotlib.pyplot as plt

# NewsAPI key (replace 'YOUR_API_KEY' with your actual NewsAPI key)
API_KEY = 'c9c5cccd294f4fb2a51ced5ed618de86'  # Ta clé API
BASE_URL = 'https://newsapi.org/v2/everything'

# Initializing vote variables (if not already initialized)
if "votes_A" not in st.session_state:
    st.session_state.votes_A = random.randint(1, 100)  # Random starting votes for A
    st.session_state.votes_B = random.randint(1, 100)  # Random starting votes for B
if "has_voted" not in st.session_state:
    st.session_state.has_voted = False  # Variable to ensure only one vote
if "start_date" not in st.session_state:
    st.session_state.start_date = datetime.datetime.now()  # Set the start date for voting

# Calculate percentage of votes
def get_percentage(candidate_votes, total_votes):
    if total_votes == 0:
        return 0
    return (candidate_votes / total_votes) * 100

# Check if the voting period (2 weeks) has expired
def voting_period_expired():
    now = datetime.datetime.now()
    delta = now - st.session_state.start_date
    return delta.days > 14  # 14 days = 2 weeks

# Display the title and instructions
st.title("Election: Mr./Ms. A vs Mr./Ms. B")
st.write("Choose your candidate, and we will show the vote results after you cast your vote.")

# Custom CSS styling for improved appearance
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        width: 100%;
        padding: 10px;
        border: none;
    }
    .stRadio>div>label>div {
        font-size: 18px;
        color: #333;
    }
    .stAlert {
        background-color: #e6f7e6;
        color: #2e6e2e;
        font-weight: bold;
    }
    .stMarkdown {
        font-size: 18px;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# First page - Voting options
if not st.session_state.has_voted:
    vote_option = st.radio(
        "Who would you like to choose?",
        ("Mr./Ms. A", "Mr./Ms. B")
    )

    # Button to vote
    if st.button("Vote"):
        if vote_option == "Mr./Ms. A":
            st.session_state.votes_A += 1
        elif vote_option == "Mr./Ms. B":
            st.session_state.votes_B += 1

        # Mark that the user has voted to prevent voting again
        st.session_state.has_voted = True

        # After voting, redirect to the results page
        st.experimental_rerun()

# Second page - After voting
if st.session_state.has_voted:
    # Display the vote results
    st.write("Thank you for voting! Here are the current election results:")

    total_votes = st.session_state.votes_A + st.session_state.votes_B
    percent_A = get_percentage(st.session_state.votes_A, total_votes)
    percent_B = get_percentage(st.session_state.votes_B, total_votes)

    st.subheader("Vote Results")
    st.write(f"Total votes: {total_votes}")

    if percent_A > percent_B:
        st.markdown(f"<span style='color: red;'>Mr./Ms. A: {st.session_state.votes_A} votes ({percent_A:.2f}%)</span>", unsafe_allow_html=True)
        st.markdown(f"Mr./Ms. B: {st.session_state.votes_B} votes ({percent_B:.2f}%)", unsafe_allow_html=True)
    else:
        st.markdown(f"Mr./Ms. A: {st.session_state.votes_A} votes ({percent_A:.2f}%)", unsafe_allow_html=True)
        st.markdown(f"<span style='color: blue;'>Mr./Ms. B: {st.session_state.votes_B} votes ({percent_B:.2f}%)</span>", unsafe_allow_html=True)

    # Pie chart for visual representation
    labels = ["Mr./Ms. A", "Mr./Ms. B"]
    sizes = [st.session_state.votes_A, st.session_state.votes_B]
    colors = ['#ff9999','#66b3ff']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot()

    # News section
    st.subheader("Latest News")

    # Ask the user to input a keyword (e.g., "USA elections")
    keyword = st.text_input("Enter a keyword to get the latest news", "USA elections")

    if keyword:
        params = {
            'q': keyword,  # The query word for the news search
            'apiKey': API_KEY,
            'pageSize': 5  # Limit the number of articles shown
        }

        # Get the news data
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            if data['totalResults'] > 0:
                st.write(f"Found {data['totalResults']} articles related to '{keyword}':")
                for article in data['articles']:
                    st.write(f"**{article['title']}**")
                    st.write(f"[Read more]({article['url']})")
                    st.write(f"{article['description']}")
                    st.write("---")
            else:
                st.write(f"No articles found for '{keyword}'")
        else:
            st.error("Failed to retrieve news. Please try again later.")
