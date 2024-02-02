import requests
from bs4 import BeautifulSoup
import pandas as pd 

# URL of the New York Times page containing the articles
url = 'https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html'

# Send get request to url

response = requests.get(url)

# Check for the successful record
if response.status_code == 200:
    # Parse the html content using BeautifulSoup

    soup = BeautifulSoup(response.text,'html.parser')

    # Create the lists for items to be extracted
    Dates = []
    lies = []
    Explanation = []
    url = []
    # Extract date to work on
    data = soup.find_all('span',class_ = 'short-desc')

    for article in data:
        # Extract dates
        Dates.append(article.text.strip().split('\xa0')[0])
        # Extract Lies
        lies.append(article.text.strip().split('\xa0')[1].split('(')[0].replace('“', '').replace('”', ''))
        # Extract Explanations
        Explanation.append(article.text.strip().split('\xa0')[1].split('”')[1].replace('(','').replace(')',''))
        # Extract URL
        url.append(article.find('a')['href'])

    # Makeing Tabular structure of data
    Dataset = pd.DataFrame({'Dates':Dates,'Lies':lies,'Explanations':Explanation,'URL':url})

    # Exporting data to a csv file
    Dataset.to_csv('NewYork Times Articles.csv')
    print("Dataset successfully created and exported to : ('NewYork Times Articles.csv')")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")