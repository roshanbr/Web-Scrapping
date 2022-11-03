import requests
import bs4 
r = requests.get('https://stackoverflow.com/questions/tagged/python/')

soup = bs4.BeautifulSoup(r.text, 'lxml')
question=soup.select('.s-post-summary--content-title')


for i in soup.select('.s-post-summary--content-title'):
    {
        print(i.text)
    }