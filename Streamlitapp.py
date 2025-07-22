import streamlit as st

st.title("This is my first App")

name=st.text_input("Enter your name: ")
st.write(f"Your name is: {name}")

st.header("Do you like Streamlit?")
if st.button("Yes!"):
    st.success("Okay, keep it up........")
if st.button("NO"):
    st.warning("Practice a little bit more!")

s1=st.slider("Enter your age: ",10,90)
st.write(f"your age is: {s1}")

n1=st.number_input("Enter number 1: ",0.00)
n2=st.number_input("Enter number 2: ",0.00)
option=st.selectbox("Select operation",['add','sub','mul','div'])
if st.button("Calculate"):
    if option=='add':
        res=n1+n2
        st.write(f"Result is: {res}")
    elif option=='sub':
        res=n1+n2
        st.write(f"Result is: {res}")
    elif option=='mul':
        res=n1+n2
        st.write(f"Result is: {res}")
    elif option=='div':
        res=n1+n2
        st.write(f"Result is: {res}")
    else:
        st.warning("No option is selected")

st.sidebar.title("user info")

name1=st.sidebar.text_input("Name:")
age1=st.sidebar.number_input("Age:")
st.sidebar.write(f"Name is: {name} and age is: {age1}")

import pandas as pd
df=pd.DataFrame({
    "name":['Ali','sara','zara'],
    "age":[23,45,67],
    "marks":[90,78,99]
})

st.write(df)

f1=st.file_uploader("Upload your file!",type=['csv'])
df2=pd.read_csv(f1)

df3=df2.dropna()
cols=df2.columns.tolist()

s2=st.selectbox("select any of following",cols)
st.write(s2)
st.write(cols)
t1,t2,t3=st.tabs(["Home","About","Contact"])
with t1:
    st.write("home tab")
with t2:
    st.write("about tab")
    st.write(df2.head(8))
with t3:
    st.write("contact tab")