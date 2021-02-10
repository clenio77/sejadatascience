import pandas as pd
import streamlit as st
import plotly.express as px



st.title('house Rocket Company')

st.markdown('Welcome to House Rocket Data Analytics')

st.header('Load data')

#read data
@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    data['date'] = pd.to_datetime(data['date'])
    return data



# load data
data = get_data('./datasets/kc_house_data.csv')


# plot map
st.sidebar.subheader('House Rocket Map')
is_check = st.sidebar.checkbox('Display Map')

# filters
price_min = int(data['price'].min())
price_max = int(data['price'].max())
price_avg = int(data['price'].mean())

price_slider = st.sidebar.slider('Price Range',
                         price_min,
                         price_max,
                         price_avg)

if is_check:
    # select rows
    houses = data[data['price'] < price_slider][['id','lat','long','price']]
    st.dataframe(houses)

    # draw map
    fig = px.scatter_mapbox(
        houses,
        lat='lat',
        lon='long',
        size='price',
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=15,
        zoom=10
    )
    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=600, margin={'r': 0, 't': 0, 'l': 0, 'b': 2})
    st.plotly_chart(fig)
