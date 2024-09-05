import streamlit as st
import random
import faker

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