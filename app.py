import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')

st.header('Vehicle types by price')
#create a plotly histogram figure
fig_vt_by_p = px.histogram(df, x='price', color='type')
#display the figure with streamlit
fig_vt_by_p.show()
st.write(fig_vt_by_p)

st.header('Price Vs Odometer')
fig_odo_vs_p = px.scatter(df, x="odometer", y="price", 
                 labels={"odometer": "Odometer Reading (miles)", "price": "Price ($)"},
                 hover_data=["model", "model_year", "condition"])
#fig_odo_vs_p.show()
st.write(fig_odo_vs_p)

fig_transmission = px.histogram(df, x="transmission", 
                   title="Transmission Type Distribution",
                   labels={"transmission": "Transmission Type", "count": "Count"},
                   category_orders={"transmission": ["automatic", "manual"]})

fig_transmission.show()
st.write(fig_transmission)

st.header('Price Vs Odometer')
fig_odo_vs_year_vs_p = px.scatter(df, x="odometer", y="price", 
                 labels={"odometer": "Odometer Reading (miles)", "price": "Price ($)"},
                 hover_data=["model", "model_year", "condition"])
fig_odo_vs_year_vs_p.show()
st.write(fig_odo_vs_year_vs_p)

fig_fuel_type = px.histogram(df, x="fuel", 
                   title="Fuel Type Distribution",
                   labels={"fuel": "Fuel Type", "count": "Count"},
                   category_orders={"fuel": ["gas", "diesel"]})

fig_fuel_type.show()
st.write(fig_fuel_type)



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