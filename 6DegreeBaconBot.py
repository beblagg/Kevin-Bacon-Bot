from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
from random import randint

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Set up our variables / dictionaries
count = 0
linkdct = {}
titledct = {}

# Begin with our starting URL of Kevin Bacon's wiki page
url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'

def get_info(url):
    global count
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    # Look through the hyperlinks within the paragraph tags of the page and create a numbered dictionary of them
    all_links = soup.select('p a[href]')
    for links in all_links:
        if (re.match(r'^/wiki.*', str(links.get('href', None)))) == None:
            continue
        hlink = 'https://en.wikipedia.org'+links.get('href', None)
        title = links.get('title', None)
        count = count + 1
        linkdct[count] = hlink
        titledct[count] = title

n=1
while n<7:
    count = 0
    linkdct = {}
    titledct = {}
    get_info(url)
    randnum = randint(1,count)
    print(n,'->',titledct[randnum], '(Link', str(randnum)+'/'+str(count)+')')
    url = linkdct[randnum]
    n=n+1

print(url)
