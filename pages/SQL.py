import streamlit as st
from src.func import space

st.title('SQL query')
space(2)

with open('queries/trend.sql', 'r') as file:
    sql_query = file.read()
st.markdown('#### Query used to get dashboard data')
st.code(sql_query, language='sql')
space(2)

with open('queries/test1.sql', 'r') as file:
    sql_query = file.read()
st.markdown('#### Query used to test the number of users in common between the 2 tables')
st.code(sql_query, language='sql')
space(2)

with open('queries/test2.sql', 'r') as file:
    sql_query = file.read()
st.markdown('#### Query used to check the repartition of the plans in the sample')
st.code(sql_query, language='sql')
space(2)

st.markdown('#### I have also done other queries to check and understand '
            'the data, but they are not very relevant for the report.')
