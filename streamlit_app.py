import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from faker import Faker
import random

@st.dialog("Cast your vote")
def vote():
    st.write(f"Why is your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.rerun()

def tostada():
    st.toast("Tostada")

faker = Faker()

st.title("New app.")
# st.set_page_config(page_title="Main")
# st.sidebar.title("Main page")

# st.markdown("")
# st.sidebar.markdown("# Main page")

# st.Page(title="Main page")

data = []

for i in range(1,15):
    data.append({
        "name":faker.name(),
        "units":random.randrange(1,200),
        "price":random.randrange(1,50),
        "restock":random.randrange(1,100)        
    })

finances = {
    "in":{
        "2018":random.randrange(90000,250000),
        "2019":random.randrange(90000,250000),
        "2020":random.randrange(90000,250000),
        "2021":random.randrange(90000,250000),
        "2022":random.randrange(90000,250000),
        "2023":random.randrange(90000,250000),
        "2024":random.randrange(90000,250000),
    },
    "out":{
        "2018":random.randrange(90000,250000),
        "2019":random.randrange(90000,250000),
        "2020":random.randrange(90000,250000),
        "2021":random.randrange(90000,250000),
        "2022":random.randrange(90000,250000),
        "2023":random.randrange(90000,250000),
        "2024":random.randrange(90000,250000),
    }          
}

col1,col2 = st.columns(2)

col1.button("Click",on_click=vote,use_container_width=True)
col2.button("Tostada",on_click=tostada,use_container_width=True)

# click = st.button("Click",on_click=vote)

# data_frame = pd.DataFrame({
#     "first column":[1,2,3,4],
#     "second column":[10,20,30,40]
# })

st.header("Inventario")

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
        # st.warning(f"Hay {count} elemento por debajo del numero de restock")
        # with st.expander(st.warning(f"Hay {count} elemento por debajo del numero de restock")):
        restock_warning = f"Hay {count} elemento por debajo del numero de restock"
        with st.expander(restock_warning):
            # st.write("x")
            for i in data:
                if i["restock"] > i["units"]:
                    item_restock_warning = " ·~ " + i["name"] + " - " + str(i["units"]) + " unidades (" + str(i["restock"]) + ")."
                    st.write(item_restock_warning)
    else:
        # st.warning(f"Hay {count} elementos por debajo del numero de restock")
        restock_warning = f"Hay {count} elementos por debajo del numero de restock"
        with st.expander(restock_warning):
            # st.write("x")
            for i in data:
                if i["restock"] > i["units"]:
                    item_restock_warning = " ·~ " + i["name"] + " - " + str(i["units"]) + " unidades (" + str(i["restock"]) + ")."
                    st.write(item_restock_warning)

st.altair_chart(
    # alt.Chart(data_frame).mark_bar(orient="horizontal").encode(x="units",y="name")
    alt.Chart(data_frame).mark_bar(orient="horizontal").encode(alt.X("units",title="Unidades"),alt.Y("name",title="Nombres"))
    +alt.Chart(data_frame).mark_point(shape="diamond",filled=True,size=50,color="red",opacity=1).encode(x="restock",y="name"),use_container_width=True
    )

st.header("Finanzas")

tab1,tab2 = st.tabs(["Ingresos","Gastos"])

tab1.bar_chart(finances["in"],color="#3b57e3")
tab2.bar_chart(finances["out"],color="#3b57e3")

st.subheader("Balance")

chart_data = pd.DataFrame(
    finances,columns=["in","out"]
    #  np.random.randn(20, 3),
    #  columns=['a', 'b', 'c']
    )

chart_data.columns = ["Ingresos","Gastos"]

st.line_chart(chart_data,color=["#de2f2f","#2fde5d"])

