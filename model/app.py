import streamlit as st
import pandas as pd

# Function to load recommendations from a text file
def load_recommendations(filename):
    recommendations = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        current_section = None
        for line in lines:
            line = line.strip()
            if "Top N Recommendations" in line:
                current_section = line
                continue
            
            if current_section and line:
                try:
                    user, items = line.split(":", 1)  # Use maxsplit=1
                    recommendations[user.strip()] = eval(items.strip())  # Safely evaluate the list
                except ValueError as e:
                    st.warning(f"Could not parse line: {line} - Error: {e}")
    return recommendations

# Load user and item-based recommendations
user_based_recommendations = load_recommendations('recommendations.txt')
item_based_recommendations = load_recommendations('recommendations.txt')  # Adjust logic if necessary for item-based

# Streamlit app layout
st.title("Recommendations App")

# Sidebar for user selection
user_selection = st.sidebar.selectbox("Select a User:", list(user_based_recommendations.keys()))

# Display user-based recommendations
st.subheader(f"User-Based Recommendations for {user_selection}")
st.write(user_based_recommendations[user_selection])

# Display item-based recommendations
st.subheader("Item-Based Recommendations")
if user_selection in item_based_recommendations:
    st.write(item_based_recommendations[user_selection])  # Adjust this part to access the item-based recommendations properly
else:
    st.write("No item-based recommendations available for this user.")

# Additional interactive features can be added here
