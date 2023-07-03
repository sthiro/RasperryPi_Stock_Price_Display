import yfinance as yf
import pandas as pd
import time
import drivers

display = drivers.Lcd()

tickers = ['aapl', 'amd', "msft" ] # 0 - Apple , 1 - AMD, 2 - Microsoft
NameStocks = ['Apple', "AMD", "Microsoft"]
CurrentDemoPrice = 113
alerts = []

def fetchPrice(ticker_no): # Fetching Price
    data = yf.Ticker(tickers[ticker_no])
    return data.info['currentPrice']

def sendToDisplay(Index,Price):    #Displaying price on LCD
    # Remember that your sentences can only be 16 characters long!
    try:
        print("Writing to display")
        display.lcd_display_string(f"{NameStocks[Index]}    : {Price} $",0)  # Write line of text to first line of display
        display.lcd_display_string("By - S.Thiroshan",0)  # Write line of text to first line of display

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

index = 0

while True:
    time.sleep(5)
    if index == 3: index = 0
    print("Microsoft Price  :" + str(fetchPrice(2))) # Apple Price
    sendToDisplay(index,str(fetchPrice(index)))
    index = index + 1




   


 