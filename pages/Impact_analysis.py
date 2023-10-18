import streamlit as st
from src.func import space

# title
st.title("Impact analysis of Lydia roulette campaign")
space(2)

# short description
st.markdown("""
            Being in exam period and with work on the side, I unfortunately didn't have time to do Lydia roulette's impact analysis.

However, here's the approach I would have taken in a situation more advantageous to me:
- Retrieve all purchases made with Lydia for individuals having won at least once in the data date range
- Filter individuals to have won Lydia roulette at least one week before the last date and at least one week after the first date of the data set
- Look at and compare the distribution of the number of purchases made with Lydia per user in the week preceding the win and the following week
- Statistically compare the average number of purchases before and after the win

            """)