import streamlit as st
import pandas as pd
import numpy as np

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

finances = {
    "2020":{
        "in":100,
        "out":20
    },
    "2021":{
        "in":115,
        "out":70
    },
    "2022":{
        "in":170,
        "out":22
    },
    "2023":{
        "in":40,
        "out":10
    }           
}

# df = pd.DataFrame({
#     "first column":[1,2,3,4],
#     "second column":[10,20,30,40]
# })
df = pd.DataFrame(data)

df

chart_data = pd.DataFrame(
    finances
    #  np.random.randn(20, 3),
    #  columns=['a', 'b', 'c']
    )

st.line_chart(chart_data)
