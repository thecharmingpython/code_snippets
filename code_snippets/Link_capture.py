# Use Requests and Beautiful supo to find all links on a page

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
#ensure the URL has http or https
if ("https" or "http") in url:
    response = requests.get(url)
else:
    response = requests.get("https://" + url)

soup = BeautifulSoup(response.text, "html.parser")
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Output to a file (myLinks.txt) instead of to stdout
# You can change 'a' to 'w' to overwrite the file each time
with open("links.txt", 'a') as f:
    print(links[:10], file=f)