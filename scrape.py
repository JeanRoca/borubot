import bs4
import discord
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# declare the url we would like to scrape from
# using watchcartoononline because it has the least ads
my_url = "https://www.watchcartoononline.io/anime/boruto-naruto-next-generations-english-subbed"

# open connection and grab page
uClient = uReq(my_url)
page_html = uClient.read()

# close connection after we have read information
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs all of the Boruto episodes
containers = page_soup.findAll("a",{"class":"sonra"})

# loops over all the Boruto episodes
for container in containers:
    # will give the episode title
    title = container.text
    print(title)

    # the link is contained in between href and rel. grab what is in the middle of that to get link
    hyper_link = str(str(container).split("href=",)[1]).split("rel=")[0].replace('"', "").strip()
    print(hyper_link)

# grab the title from the newest episode indexed at 0
latest_episode = containers[0].text

# grab the latest link
latest_link = str(str(containers).split("href=",)[1]).split("rel=")[0].replace('"', "").strip()

print(latest_episode)
print(latest_link)
