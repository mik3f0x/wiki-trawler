# Based on rapper_trawler_0.py in naming project
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

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


# 1. Read CSV
df = pd.read_csv("wiki_rappers.csv")

print(df.duplicated().sum())

# 2(a). For complete row duplicate
df.drop_duplicates(inplace=True)
             
# 2(b). For partials
# pd.drop_duplicates(subset=['Date', 'Time', <other_fields>], inplace=True)

print(df.duplicated().sum())

# 3. Save then
df.to_csv("wiki_rappers.csv", index=False)

deduped_file = open('wiki_rappers.csv', 'r', encoding='utf-8')
row_count = sum(1 for row in deduped_file)
print(row_count)
deduped_file.close()
