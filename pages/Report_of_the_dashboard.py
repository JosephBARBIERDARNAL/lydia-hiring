import streamlit as st
from src.func import space

# title
st.title("Report and methods")
space(2)

# short description
st.markdown("""
            This is the report of the dashboard for the Product Team.
            
            The Dashboard page contains 4 charts: 
            
            - A **line chart** showing the evolution of amounts paid by Lydia, per day.
            The first thing that stands out is the peak of over €4,000 on December 28. 
            - A **histogram** illustrating the distribution of amounts paid, showing that
            most of the amounts in the sample are below 1500€ (only 3 are above).
            - A **bar chart** showing the number of transactions per day. The days with the
            most transactions are generally Mondays. Overall, the number of transactions
            is relatively stable over time.
            - A **stacked bar chart** showing the proportion of transactions per plan.
            The distribution of plan types is relatively stable over time.
            This is an expected effect, given that the choice of winning users is random
            (i.e. independent of the plan). 
            
            Limitations:
            - With more time, the implementation of a **date granularity feature**
            (day, week, month) would have been relevant.
            - With more data, **distribution graphs** could have provided a wealth
            of information that is difficult to visualize at present.
            - Add a cache system to avoid reloading the data at each page refresh.
            
            
            """)