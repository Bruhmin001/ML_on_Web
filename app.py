import streamlit as st

# Title of the app
st.title('Basic Streamlit App with Sidebar')

# Sidebar
st.sidebar.title('Sidebar')
st.sidebar.write('This is the sidebar.')

# Main content
st.write('This is the main content area.')

# Sidebar input
user_input = st.sidebar.text_input('Enter a message:', 'Hello, Streamlit!')

# Display user input
st.write('You entered:', user_input)