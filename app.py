import streamlit as st
import datetime
import matplotlib.pyplot as plt

# Initializing vote variables (if not already initialized)
if "votes_A" not in st.session_state:
    st.session_state.votes_A = 0
    st.session_state.votes_B = 0
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

# If voting period has expired, show a message and prevent voting
if voting_period_expired():
    st.write("The voting period has ended. You can no longer vote.")
    st.write("Here are the current election results:")

    # Display results if voting period has ended
    total_votes = st.session_state.votes_A + st.session_state.votes_B
    percent_A = get_percentage(st.session_state.votes_A, total_votes)
    percent_B = get_percentage(st.session_state.votes_B, total_votes)

    # Display the results with dynamic color styling
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

else:
    # Display countdown timer
    now = datetime.datetime.now()
    delta = st.session_state.start_date + datetime.timedelta(days=14) - now
    if delta.days > 0:
        st.write(f"Time left to vote: {delta.days} days, {delta.seconds // 3600} hours, {(delta.seconds // 60) % 60} minutes")
    else:
        st.write("The voting period has ended.")

    # Voting options (only if the user hasn't voted yet and voting is still open)
    if st.session_state.has_voted:
        st.write("You have already voted. Here are the current election results:")
        total_votes = st.session_state.votes_A + st.session_state.votes_B
        percent_A = get_percentage(st.session_state.votes_A, total_votes)
        percent_B = get_percentage(st.session_state.votes_B, total_votes)

        # Show the results after voting
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

    else:
        # If the user hasn't voted yet
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

            # After voting, display the results
            total_votes = st.session_state.votes_A + st.session_state.votes_B
            percent_A = get_percentage(st.session_state.votes_A, total_votes)
            percent_B = get_percentage(st.session_state.votes_B, total_votes)

            # Display the results
            st.subheader("Vote Results")
            st.write(f"Total votes: {total_votes}")

            if percent_A > percent_B:
                st.markdown(f"<span style='color: red;'>Mr./Ms. A: {st.session_state.votes_A} votes ({percent_A:.2f}%)</span>", unsafe_allow_html=True)
                st.markdown(f"Mr./Ms. B: {st.session_state.votes_B} votes ({percent_B:.2f}%)", unsafe_allow_html=True)
            else:
                st.markdown(f"Mr./Ms. A: {st.session_state.votes_A} votes ({percent_A:.2f}%)", unsafe_allow_html=True)
                st.markdown(f"<span style='color: blue;'>Mr./Ms. B: {st.session_state.votes_B} votes ({percent_B:.2f}%)</span>", unsafe_allow_html=True)

            # Display a confirmation message for voting
            st.success("Thank you for voting!")
