import streamlit as st
import datetime

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

# If voting period has expired, show a message and prevent voting
if voting_period_expired():
    st.write("The voting period has ended. You can no longer vote.")
    st.write("Here are the current election results:")

    # Display results if voting period has ended
    total_votes = st.session_state.votes_A + st.session_state.votes_B
    percent_A = get_percentage(st.session_state.votes_A, total_votes)
    percent_B = get_percentage(st.session_state.votes_B, total_votes)

    # Show the results
    st.subheader("Vote Results")
    st.write(f"Total votes: {total_votes}")
    st.write(f"Mr./Ms. A: {st.session_state.votes_A} votes ({percent_A:.2f}%)")
    st.write(f"Mr./Ms. B: {st.session_state.votes_B} votes ({percent_B:.2f}%)")
else:
    # Voting options (only if the user hasn't voted yet and voting is still open)
    if st.session_state.has_voted:
        st.write("You have already voted. Here are the current election results:")
        total_votes = st.session_state.votes_A + st.session_state.votes_B
        percent_A = get_percentage(st.session_state.votes_A, total_votes)
        percent_B = get_percentage(st.session_state.votes_B, total_votes)

        # Show the results after voting
        st.subheader("Vote Results")
        st.write(f"Total votes: {total_votes}")
        st.write(f"Mr./Ms. A: {st.session_state.votes_A} votes ({percent_A:.2f}%)")
        st.write(f"Mr./Ms. B: {st.session_state.votes_B} votes ({percent_B:.2f}%)")
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
            st.write(f"Mr./Ms. A: {st.session_state.votes_A} votes ({percent_A:.2f}%)")
            st.write(f"Mr./Ms. B: {st.session_state.votes_B} votes ({percent_B:.2f}%)")

            # Display a confirmation message for voting
            st.success("Thank you for voting!")




