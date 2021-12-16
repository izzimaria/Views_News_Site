from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome("C:/Users/maria/Desktop/chromedriver.exe",ChromeDriverManager().install(), chrome_options=chrome_options)
driver=webdriver.Chrome("C:/Users/maria/Desktop/chromedriver.exe")

# Query to obtain links
query = 'argentina'
links = [] # Initiate empty list to capture final results
# Specify number of pages on google search, each page contains 10 #links

url = "http://www.google.com/search?q=" + query
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# soup = BeautifulSoup(r.text, 'html.parser')

search = soup.find_all('div', class_="yuRUbf")
for h in search:
    links.append(h.a.get('href'))
        
print(links[:3])