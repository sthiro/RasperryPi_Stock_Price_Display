import yfinance as yf
import pandas as pd
import time

while True:
    ################################ Apple ################################


    # Define the tickers for the stocks you want to fetch
    tickers_Apple = ['AAPL']

    # Fetch the stock data
    data_Apple = yf.download(tickers_Apple, period='1d', interval='1m', group_by='ticker')

    df_Apple = pd.DataFrame(data_Apple)

    # Get the last row's "Adj Close" value
    last_adj_close_Apple = df_Apple['Adj Close'].iloc[-1]

    # Convert DataFrame to Excel file
    df_Apple.to_excel('Apple_Stock_Price.xlsx', index=False)

    print("Apple    : " + str(last_adj_close_Apple))


    ################################ Apple ################################

    ################################ AMD ################################


    # Define the tickers for the stocks you want to fetch
    tickers_AMD= ['AMD']

    # Fetch the stock data
    data_AMD = yf.download(tickers_AMD, period='1d', interval='1m', group_by='ticker')

    df_AMD = pd.DataFrame(data_AMD)

    # Get the last row's "Adj Close" value
    last_adj_close_AMD = df_AMD['Adj Close'].iloc[-1]

    # Convert DataFrame to Excel file
    df_AMD.to_excel('AMD_Stock_Price.xlsx', index=False)

    print("AMD  :" + str(last_adj_close_AMD))


    ################################ AMD ################################

    ################################ Microsoft ################################


    # Define the tickers for the stocks you want to fetch
    tickers_MSFT = ['MSFT']

    # Fetch the stock data
    data_MSFT = yf.download(tickers_MSFT, period='1d', interval='1m', group_by='ticker')

    df_MSFT = pd.DataFrame(data_MSFT)

    # Get the last row's "Adj Close" value
    last_adj_close_MSFT = df_MSFT['Adj Close'].iloc[-1]

    # Convert DataFrame to Excel file
    df_MSFT.to_excel('Microsoft_Stock_Price.xlsx', index=False)

    print("MSFT  :" + str(last_adj_close_MSFT))

    ################################ Microsoft ################################

    time.sleep(2)
    print("---------------------------------------------  2 Sec --------------------------------------------- ")
