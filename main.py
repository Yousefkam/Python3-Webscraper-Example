import pandas as pd #importing the pandas library which we will be using to 
import requests #importing requests library which we will use to do GET HTTP requests to the weather site.
from bs4 import BeautifulSoup #importing BeautifulSoup lib which we will use to parse GET request into HTML 5

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.X9kT39gzaUk') #Doing get request to the NYC Weather Forecast
soup = BeautifulSoup(page.content, 'html.parser') #Parsing the data from the request into HTML
week = soup.find(id='seven-day-forecast-body') #Locating the Forecast div in the page

items = week.find_all(class_='tombstone-container') #More locating... 

name = [item.find(class_='period-name').get_text() for item in items] #Here we log the period name in each forecasting period
desc = [item.find(class_='short-desc').get_text() for item in items] #Logging the period's description
temp = [item.find(class_='temp').get_text() for item in items] #Logging Temperatures

weather_stuff = pd.DataFrame(
    {'period': name,
    'short-descs': desc,
    "temps": temp},
) #Putting everything we scraped into a Pandas DataFrame


weather_stuff.to_csv('weather_stats.csv') #Pushing the dataframe into a CSV file