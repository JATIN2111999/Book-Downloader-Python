import requests
from bs4 import BeautifulSoup
import pprint

bookname="hello"
urllink="http://libgen.is/search.php?req="+bookname+"&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"
def urls(url):
    page=requests.get(url)    
    soup=BeautifulSoup(page.text,'html.parser')
    return soup

soup=urls(urllink)
xyz=soup.find_all('table')
soup=xyz[2]
trs=soup.find_all('tr')

i=int(input('enter the value of i'))
tr=trs[i]
download=tr.find_all('td')[9].a.get("href")
print(download)

finalsoup=urls(download)
if finalsoup.find_all('td')[1].a.text == 'GET':
    final=finalsoup.find_all('td')[1].a.get('href')
    pp=pprint.PrettyPrinter(indent=4)
    pp.pprint(final)
else:
    print("can't find nibba or something went wrong")