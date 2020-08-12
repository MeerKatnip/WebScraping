import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.XzQM9RNKgnU')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
# print(week)

items = week.find_all(class_ = 'tombstone-container')
print(items[0])
