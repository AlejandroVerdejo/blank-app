import streamlit as st
import random
from faker import Faker
import altair as alt
import pandas as pd
import plotly.graph_objects as go
from streamlit_gsheets import GSheetsConnection

# Configuracion de la pagina #! Siempre al principio
st.set_page_config(
    page_title="Main page",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Crea una conexion con la base de datos (GoogleSheet)
# conn = st.connection(spreadsheet="https://docs.google.com/spreadsheets/d/1u9tYEHSsOnzZdVIalTaQyEVlw5wEBa1mBZDCqsi7IMQ/edit?usp=sharing", type=GSheetsConnection)
# conn = st.connection("gsheets", type=GSheetsConnection)
# st.write(conn._connection_name)
# inventory_data = conn.read(
#     worksheet="inventory"
# )
# conn = st.connection("gsheets", type=GSheetsConnection)
# df = conn.read(
#     worksheet="inventory",
#     usecols=[0, 1],
#     nrows=3,
# )

# Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has :{row.units}:")

faker = Faker()

categories = ["alimento","ropa","medicina"]

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


st.title("Inventario")


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

# Crea un selector para elegir las categorias que se muestren en los graficos
options = st.multiselect("Categorias:",categories,categories)

# Filtra los datos del inventario para sacar unicamente los de las categorias seleccionadas
def category_filter(inventory):
    # Lista en la que se añadiran los datos filtrados
    filtered_inventory = []
    for item in inventory:
        # Si la categoria se encuentra en las seleccionadas
        if item["category"] in options:
            filtered_inventory.append(item)
    return filtered_inventory

# Lista con los datos filtrados por categoria
filtered_inventory = category_filter(st.session_state["data"])

# Crea el DataFrame con los datos filtrados para los graficos
graph_inventory_data_frame = pd.DataFrame(filtered_inventory)

# Crea dos tabs para Existencias y Ventas
inventory_tab_1,inventory_tab_2 = st.tabs(["Existencias","Ventas"])

# Cuenta los elementos con menos unidades del numero de restock indicado
count = 0
for i in filtered_inventory:
    if i["restock"] > i["units"]:
        count += 1

# En caso de elementos con menos unidades que numero de restock, mostrara un aviso indicando cuantos elementos hay y la informacion de cada uno
if count > 0:
    if count == 1:
        restock_warning = f"Hay {count} elemento por debajo del numero de restock"
        with inventory_tab_1.expander(restock_warning):
            for i in filtered_inventory:
                if i["restock"] > i["units"]:
                    item_restock_warning = " ·~ " + i["name"] + " - " + str(i["units"]) + " unidades (" + str(i["restock"]) + ")."
                    st.write(item_restock_warning)
    else:
        restock_warning = f"Hay {count} elementos por debajo del numero de restock"
        with inventory_tab_1.expander(restock_warning):
            for i in filtered_inventory:
                if i["restock"] > i["units"]:
                    item_restock_warning = " ·~ " + i["name"] + " - " + str(i["units"]) + " unidades (" + str(i["restock"]) + ")."
                    st.write(item_restock_warning)

# Añade la tabla con las unidades de cada elemento al primer tab
inventory_tab_1.altair_chart(
    # Muestra las unidades
    alt.Chart(graph_inventory_data_frame).mark_bar(orient="horizontal",color="#3b57e3").encode(alt.X("units",title=""),alt.Y("name",title=""))
    # Muestra el punto de restock
    +alt.Chart(graph_inventory_data_frame).mark_point(shape="diamond",filled=True,size=50,color="red",opacity=1).encode(x="restock",y="name"),use_container_width=True
    )

# Añade un radio al segundo tab para seleccionar si mostrara las ventas totales o del ultimo mes
with inventory_tab_2:
    sales_radio = st.radio(label="",options=["Ultimo mes","Totales"],horizontal=True, label_visibility="collapsed")

# Cambia la variable de sesion segun el radio
if sales_radio == "Ultimo mes":
    st.session_state["show_sales"] = "l_sales"
else:
    st.session_state["show_sales"] = "t_sales"

# Mostrara las ventas de los productos, mostrando las totales o las del ultimo mes segun la variable de sesion #* Con grafico de barras
inventory_tab_2.altair_chart(
    alt.Chart(graph_inventory_data_frame).mark_bar(orient="horizontal",color="#3b57e3").encode(alt.X(st.session_state["show_sales"],title=""),alt.Y("name",title="")),use_container_width=True
)

# Mostrara las ventas de los productos, mostrando las totales o las del ultimo mes segun la variable de sesion #* Con grafico de quesitos
# fig = go.Figure(data=[go.Pie(labels=inventory_data_frame["name"], values=inventory_data_frame[st.session_state["show_sales"]])])
# fig.update_layout(width=700, height=500)
# inventory_tab_2.plotly_chart(fig)