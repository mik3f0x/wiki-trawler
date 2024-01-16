# Based on rapper_trawler_0.py in naming project
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json, csv
import time

start_time = time.time()

list_url = "https://en.wikipedia.org/wiki/List_of_hip_hop_musicians"
list_title = list_url[list_url.rindex("/wiki/")+6:]

response = requests.get(list_url)

soup = BeautifulSoup(response.content, 'html.parser')

# Open the CSV file for writing
csv_file = open(f"{list_title}.csv", 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Link Title", "Article Title", "Link URL", "Article URL"])


def get_final_url(title):
    url = f'https://en.wikipedia.org/w/api.php?action=query&titles={title}&redirects&format=json'
    response = requests.get(url)

    if "redirects" in json.loads(response.text)["query"]:
        final_title = json.loads(response.text)["query"]["redirects"][0]["to"]
        snake_title = final_title.replace(" ", "_")
    else:
        snake_title = title
        final_title = title.replace("_", " ")

    final_url = f"https://en.wikipedia.org/wiki/{snake_title}"
    redirect_dict = {"title": final_title, "final_url": final_url}

    return redirect_dict


list_divs = soup.find_all('div', class_='div-col')

count = 0
for div in list_divs:
    for link in div.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/wiki/'):
            title = link.text.strip()
            link_url = f"https://en.wikipedia.org{href}"

            delimiter = "#" if "#" in href else "/"
            snake_title = href[href.rindex(delimiter)+1:]

            redirect = get_final_url(snake_title)
            true_title = redirect["title"]
            true_url = redirect["final_url"]

            count += 1

            csv_writer.writerow([title, true_title, link_url, true_url])

            # if count % 1000 == 0 or count > 4000:
            #     print(f"Writing line {count}") # - {title}: {link_url}")

            # if true_url != link_url:
            #     print(f"Found redirect on line {count} for {title} -> {true_title}\n\t{link_url}\n\t-> {true_url}")
                      
print(f"Finished writing {count} entries")

csv_file.close()


# 1. Read CSV
df = pd.read_csv(f"{list_title}.csv")

print(f"{df.duplicated().sum()} exact duplicates found:")
print(df[df.duplicated()])

# 2(a). For complete row duplicate
df.drop_duplicates(inplace=True)
print(f"Removing exact duplicates\n{df.duplicated().sum()} duplicates remaining")
            
# 2(b). For partials
title_dups = df[df.duplicated(subset=["Article Title"], keep=False)]
print(f"Article Title duplicates:\n{title_dups}")

url_dups = df[df.duplicated(subset=["Article URL"], keep=False)]
print(f"Article URL duplicates:\n{url_dups}")

# 3. Save then
df.to_csv(f"{list_title}.csv", index=False)

deduped_file = open(f"{list_title}.csv", 'r', encoding='utf-8')
row_count = sum(1 for row in deduped_file)
print(f"{row_count} rows in final file")
deduped_file.close()


elapsed = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))
print(f"Total time elapsed: {elapsed}")