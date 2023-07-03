import yfinance as yf
import pandas as pd
import time
import drivers

display = drivers.Lcd()

tickers = ['aapl', 'amd', "msft" ] # 0 - Apple , 1 - AMD, 2 - Microsoft
CurrentDemoPrice = 113
alerts = []

def fetchPrice(ticker_no): # Fetching Price
    data = yf.Ticker(tickers[ticker_no])
    return data.info['currentPrice']

def sendToDisplay(Price1, Price2, Price3):    #Displaying price on LCD
    # Remember that your sentences can only be 16 characters long!
    try:
        print("Writing to display")
        display.lcd_display_string("Greetings Human!", 1)  # Write line of text to first line of display

    except KeyboardInterrupt:
        # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        print("Cleaning up!")
        display.lcd_clear()

def setAlert(Ticker,Price,Condition):  #Setting up alert
    alerts.append([Ticker,Price,Condition])

def Alert():
    for alert in alerts:

        if (alert[1] <= CurrentDemoPrice) and (alert[2] == "Crossing Down"):  #Crossing Down
            print("Alert Crossing Down")

        if (alert[1] >= CurrentDemoPrice) and (alert[2] == "Crossing Up"):
            print("Alert Crossing Up")

while True:
    time.sleep(1)

    print("Microsoft Price  :" + str(fetchPrice(2))) # Apple Price
    sendToDisplay(fetchPrice(0),fetchPrice(1),fetchPrice(2))
    Alert()




   


 