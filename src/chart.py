import plotly.graph_objects as go
import streamlit as st


def line_chart(df, x, y, date_start, date_end):

    # Filter dataframe
    df = df[(df[x] >= date_start) & (df[x] <= date_end)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df[x], y=df[y], mode='lines+markers', name='Amount paid'))
    fig.update_layout(
        title='Amount paid Daily',
        xaxis=dict(title='Date (daily)'),
        yaxis=dict(title='Amount paid by Lydia'),
        showlegend=True,
        legend=dict(x=0.02, y=0.98),
    )
    st.plotly_chart(fig, use_container_width=True)


def histogram(df, x, date_start, date_end, bins):

    # Create a histogram using Plotly graph objects
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df[x], nbinsx=bins))

    fig.update_layout(
        title="Distribution of Amount paid by Lydia",
        xaxis_title="Value",
        yaxis_title="Frequency",
        bargap=0.05
    )

    st.plotly_chart(fig, use_container_width=True)

def barchart(df, x, y, date_start, date_end):

    # Filter dataframe
    df = df[(df[x] >= date_start) & (df[x] <= date_end)]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=df[x], y=df[y], marker_color='lightblue', name='# Transaction'))
    fig.update_layout(
        title='Number of transactions',
        xaxis=dict(title='Date (daily)'),
        yaxis=dict(title='# Transaction'),
        showlegend=True,
        legend=dict(x=0.02, y=0.98),
    )
    st.plotly_chart(fig, use_container_width=True)



def stacked_barchart(df, x, date_start, date_end):

    # Filter dataframe
    df = df[(df[x] >= date_start) & (df[x] <= date_end)]

    df['Black'] = df['black_plan_prop']
    df['Blue'] = df['blue_plan_prop']
    df['No Plan'] = df['noplan_prop']

    colors = ['black', '#1f77b4', 'gold']

    fig = go.Figure()
    for i, col in enumerate(['Black', 'Blue', 'No Plan']):
        fig.add_trace(go.Bar(
            x=df[x],
            y=df[col],
            name=col,
            hoverinfo='y+name',
            marker_color=colors[i]
        ))

    # Set the layout of the chart
    fig.update_layout(
        barmode='stack',  # Stacked bar chart
        title='Evolution of Plan Distribution Over Time Among Winners',
        xaxis_title='Date',
        yaxis_title='Percentage',
        xaxis=dict(tickangle=-45),  # Rotate x-axis labels for readability
    )

    st.plotly_chart(fig, use_container_width=True)