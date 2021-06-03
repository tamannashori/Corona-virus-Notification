from plyer import notification
import json
import requests
#from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="D:\covidNotify\iconc.ico",
        timeout=6
    )


def getData(url):
    r = requests.get(url).json()
    #content = r.text
    return r



if __name__ == "__main__":
    while True:    
        myHtmlData = getData('https://www.mohfw.gov.in/data/datanew.json')
        states=['Uttar Pradesh','Chandigarh','Maharashtra']
        stData=[]
        List=[]
        for d in myHtmlData:
            #print('{:<30} {:<10} {:<10} {:<10} {:<10}'.format(d['state_name'], d['active'], d['positive'], d['cured'], d['death']))
            stData=[d['state_name'], d['active'], d['positive'], d['cured'], d['death']]
            if stData[0] in states:
                #print(stData)
                nTitle = 'Cases of Covid-19'
                nText = f"State: {stData[0]}\nActive : {stData[1]} & Positive : {stData[2]}\nCured :  {stData[3]}\nDeaths :  {stData[4]}"
                notifyMe(nTitle, nText)
                time.sleep(8)
        time.sleep(60)