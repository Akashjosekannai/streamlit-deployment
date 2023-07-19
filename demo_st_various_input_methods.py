import streamlit as st
import pickle

st.title("Streamlit Demo: Input Data")

with open ('model_pickle','rb') as f:
    model =pickle.load(f)

# Text Field carat
st.subheader("carat")
carat = st.text_input("Enter some text",key=1)
st.write("Text input:", carat)

# Text Field cut
st.subheader("Cut")
cut = st.text_input("Enter some text",key=2)
st.write("Text input:", cut)

# Text Field color
st.subheader("Color")
color = st.text_input("Enter some text",key=3)
st.write("Text input:", color)


# Text Field clarity
st.subheader("Clarity")
clarity = st.text_input("Enter some text",key=4)
st.write("Text input:", clarity)


# Text Field depth
st.subheader("Depth")
depth = st.text_input("Enter some text",key=5)
st.write("Text input:", depth)


# Text Field table
st.subheader("Table")
table = st.text_input("Enter some text",key=6)
st.write("Text input:", table)


# Button
st.subheader("For Price")
if st.button("Click Me"):
    st.write("Button was clicked!")
    yhat_test=model.predict([[carat, cut,color,clarity,depth,table]])
    st.write("Predicted Price",yhat_test )

