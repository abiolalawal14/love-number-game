import streamlit as st
import random

st.set_page_config(page_title="Omotoke Love Number Game", page_icon="💖")

st.image("omot.jpg")  # Display the love banner
st.title("💖 Welcome to the Love Number Game 💖")
st.write("Enter a number and receive a romantic message just for you!")



# Set up our memory
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 10)
if 'tries' not in st.session_state:
    st.session_state.tries = 0
if 'won' not in st.session_state:
    st.session_state.won = False

st.title("💘 Hey Omotoke here is Our Love Number Game")
st.markdown("Guess a number between 1 and 10 and get a sweet love message! 💌")

guess = st.number_input("Enter your number:", min_value=1, max_value=10, step=1)

if st.button("Submit Guess"):
    st.session_state.tries += 1
    if guess == st.session_state.number_to_guess:
        st.session_state.won = True
        st.success(f"💖 You guessed it right in {st.session_state.tries} tries! Love is in the air!")
    else:
        love_quotes = [
            "Love is not about how many days, but how deeply you feel. 🌹",
            "You are one guess closer to my heart! 💌",
            "Every miss brings us closer together. ❤️",
            "Even when you're wrong, you're charming. 💕",
            "Oops! But I still adore you. 😘"
            "You're sweet like sugar 💖",
            "You're lucky in love!",
            "Your heart is as infinite as 8 ♾️",
            "You shine brighter than 9 stars!",
            "Perfect 10! Love is all around you 🌹"
        ]
        st.warning(random.choice(love_quotes))

if st.session_state.won:
    if st.button("Play Again"):
        st.session_state.number_to_guess = random.randint(1, 10)
        st.session_state.tries = 0
        st.session_state.won = False
