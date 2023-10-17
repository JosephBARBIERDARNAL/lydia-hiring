import streamlit as st
from src.func import space



st.title('About')
st.markdown('### This web application is a simple tool built to visualize '
            'data about Lydia Roulette, by Joseph Barbier.')
space(2)

st.markdown('### Sidebar menu')
st.markdown('''
            - **Dashboard**: this page contains 4 charts:
                - A line chart showing the evolution of amounts paid by Lydia, per day.
                - A histogram illustrating the distribution of amounts paid
                - A bar chart showing the number of transactions per day.
                - A stacked bar chart showing the proportion of transactions per plan.
            
            - **Report of the dashboard**: this page contains a report of the dashboard.
            
            - **CRM campaign**: this page contains a report of the CRM campaign.
            
            - **SQL**: this page contains the SQL queries used to build the dashboard.
            ''')
space(2)
st.markdown('The source code of this web application is available at [this link](https://github.com/JosephBARBIERDARNAL/lydia-hiring)')