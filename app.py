import streamlit as st
import pandas as pd
import pickle

# Load the trained Random Forest model
with open('https://github.com/harshalpanchal2000/Drug_Classifier-/blob/main/random_forest_model_better_accuracy.pkl', 'rb') as f:
    model = pickle.load(f)

def main():
    st.title("Hello, World!")

if __name__ == "__main__":
    main()
