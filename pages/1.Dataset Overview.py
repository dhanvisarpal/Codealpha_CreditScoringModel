import streamlit as st
import pandas as pd 

st.title("Dataset overview")
df = pd.read_csv(r"C:\Users\user\default of credit card clients.csv",header=1)
st.dataframe(df)

st.write(df.shape)
st.write(df.columns.tolist())

st.header("Dataset Shape")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

with col3: 
    st.metric("misssing vaues",df.isnull().sum().sum())

st.write(df.describe())