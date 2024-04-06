import streamlit as st
import pickle
import requests

# URL to the pickle file
pickle_url = "https://github.com/harshalpanchal2000/Drug_Classifier-/raw/main/random_forest_model_better_accuracy.pkl"

# Download the pickle file from the URL
response = requests.get(pickle_url)

# Check if the request was successful
if response.status_code == 200:
    # Load the trained Random Forest model
    model = pickle.loads(response.content)
else:
    st.error("Failed to download the model.")

def main():
    st.title("Hello, World!")

if __name__ == "__main__":
    main()


