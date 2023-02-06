import yfinance as yf
import streamlit as st

import pandas as pd 

st.write("""
# Simple Stock Price Data App

Shown are the stock closing price and volume of Google!

""")

#Define the ticker symbol
tickerSymbol = "GOOGL"


#Get the data of this ticker
tickerData = yf.Ticker(tickerSymbol)

#Get the historical price for this ticker
tickerDf = tickerData.history(period='1d',start = '2010-5-31',end='2020-5-31')


#Line charts for Close price and Volume price
st.write("""  Closing price """)
st.line_chart(tickerDf.Close)
st.write("""  Volume price """)
st.line_chart(tickerDf.Volume)
