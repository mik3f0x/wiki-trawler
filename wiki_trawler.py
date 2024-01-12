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
csv_writer.writerow(["Link Title", "Link URL"])

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
            # this doesn't seem to actually work; it just returns the same url, not the redirect
            # line_response = requests.get(article_url)
            # true_url = line_response.url

            # if true_url != article_url:
            #     print(f"found redirect for {title}: {article_url} -> {true_url}")
            
            # Write the extracted information to the CSV file
            csv_writer.writerow([title, article_url])

            # print(f"Writing line {count}")
            
print(f"Finished writing {count} entries")

# Close the CSV file
csv_file.close()


# 1. Read CSV
df = pd.read_csv("wiki_rappers.csv")

print(f"{df.duplicated().sum()} duplicates found:")
print(df[df.duplicated()])

# 2(a). For complete row duplicate
df.drop_duplicates(inplace=True)
print(f"Removing duplicates\n{df.duplicated().sum()} duplicates remaining")
            
# 2(b). For partials
title_dups = df[df.duplicated(subset=["Link Title"], keep=False)]
url_dups = df[df.duplicated(subset=["Link URL"], keep=False)]
print(f"Link Title duplicates:\n{title_dups}\nLink URL duplicates:\n{url_dups}")

# 3. Save then
df.to_csv("wiki_rappers.csv", index=False)

deduped_file = open('wiki_rappers.csv', 'r', encoding='utf-8')
row_count = sum(1 for row in deduped_file)
print(f"{row_count} rows in final file")
deduped_file.close()
