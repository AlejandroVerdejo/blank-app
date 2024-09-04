import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from faker import Faker
import random
import matplotlib.pyplot as plt
import plost

# Configuracion de la pagina #! Siempre al principio
st.set_page_config(
    page_title="Main page",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Crea un dialog para que el usuario introduzca datos
@st.dialog("Cast your vote")
def vote():
    st.write(f"Why is your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.rerun()

def tostada():
    st.toast("Tostadita")

faker = Faker()

st.title("New app.")

# Opciones para las categorias de los elementos
categories = ["alimento","ropa","medicina"]

# Guarda los datos en la sesion para mantenerlos en los refrescos de la pagina
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
            "t_sales":random.randrange(last_month_sales,500),
            "category":random.choice(categories)
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

if "y_finances" not in st.session_state:
    st.session_state["y_finances"] = {
        "in":{
            "2018":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
            "2019":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
            "2020":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
            "2021":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
            "2022":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
            "2023":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
            "2024":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
        },
        "out":{
            "2018":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
            "2019":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
            "2020":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
            "2021":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
            "2022":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
            "2023":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
            "2024":{
                "Enero":random.randrange(90000,250000),
                "Febrero":random.randrange(90000,250000),
                "Marzo":random.randrange(90000,250000),
                "Abril":random.randrange(90000,250000),
                "Mayo":random.randrange(90000,250000),
                "Junio":random.randrange(90000,250000),
                "Julio":random.randrange(90000,250000),
                "Agosto":random.randrange(90000,250000),
                "Septiembre":random.randrange(90000,250000),
                "Octubre":random.randrange(90000,250000),
                "Noviembre":random.randrange(90000,250000),
                "Diciembre":random.randrange(90000,250000),
            },
        }          
    }

if "show_sales" not in st.session_state:
    st.session_state["show_sales"] = "l_sales"

if "finances_mode" not in st.session_state:
    st.session_state["finances_mode"] = "yearly"

if "finances_year" not in st.session_state:
    st.session_state["finances_year"] = 2023

# Crea un contenedor divido en dos columnas
col1,col2 = st.columns(2)

# Añade un boton a la primera columna
col1.button("Click",on_click=vote,use_container_width=True)
# Añade un boton a la segunda columna
col2.button("Tostada",on_click=tostada,use_container_width=True)

st.header("Inventario")

inventory_data_frame = pd.DataFrame(st.session_state["data"])

# Crea un dataFrame con los datos del inventario, ocultando el campo de index y dandole nombre a las columnas
st.data_editor(inventory_data_frame,hide_index=True, use_container_width=True,column_config={
    "name":st.column_config.TextColumn(
        "Nombre",
        help="Nombre del producto"
    ),
    "units":st.column_config.NumberColumn(
        "Unidades",
        help="Unidades en stock del producto",
        min_value=0,
        step=1,
    ),
    "price":st.column_config.NumberColumn(
        "Precio",
        help="Precio del producto",
        min_value=0,
        step=1,
        format="%d€"
    ),
    "restock":st.column_config.NumberColumn(
        "Restock",
        help="Cantidad a la que indicar que es necesario un restock",
        min_value=0,
        step=1,
    ),
    "l_sales":st.column_config.NumberColumn(
        "V. Ultimo mes",
        help="Ventas del producto en el ultimo mes",
        min_value=0,
        step=1,
        disabled=True
    ),
    "t_sales":st.column_config.NumberColumn(
        "V. Totales",
        help="Ventas totales del producto",
        min_value=0,
        step=1,
        disabled=True
    ),
    "category":st.column_config.SelectboxColumn(
        "Categoria",
        help="Categoria del producto",
        options=categories,
        required=True
    )
})

# st.bar_chart(data=data_frame,x="name",x_label="Stock",y="units",y_label="Items", horizontal=True)

# Crea dos tabs para Existencias y Ventas
inventory_tab_1,inventory_tab_2 = st.tabs(["Existencias","Ventas"])

# Cuenta los elementos con menos unidades del numero de restock indicado
count = 0
for i in st.session_state["data"]:
    if i["restock"] > i["units"]:
        count += 1

# En caso de elementos con menos unidades que numero de restock, mostrara un aviso indicando cuantos elementos hay y la informacion de cada uno
if count > 0:
    if count == 1:
        restock_warning = f"Hay {count} elemento por debajo del numero de restock"
        with inventory_tab_1.expander(restock_warning):
            for i in st.session_state["data"]:
                if i["restock"] > i["units"]:
                    item_restock_warning = " ·~ " + i["name"] + " - " + str(i["units"]) + " unidades (" + str(i["restock"]) + ")."
                    st.write(item_restock_warning)
    else:
        restock_warning = f"Hay {count} elementos por debajo del numero de restock"
        with inventory_tab_1.expander(restock_warning):
            for i in st.session_state["data"]:
                if i["restock"] > i["units"]:
                    item_restock_warning = " ·~ " + i["name"] + " - " + str(i["units"]) + " unidades (" + str(i["restock"]) + ")."
                    st.write(item_restock_warning)

# Añade la tabla con las unidades de cada elemento al primer tab
inventory_tab_1.altair_chart(
    # Muestra las unidades
    alt.Chart(inventory_data_frame).mark_bar(orient="horizontal",color="#3b57e3").encode(alt.X("units",title=""),alt.Y("name",title=""))
    # Muestra el punto de restock
    +alt.Chart(inventory_data_frame).mark_point(shape="diamond",filled=True,size=50,color="red",opacity=1).encode(x="restock",y="name"),use_container_width=True
    )

# Añade un radio al segundo tab para seleccionar si mostrara las ventas totales o del ultimo mes
with inventory_tab_2:
    sales_radio = st.radio(label="",options=["Ultimo mes","Totales"],horizontal=True)

# Cambia la variable de sesion segun el radio
if sales_radio == "Ultimo mes":
    st.session_state["show_sales"] = "l_sales"
else:
    st.session_state["show_sales"] = "t_sales"

# Mostrara las ventas de los productos, mostrando las totales o las del ultimo mes segun la variable de sesion
inventory_tab_2.altair_chart(
    alt.Chart(inventory_data_frame).mark_bar(orient="horizontal",color="#3b57e3").encode(alt.X(st.session_state["show_sales"],title=""),alt.Y("name",title="")),use_container_width=True
)

plost.pie_chart(
    data=inventory_data_frame,
    theta=st.session_state["show_sales"]
)

st.header("Finanzas")

# finances_show_mode = st.radio(label="",options=["Anuales","Mensuales"],horizontal=True)

# if finances_show_mode == "Anuales":
#     st.session_state["finances_mode"] = "yearly"
# else:
#     st.session_state["finances_mode"] = "monthly"

# if st.session_state["finances_mode"] == "monthly":
#     select = st.selectbox(label="",options=[2018,2019,2020,2021,2022,2023,2024])

# finances_data = {
#     "in":{},
#     "out":{}
# }

# for data in st.session_state["finances"]["in"]:
#     finances_data["in"]

# Crea dos tabs para Ingresos y Gastos
finances_tab_1,finances_tab_2 = st.tabs(["Ingresos","Gastos"])

# Añade la tabla de los ingresos al primer tab
finances_tab_1.bar_chart(st.session_state["finances"]["in"],color="#2fde5d")
# Añade la tabla de los ingresos al segundo tab
finances_tab_2.bar_chart(st.session_state["finances"]["out"],color="#de2f2f")

st.subheader("Balance")

# Crea el grafico de lineas con los ingresos y gastos
finances_chart_data = pd.DataFrame(
    st.session_state["finances"],columns=["in","out"]
    )

# Da nombre a las columnas(lineas)
finances_chart_data.columns = ["Ingresos","Gastos"]

# Cambia el color de cada linea
st.line_chart(finances_chart_data,color=["#de2f2f","#2fde5d"])