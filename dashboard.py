import streamlit as st
import pandas as pd
from PIL import Image
from random import randint
from random import seed
seed(1) 

filename = "dashboard.py"
print("Run the file:")
print(f"streamlit run {filename}")

#---------------------------------------------------------------
# Data and functions
#---------------------------------------------------------------

df = pd.DataFrame({
        'book_id': [1, 2, 3, 1, 2, 3, 1, 2, 3],
        'agency': [
            "Municipality 1","Municipality 1","Municipality 1",
            "Municipality 2","Municipality 2","Municipality 2",
            "Municipality 3","Municipality 3","Municipality 3"],
        'loans': [randint(0,50) for _ in range(9)]
})


def predict(df, book_id, municipality:str):
    seed(1)
    user_df = df[(df.agency==municipality) & (df.book_id==book_id)]
    return user_df

#---------------------------------------------------------------
# Streamlit frontend
#---------------------------------------------------------------

# Title
st.title("Book Forecast")
st.write("*Streamlit* dashboard")

#----------------
# Insert Faustnr
#----------------

# Select box
municipality = st.selectbox(
    'Choose municipality',
     ['Municipality 1','Municipality 2','Municipality 3']
)

# Write faustnumber
book_id = st.number_input("Insert book ID (between 1-3)", min_value=1, max_value=3)

# Show result
result = predict(df, book_id, municipality)

if st.button('Predict'):
    st.write(f"#### Expected loans: {int(result.loans.values)}")

#--------------
# Show data
#--------------
if st.checkbox('Show dataframe'):
    st.write(result)

    image = Image.open('pic1.jpg')
    st.image(image, caption='Provided by Me')