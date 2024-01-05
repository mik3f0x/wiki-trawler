# Based on rapper_trawler_0.py in naming project
import requests
from bs4 import BeautifulSoup
import csv

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_hip_hop_musicians'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Open the CSV file for writing
csv_file = open('wiki_rappers.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

# Find all hyperlinks in the HTML source
list_divs = soup.find_all('div', class_='div-col')

count = 0

for div in list_divs:
    for link in div.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/wiki/'):
            # Extract the article title
            title = link.text.strip()

            count += 1

            # Get the URL of the article
            article_url = f"https://en.wikipedia.org{href}"

            # Process the article URL and extract relevant information
            # ... (your code here)
            
            # Write the extracted information to the CSV file
            csv_writer.writerow([title, article_url])
            
print(count)

# Close the CSV file
csv_file.close()
