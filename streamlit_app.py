import streamlit as st
import pandas as pd
import numpy as np

# @st.dialog("Cast your vote")
def vote():
    st.write(f"Why is your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.rerun()

st.markdown("# Main page")
# st.sidebar.markdown("# Main page")

st.title("New app")

data = [
    {
        "name":"p1",
        "units":20,
        "price":7,
        "restock":10
    },
    {
        "name":"p2",
        "units":33,
        "price":13,
        "restock":15
    }    
]

finances = {
    "in":{
        "2020":100,
        "2021":182,
        "2022":98,
        "2023":80
    },
    "out":{
        "2020":120,
        "2021":18,
        "2022":50,
        "2023":8
    }          
}

click = st.button("Click",on_click=vote)

# data_frame = pd.DataFrame({
#     "first column":[1,2,3,4],
#     "second column":[10,20,30,40]
# })
data_frame = pd.DataFrame(data)

st.dataframe(data_frame,hide_index=True, width=1000)

st.bar_chart(data=data_frame,x="name",x_label="Stock",y="units",y_label="Items", horizontal=True)

chart_data = pd.DataFrame(
    finances
    #  np.random.randn(20, 3),
    #  columns=['a', 'b', 'c']
    )

st.line_chart(chart_data)
