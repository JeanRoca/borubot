import discord
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import config
client = discord.Client()

my_url = "https://www.watchcartoononline.io/anime/boruto-naruto-next-generations-english-subbed"


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content == "!boruto":
        await client.send_message(message.channel, last_episode())

    # If the string starts with !boruto and does not contain only letters
    if "!boruto " in message.content and not str(message.content).isalpha():
        await client.send_message(message.channel, specific_episode(int(''.join(filter(str.isdigit, message.content)))))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


def last_episode():
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

    msg = (latest_episode + "\n" + latest_link)
    return msg


def specific_episode(num):
    uClient = uReq(my_url)
    page_html = uClient.read()


    # close connection after we have read information
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")

    # grabs all of the Boruto episodes
    containers = page_soup.findAll("a", {"class": "sonra"})

    if num > len(containers):
        return "There are only " + str(len(containers)) + " episodes currently"

    else:
        number = len(containers) - num
        # grab the title from the newest episode indexed at 0
        episode = containers[number].text

        # grab the latest link
        link = str(str(containers[number]).split("href=", )[1]).split("rel=")[0].replace('"', "").strip()

        msg = (episode + "\n" + link)
        return msg


client.run(config.token)
