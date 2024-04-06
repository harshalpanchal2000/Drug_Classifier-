import streamlit as st
import pickle
import requests
from io import BytesIO

# URL to the pickle file
pickle_url = "https://github.com/harshalpanchal2000/Drug_Classifier-/blob/main/random_forest_model_better_accuracy.pkl"

# Download the pickle file from the URL
response = requests.get(pickle_url)
file_content = BytesIO(response.content)

# Load the trained Random Forest model
model = pickle.load(file_content)

def main():
    st.title("Hello, World!")

if __name__ == "__main__":
    main()
