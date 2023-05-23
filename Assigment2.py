import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.graph_objs as go
import streamlit as st
import streamlit.components.v1 as components

# Read the data
data = pd.read_csv('assign2_wastedata.csv')
pivot_table = data.pivot_table(index='Date', columns='Substream', values='Volume', aggfunc='sum')

# Group the data by Substream and calculate the total volume for each substream
grouped_data = data.groupby('Substream')['Volume'].sum().reset_index()

# Group the data by Stream and calculate the total volume for each stream
grouped_data_stream = data.groupby(['Building', 'Stream']).sum()['Volume'].reset_index()

# Create the interactive treemap using Plotly Express
fig_treemap = px.treemap(
    grouped_data_stream,
    path=['Building', 'Stream'],
    values='Volume',
    # color='Volume',
    # color_continuous_scale='colors',
    title='Waste Stream Distribution'
)

# # Create the interactive heat map using Plotly
# fig_heatmap = go.Figure(data=go.Heatmap(
#     z=pivot_table.values,
#     x=pivot_table.columns,
#     y=pivot_table.index,
#     colorscale='Viridis'))

# # Customize the layout
# fig_heatmap.update_layout(
#     title='Waste Volume Heatmap',
#     xaxis_title='Substream',
#     yaxis_title='Date')

st.set_page_config(layout="wide")

# Header and title
st.title('Waste Analysis')

# Display Tree map 
st.header('Interactive Treemap')
st.plotly_chart(fig_treemap)

# # Display heat map 
# st.header('Interactive Heat Map')
# st.plotly_chart(fig_heatmap)
