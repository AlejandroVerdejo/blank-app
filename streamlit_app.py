import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

@st.dialog("Cast your vote")
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
    },
    {
        "name":"p3",
        "units":3,
        "price":80,
        "restock":5
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

col1,col2 = st.columns(2)

col1.button("Click",on_click=vote,use_container_width=True)
col2.button("Back",use_container_width=True)

# click = st.button("Click",on_click=vote)

# data_frame = pd.DataFrame({
#     "first column":[1,2,3,4],
#     "second column":[10,20,30,40]
# })
data_frame = pd.DataFrame(data)

st.dataframe(data_frame,hide_index=True, use_container_width=True,column_config={
    "name":"Nombre",
    "units":"Unidades",
    "price":"Precio",
    "restock":"Restock"
})

# st.table(data_frame)

# st.bar_chart(data=data_frame,x="name",x_label="Stock",y="units",y_label="Items", horizontal=True)

count = 0
for i in data:
    if i["restock"] > i["units"]:
        count += 1

if count > 0:
    if count == 1:
        st.warning(f"Hay {count} elemento por debajo del numero de restock")
    else:
        st.warning(f"Hay {count} elementos por debajo del numero de restock")

st.altair_chart(
    # alt.Chart(data_frame).mark_bar(orient="horizontal").encode(x="units",y="name")
    alt.Chart(data_frame).mark_bar(orient="horizontal").encode(alt.X("units",title="Unidades"),alt.Y("name",title="Nombres"))
    +alt.Chart(data_frame).mark_point(shape="diamond",filled=True,size=50,color="red",opacity=1).encode(x="restock",y="name"),use_container_width=True
    )

chart_data = pd.DataFrame(
    finances
    #  np.random.randn(20, 3),
    #  columns=['a', 'b', 'c']
    )

st.line_chart(chart_data)
