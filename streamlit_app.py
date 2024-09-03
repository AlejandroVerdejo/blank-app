import streamlit as st
import pandas as pd

st.markdown("# Main page 🎈")
# st.sidebar.markdown("# Main page 🎈")

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

data = [
    {
        "name":"K",
        "age":20
    },
    {
        "name":"K",
        "age":33
    }    
]

df = pd.DataFrame({
    data
})

df
