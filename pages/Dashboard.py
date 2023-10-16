import streamlit as st
import pandas as pd
from src.func import space
from src.chart import line_chart, barchart, stacked_barchart, histogram

# title
st.title('Dashboard')

#open file
df = pd.read_csv('trend.csv')
df['date_reimbursement'] = pd.to_datetime(df['date_reimbursement'])

# filter date (default to first and last date)
date_start = pd.to_datetime(st.sidebar.date_input('Start date', df['date_reimbursement'].min()))
date_end = pd.to_datetime(st.sidebar.date_input('End date', df['date_reimbursement'].max()))
space(2)

#line chart
line_chart(df, 'date_reimbursement', 'amount_paid',
           date_start, date_end)

#histogram
bins = st.slider('Number of bins', 1, 100, 20)
histogram(df, 'amount_paid', date_start, date_end, bins)

#barchart
barchart(df, 'date_reimbursement', 'count_transaction',
            date_start, date_end)

#staked barchart
stacked_barchart(df, 'date_reimbursement',
                 date_start, date_end)



