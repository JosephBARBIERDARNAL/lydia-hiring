import streamlit as st
from src.func import space

# title
st.title("CRM campaign")
space(2)

# short description
st.markdown("""
            This is the report of the project for the CRM Team.
            
            In order to know which users will be most relevant
            for a Lydia roulette communications campaign, we need to consider the following elements.
            - Users who **already use Lydia** regularly are of little interest. 
            - Users who have not used Lydia for a long time are also of little interest.
            It means we have to define a **threshold** for the time since last activity.
            - Define a list of user features relevant to the segmentation issue:
            age, time since last activity, way of using Lydia (trading, stock market, savings...) etc. 
            
            The next step is to define the metrics and KPIs that best measure the campaign's impact.
            To do this, we can look at :
            - the **relative change in Lydia use** (number of average weekly uses over the 3
            months prior to the campaign VS new daily use). We can create a visualization
            of the evolution of the distribution of this metric (histogram, violin plot...),
            to **avoid aggregating** it and retain maximum information. 
            - the relative **change in the number of users** who have made a transaction
            (or several transactions) in the last 3 months. We can also create a visualization
            of the evolution of the distribution of this metric. 
            
            To optimize the type of campaign to keep, we can imagine an **AB test**, with 2 or 3 different groups.
            - the groups must be sampled from the same population (and this population
            must meet the segmentation criteria)
            - the groups should differ in the campaign **only** in the type of communication received
            - we need to define which campaigns will be sent. This depends on what
            we want to test: a campaign with variations of an e-mail on Lydia roulette,
            a campaign with either a message on the app or by e-mail, etc. In my opinion,
            it seems **more relevant** to compare the impact between mail VS message on the app,
            in order to use the test results as **a priori** for other tests (important for Bayesian inferences). 
            - finally, we need to use the metrics defined above to define a statistical
            means of detecting differences. A common way to do this is with a Student's t test or an Anova,
            depending on the number of groups. 

            """)