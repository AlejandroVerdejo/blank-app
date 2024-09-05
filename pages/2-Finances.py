import streamlit as st
import random
import pandas as pd

# Configuracion de la pagina #! Siempre al principio
st.set_page_config(
    page_title="Main page",
    layout="wide",
    initial_sidebar_state="expanded"
)

YEARS = ["2020","2021","2022","2023"]

if "finances" not in st.session_state:
    st.session_state["finances"] = {
        "in":{
            "2020":{
                "01-Enero":random.randrange(90000,250000),
                "02-Febrero":random.randrange(90000,250000),
                "03-Marzo":random.randrange(90000,250000),
                "04-Abril":random.randrange(90000,250000),
                "05-Mayo":random.randrange(90000,250000),
                "06-Junio":random.randrange(90000,250000),
                "07-Julio":random.randrange(90000,250000),
                "08-Agosto":random.randrange(90000,250000),
                "09-Septiembre":random.randrange(90000,250000),
                "10-Octubre":random.randrange(90000,250000),
                "11-Noviembre":random.randrange(90000,250000),
                "12-Diciembre":random.randrange(90000,250000),            
            },
            "2021":{
                "01-Enero":random.randrange(90000,250000),
                "02-Febrero":random.randrange(90000,250000),
                "03-Marzo":random.randrange(90000,250000),
                "04-Abril":random.randrange(90000,250000),
                "05-Mayo":random.randrange(90000,250000),
                "06-Junio":random.randrange(90000,250000),
                "07-Julio":random.randrange(90000,250000),
                "08-Agosto":random.randrange(90000,250000),
                "09-Septiembre":random.randrange(90000,250000),
                "10-Octubre":random.randrange(90000,250000),
                "11-Noviembre":random.randrange(90000,250000),
                "12-Diciembre":random.randrange(90000,250000),
            }, 
            "2022":{
                "01-Enero":random.randrange(90000,250000),
                "02-Febrero":random.randrange(90000,250000),
                "03-Marzo":random.randrange(90000,250000),
                "04-Abril":random.randrange(90000,250000),
                "05-Mayo":random.randrange(90000,250000),
                "06-Junio":random.randrange(90000,250000),
                "07-Julio":random.randrange(90000,250000),
                "08-Agosto":random.randrange(90000,250000),
                "09-Septiembre":random.randrange(90000,250000),
                "10-Octubre":random.randrange(90000,250000),
                "11-Noviembre":random.randrange(90000,250000),
                "12-Diciembre":random.randrange(90000,250000),
            }, 
            "2023":{
                "01-Enero":random.randrange(90000,250000),
                "02-Febrero":random.randrange(90000,250000),
                "03-Marzo":random.randrange(90000,250000),
                "04-Abril":random.randrange(90000,250000),
                "05-Mayo":random.randrange(90000,250000),
                "06-Junio":random.randrange(90000,250000),
                "07-Julio":random.randrange(90000,250000),
                "08-Agosto":random.randrange(90000,250000),
                "09-Septiembre":random.randrange(90000,250000),
                "10-Octubre":random.randrange(90000,250000),
                "11-Noviembre":random.randrange(90000,250000),
                "12-Diciembre":random.randrange(90000,250000),
            }, 
        },
        "out":{
            "2020":{
                "01-Enero":random.randrange(90000,250000),
                "02-Febrero":random.randrange(90000,250000),
                "03-Marzo":random.randrange(90000,250000),
                "04-Abril":random.randrange(90000,250000),
                "05-Mayo":random.randrange(90000,250000),
                "06-Junio":random.randrange(90000,250000),
                "07-Julio":random.randrange(90000,250000),
                "08-Agosto":random.randrange(90000,250000),
                "09-Septiembre":random.randrange(90000,250000),
                "10-Octubre":random.randrange(90000,250000),
                "11-Noviembre":random.randrange(90000,250000),
                "12-Diciembre":random.randrange(90000,250000),            
            },
            "2021":{
                "01-Enero":random.randrange(90000,250000),
                "02-Febrero":random.randrange(90000,250000),
                "03-Marzo":random.randrange(90000,250000),
                "04-Abril":random.randrange(90000,250000),
                "05-Mayo":random.randrange(90000,250000),
                "06-Junio":random.randrange(90000,250000),
                "07-Julio":random.randrange(90000,250000),
                "08-Agosto":random.randrange(90000,250000),
                "09-Septiembre":random.randrange(90000,250000),
                "10-Octubre":random.randrange(90000,250000),
                "11-Noviembre":random.randrange(90000,250000),
                "12-Diciembre":random.randrange(90000,250000),
            },
            "2022":{
                "01-Enero":random.randrange(90000,250000),
                "02-Febrero":random.randrange(90000,250000),
                "03-Marzo":random.randrange(90000,250000),
                "04-Abril":random.randrange(90000,250000),
                "05-Mayo":random.randrange(90000,250000),
                "06-Junio":random.randrange(90000,250000),
                "07-Julio":random.randrange(90000,250000),
                "08-Agosto":random.randrange(90000,250000),
                "09-Septiembre":random.randrange(90000,250000),
                "10-Octubre":random.randrange(90000,250000),
                "11-Noviembre":random.randrange(90000,250000),
                "12-Diciembre":random.randrange(90000,250000),
            },
            "2023":{
                "01-Enero":random.randrange(90000,250000),
                "02-Febrero":random.randrange(90000,250000),
                "03-Marzo":random.randrange(90000,250000),
                "04-Abril":random.randrange(90000,250000),
                "05-Mayo":random.randrange(90000,250000),
                "06-Junio":random.randrange(90000,250000),
                "07-Julio":random.randrange(90000,250000),
                "08-Agosto":random.randrange(90000,250000),
                "09-Septiembre":random.randrange(90000,250000),
                "10-Octubre":random.randrange(90000,250000),
                "11-Noviembre":random.randrange(90000,250000),
                "12-Diciembre":random.randrange(90000,250000),
            },
        }    
    }

st.title("Finanzas")

# Crea los tabs para dividir las finanzas entre anuales y mensuales
finances_yearly_tab, finances_monthly_tab = st.tabs(["Anual","Mensual"])

yearly_data = {
    "in":{},
    "out":{}
}

# Suma los meses de cada año para tener los datos anuales
for year in st.session_state["finances"]["in"].keys():
    yearly_data["in"][year] = sum(st.session_state["finances"]["in"][year].values())
    yearly_data["out"][year] = sum(st.session_state["finances"]["out"][year].values())

# Crea el dataframe con los ingresos y gastos
dtf_yearly_data = pd.DataFrame(
    yearly_data,columns=["in","out"]
)

# Da nombre a las columnas
dtf_yearly_data.columns = ["1-Ingresos","2-Gastos"]

# Crea dos columnas en el tab Anuales para los graficos de barras
with finances_yearly_tab:
    finances_yearly_tab_col1, finances_yearly_tab_col2 = st.columns(2)

# Añade el grafico de barras de Ingresos anuales
finances_yearly_tab_col1.bar_chart(yearly_data["in"],color="#2fde5d",x_label="Ingresos")
# Añade el grafico de barras de Gastos anuales
finances_yearly_tab_col2.bar_chart(yearly_data["out"],color="#de2f2f",x_label="Gastos")

finances_yearly_tab.subheader("Balance")

# Añade el grafico de lineas con los ingresos y gastos anuales
finances_yearly_tab.line_chart(dtf_yearly_data,color=["#2fde5d","#de2f2f"])

with finances_monthly_tab:
    # Crea los tabs para cada año en el tab de finanzas mensuales
    tabs = st.tabs(st.session_state["finances"]["in"].keys())
    for i in range(0,len(tabs)):
        # Guarda los datos de los meses del año de ese tab
        selected_year_data = {
            "in":st.session_state["finances"]["in"][YEARS[i]],
            "out":st.session_state["finances"]["out"][YEARS[i]]
        }

        # Crea el dataframe con los ingresos y gastos de ese año
        dtf_monthly_data = pd.DataFrame(
            selected_year_data,columns=["in","out"]
            # st.session_state[]    
        )
        # Crea las columnas para los graficos de barras para ese año
        with tabs[i]:
            finances_monthly_tab_col1, finances_monthly_tab_col2 = st.columns(2)
        # Añade el grafico de barras de Ingresos de ese año
        finances_monthly_tab_col1.bar_chart(selected_year_data["in"],color="#2fde5d",x_label="Ingresos "+YEARS[i])
        # Añade el grafico de barras de Gastos de ese año
        finances_monthly_tab_col2.bar_chart(selected_year_data["out"],color="#de2f2f",x_label="Gastos "+YEARS[i])
        
        # Da nombre a las columnas del dataframe
        dtf_monthly_data.columns = ["1-Ingresos","2-Gastos"]
        tabs[i].subheader("Balance")
        # Añade el grafico de lineas de los ingresos y gastos de ese año
        tabs[i].line_chart(dtf_monthly_data,x_label=YEARS[i],color=["#2fde5d","#de2f2f"])