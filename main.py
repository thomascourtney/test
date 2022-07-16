import pandas_datareader
import streamlit as st
from sklearn import datasets
import tensorflow as tf
import pandas_datareader as web
from pandas_datareader import data,wb
import matplotlib as plt
from matplotlib import style
import datetime as dt
import pandas as pd
import numpy as np
import yfinance as yf
from plotly import graph_objs as go
from darts import TimeSeries
 


st.title("Streamstrelit Example")

st.write("""
Explore different stocks
""")
stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
dataset_name = st.selectbox("Select Stock", stocks)

START = "2015-01-01"
TODAY = "2020-01-01"

@st.cache
def load_data(ticker):
    df = yf.download(ticker, START, TODAY)
    df.reset_index(inplace=True)
    return df
    


data_load_state = st.text('Loading data...')
data = load_data(stocks)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())

def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)


plot_raw_data()