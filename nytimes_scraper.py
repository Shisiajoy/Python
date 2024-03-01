import requests
from bs4 import BeautifulSoup
import csv

# Defining the URL of The New York Times front page
url = 'https://www.nytimes.com/section/todayspaper'

# Send a GET request to the website
response = requests.get(url)
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
# Find the articles on the front page
articles = soup.find_all('article')
# Initialize an empty list to store article data
data = []
# Extract titles and descriptions from the articles
for article in articles[:10]:
    try:
        title = article.find('h2').text.strip()
    except AttributeError:
        title = 'No title found'
    description = article.find('p').text.strip()
    data.append({'title': title, 'description': description})

# Write the data to a CSV file
with open('nytimes.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'description'])
    writer.writeheader()
    writer.writerows(data)


#tried running the code you provided on slack but it wasnt giving an output
#so i made some changes to the url and used try except to catch errors,but in the cvs filemit prints the error message 'no tittle file' in place of tittle
