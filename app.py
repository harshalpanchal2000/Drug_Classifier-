import streamlit as st
import pandas as pd
import pickle
import requests
from io import BytesIO

# Function to download the file from the URL
def download_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        st.error("Failed to download the file.")

# URL of the file in the GitHub repository
url = 'https://github.com/harshalpanchal2000/Drug_Classifier-/blob/main/random_forest_model_better_accuracy.pkl'

# Download the file
file_content = download_file(url)

# Load the trained Random Forest model
if file_content:
    model = pickle.load(file_content)

def main():
    st.title("Hello, World!")

if __name__ == "__main__":
    main()
