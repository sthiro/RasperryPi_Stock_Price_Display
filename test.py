alerts = []
CurrentDemoPrice = 113

def SetAlert(Ticker,Price,Condition):
    alerts.append([Ticker,Price,Condition])

SetAlert(0,103,"Crossing Up")
SetAlert(0, 123, "Crossing Up")


def Alert():
    for alert in alerts:

        if (alert[1] <= CurrentDemoPrice) and (alert[2] == "Crossing Down"):  #Corssing Down
            print("Alert Crossing Down")

        if (alert[1] >= CurrentDemoPrice) and (alert[2] == "Crossing Up"):
            print("Alert Crossing Up")

Alert()