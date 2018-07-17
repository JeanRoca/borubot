import discord
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
client = discord.Client()

my_url = "https://www.watchcartoononline.io/anime/boruto-naruto-next-generations-english-subbed"
uClient = uReq(my_url)
page_html = uClient.read()

# close connection after we have read information
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs all of the Boruto episodes
containers = page_soup.findAll("a", {"class": "sonra"})

# grab the title from the newest episode indexed at 0
latest_episode = containers[0].text

# grab the latest link
latest_link = str(str(containers).split("href=", )[1]).split("rel=")[0].replace('"', "").strip()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!boruto'):
        msg = (latest_episode + "                       " + latest_link).format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('token')