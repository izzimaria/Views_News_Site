import smtplib, ssl
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import random

# function to scrape news links from Google and write email message
def getNews():
    driver=webdriver.Chrome("chromedriver.exe")
    
    # create dictionary to map each region to the list of country options
    queries = {'East Asia':['China','Indonesia','Japan','Philippines','Vietnam',
              'Thailand','Myanmar','South Korea','Malaysia','North Korea'],
               
    'Europe and Central Asia':['Russia','Turkey','Germany','France','United Kingdom',
                 'Italy','Spain','Ukraine','Poland','Uzbekistan'],
    
    'Latin America':['Brazil','Mexico','Colombia','Argentina','Peru',
                'Venezuela','Chile','Ecuador','Guatemala','Bolivia'],
    
    'Middle East and North Africa':['Egypt','Iran','Algeria','Iraq','Morocco',
            'Saudi Arabia','Yemen','Syria','Tunisia','Jordan'],
    
    'South Asia':['India','Pakistan','Bangladesh','Afghanistan','Nepal',
              'Sri Lanka','Bhutan','Maldives'],
    
    'Sub-Saharan Africa':['Nigeria','Ethiopia','DR Congo','Tanzania','South Africa',
                  'Kenya','Uganda','Sudan','Angola','Mozambique']}
    
    results = {}
    for region in queries:
        # select a random country from each region
        rand = random.randint(0,len(queries[region])-1)
        country = queries[region][rand]
        # scrape the Google search links for the country's news today
        url = "http://www.google.com/search?q=" + country + " news today"
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search = soup.find_all('div', class_="yuRUbf")
        results[country] = []
        
        # add top three links to results
        for link in search[:3]:
            results[country].append(link.a.get('href'))
    
    # create message to send
    message = ""
    message = message+"""Subject: Today's Views News\nHello!\n"""

    # add links to message
    index = 0
    for region in queries:
        country = list(results.keys())[index]
        message += "Today's country from the region "+region+" is "+country+".\n"
        message += "Here's the first link: "+results[country][0]+"\n"
        message += "Here's the second link: "+results[country][1]+"\n"
        message += "Here's the third link: "+results[country][2]+"\n\n"
        index += 1

    message += "Thanks for subscribing, and see you tomorrow!"
    
    return message

# function to send email
# With help from: https://realpython.com/python-send-email/
def sendEmail(message,data):
    df = data
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    email = "views.daily.emails@gmail.com"
    subscribers = df['email']
    # password = input("Type your password and press enter: ")
    password = "whatifb4dawhy--"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, subscribers, message)


if __name__=="__main__":
    df = pd.read_csv("subscribers.csv")
    message = getNews()
    sendEmail(message,df)
    print("Email successfully sent!")