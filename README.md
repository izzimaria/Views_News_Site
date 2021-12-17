# Views News Site

This is a website that will send subscribers a daily email with three news sources regarding one country in each major world region. It is intended to broaden perspectives by informing users about world news outside of the US and Canada. This website was developed using Node.js, Express, HTML/CSS and Bootstrap, and web scraping via BeautifulSoup and Selenium in Python.

When a user signs up, the website will add their name to a CSV file of all the subscribers. Then, when the script to send the email is called, the news email is sent to all the emails, pulled from the CSV. This script uses BeautifulSoup to scrape the top three links on Google about the selected countries' news today. One country is randomly chosen out of the following six regions: East Asia, Europe and Central Asia, Latin America, Middle East and North Africa, South Asia, and Sub-Saharan Africa.

Here is an example of what the email looks like:

<img width="714" alt="image" src="https://user-images.githubusercontent.com/32143977/146469196-1e5290da-288d-483c-b843-924194108ebc.png"> 
<img width="715" alt="image" src="https://user-images.githubusercontent.com/32143977/146469162-f9ffc4ea-3034-457f-ac0f-e617d8c94f7b.png">

The entire website is fully functional locally, but signing up for the newsletter is not yet functional online. The website can be viewed here: https://views-news-site.herokuapp.com/.
