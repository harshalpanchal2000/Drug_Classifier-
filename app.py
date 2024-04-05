!pip install streamlit 
!pip install pandas
!pip install pickle

import streamlit as st
import pandas as pd
import pickle

# Load the trained Random Forest model
with open('random_forest_model_better_accuracy.pkl', 'rb') as f:
    model = pickle.load(f)

# Define function to preprocess user input
def preprocess_input(age, gender, education, country, ethnicity, nscore, escore, oscore, ascore, cscore, impulsive, ss, alcohol):
    return pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Education': [education],
        'Country': [country],
        'Ethnicity': [ethnicity],
        'Nscore': [nscore],
        'Escore': [escore],
        'Oscore': [oscore],
        'Ascore': [ascore],
        'Cscore': [cscore],
        'Impulsive': [impulsive],
        'SS': [ss],
        'Alcohol': [alcohol]
    })

# Define the Streamlit app
def main():
    # Title and description
    st.title('Nicotine Usage Predictor')
    st.write('This app predicts whether a person is likely to use nicotine based on various factors.')

    # User inputs
    st.sidebar.header('User Input')
    age = st.sidebar.slider('Age', 18, 100, 25)
    gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
    education = st.sidebar.selectbox('Education', ['Below College', 'College', 'Bachelor', 'Master', 'Doctorate'])
    country = st.sidebar.text_input('Country', 'United States')
    ethnicity = st.sidebar.text_input('Ethnicity', 'Caucasian')
    nscore = st.sidebar.slider('Nscore', 0.0, 1.0, 0.5)
    escore = st.sidebar.slider('Escore', 0.0, 1.0, 0.5)
    oscore = st.sidebar.slider('Oscore', 0.0, 1.0, 0.5)
    ascore = st.sidebar.slider('Ascore', 0.0, 1.0, 0.5)
    cscore = st.sidebar.slider('Cscore', 0.0, 1.0, 0.5)
    impulsive = st.sidebar.slider('Impulsive', 0.0, 1.0, 0.5)
    ss = st.sidebar.slider('SS', 0.0, 1.0, 0.5)
    alcohol = st.sidebar.slider('Alcohol', 0, 10, 5)

    # Preprocess input and make prediction
    input_df = preprocess_input(age, gender, education, country, ethnicity, nscore, escore, oscore, ascore, cscore, impulsive, ss, alcohol)
    prediction = model.predict(input_df)

    # Display prediction
    st.subheader('Prediction')
    if prediction[0] == 0:
        st.write('Not Likely to Use Nicotine')
    else:
        st.write('Likely to Use Nicotine')

if __name__ == '__main__':
    main()
