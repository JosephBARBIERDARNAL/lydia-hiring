import streamlit as st
from src.func import space

st.title('SQL query')
space(2)

with open('queries/trend.sql', 'r') as file:
    sql_query = file.read()

st.markdown('#### Query used to get dashboard data')
st.code(sql_query, language='sql')