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
        "name":"p1",
        "units":20,
        "price":7
    },
    {
        "name":"p2",
        "units":33,
        "price":13
    }    
]

# df = pd.DataFrame({
#     "first column":[1,2,3,4],
#     "second column":[10,20,30,40]
# })
df = pd.DataFrame(data)

df
