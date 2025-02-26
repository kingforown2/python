import streamlit as st

# Ask the user to input a number
user_input = st.number_input("Enter a number:")

# Print the number entered by the user
st.write(f"You entered: {user_input}")
