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

if "data" not in st.session_state:
    st.session_state["data"] = []
    for i in range(1,15):
        last_month_sales = random.randrange(1,100)
        st.session_state["data"].append({
            "name":faker.name(),
            "units":random.randrange(1,200),
            "price":random.randrange(1,50),
            "restock":random.randrange(1,100),
            "l_sales":last_month_sales,
            "t_sales":random.randrange(last_month_sales,500)
            # "sales":random.randrange(1,100)
        })

if "finances" not in st.session_state:
    st.session_state["finances"] = {
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

if "show_sales" not in st.session_state:
    st.session_state["show_sales"] = "l_sales"

col1,col2 = st.columns(2)

col1.button("Click",on_click=vote,use_container_width=True)
col2.button("Tostada",on_click=tostada,use_container_width=True)

# click = st.button("Click",on_click=vote)

# data_frame = pd.DataFrame({
#     "first column":[1,2,3,4],
#     "second column":[10,20,30,40]
# })

st.header("Inventario")


inventory_data_frame = pd.DataFrame(st.session_state["data"])

st.dataframe(inventory_data_frame,hide_index=True, use_container_width=True,column_config={
    "name":"Nombre",
    "units":"Unidades",
    "price":"Precio",
    "restock":"Restock",
    "l_sales":"Ventas ultimo mes",
    "t_sales":"Ventas totales"
})

# st.table(data_frame)

# st.bar_chart(data=data_frame,x="name",x_label="Stock",y="units",y_label="Items", horizontal=True)

inventory_tab_1,inventory_tab_2 = st.tabs(["Existencias","Ventas"])

count = 0
for i in st.session_state["data"]:
    if i["restock"] > i["units"]:
        count += 1

if count > 0:
    if count == 1:
        # st.warning(f"Hay {count} elemento por debajo del numero de restock")
        # with st.expander(st.warning(f"Hay {count} elemento por debajo del numero de restock")):
        restock_warning = f"Hay {count} elemento por debajo del numero de restock"
        with inventory_tab_1.expander(restock_warning):
            # st.write("x")
            for i in st.session_state["data"]:
                if i["restock"] > i["units"]:
                    item_restock_warning = " ·~ " + i["name"] + " - " + str(i["units"]) + " unidades (" + str(i["restock"]) + ")."
                    st.write(item_restock_warning)
    else:
        # st.warning(f"Hay {count} elementos por debajo del numero de restock")
        restock_warning = f"Hay {count} elementos por debajo del numero de restock"
        with inventory_tab_1.expander(restock_warning):
            # st.write("x")
            for i in st.session_state["data"]:
                if i["restock"] > i["units"]:
                    item_restock_warning = " ·~ " + i["name"] + " - " + str(i["units"]) + " unidades (" + str(i["restock"]) + ")."
                    st.write(item_restock_warning)

inventory_tab_1.altair_chart(
    # alt.Chart(data_frame).mark_bar(orient="horizontal").encode(x="units",y="name")
    alt.Chart(inventory_data_frame).mark_bar(orient="horizontal",color="#3b57e3").encode(alt.X("units",title=""),alt.Y("name",title=""))
    +alt.Chart(inventory_data_frame).mark_point(shape="diamond",filled=True,size=50,color="red",opacity=1).encode(x="restock",y="name"),use_container_width=True
    )

with inventory_tab_2:
    sales_radio = st.radio(label="",options=["Ultimo mes","Totales"],horizontal=True,key="sales_radio")

if sales_radio == "Ultimo mes":
    st.session_state["show_sales"] = "l_sales"
else:
    st.session_state["show_sales"] = "t_sales"

inventory_tab_2.altair_chart(
    alt.Chart(inventory_data_frame).mark_bar(orient="horizontal",color="#3b57e3").encode(alt.X(st.session_state["show_sales"],title=""),alt.Y("name",title="")),use_container_width=True
)

sales = []
for i in range(1,20):
    # sales.append(data["l_sales"])
    sales.append(random.randrange(100,1000))

priority_plot = (
    alt.Chart(sales)
    .mark_arc()
    .encode(theta="count():Q", color="Priority:N")
    .properties(height=300)
    .configure_legend(
        orient="bottom", titleFontSize=14, labelFontSize=14, titlePadding=5
    )
)
st.altair_chart(priority_plot, use_container_width=True, theme="streamlit")

st.header("Finanzas")

finances_tab_1,finances_tab_2 = st.tabs(["Ingresos","Gastos"])

finances_tab_1.bar_chart(st.session_state["finances"]["in"],color="#2fde5d")
finances_tab_2.bar_chart(st.session_state["finances"]["out"],color="#de2f2f")

st.subheader("Balance")

finances_chart_data = pd.DataFrame(
    st.session_state["finances"],columns=["in","out"]
    #  np.random.randn(20, 3),
    #  columns=['a', 'b', 'c']
    )

finances_chart_data.columns = ["Ingresos","Gastos"]

st.line_chart(finances_chart_data,color=["#de2f2f","#2fde5d"])

