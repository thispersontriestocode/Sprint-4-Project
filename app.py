import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')




st.header('Compare price distribution between fuel types')
# get a list of fuel types
fuel_list = sorted(df['fuel'].unique())
# get user's inputs from a dropdown menu
fuel_1 = st.selectbox(
                              label='Select fuel 1', 
                              options=fuel_list, 
                              index=fuel_list.index('gas')
                              )
fuel_2 = st.selectbox(
                              label='Select fuel 2',
                              options=fuel_list, 
                              index=fuel_list.index('diesel')
                              )
# filter the dataframe 
mask_filter = (df['fuel'] == fuel_1) | (df['fuel'] == fuel_2)
df_filtered = df[mask_filter]

# add a checkbox if a user wants to normalize the histogram
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

# create a plotly histogram figure
fig_price_fuel = px.histogram(df_filtered,
                      x='price',
                      nbins=30,
                      color='fuel',
                      histnorm=histnorm,
                      barmode='overlay')
# display the figure with streamlit
fig_price_fuel.show()
st.write(fig_price_fuel)