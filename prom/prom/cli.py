import click
import requests
from PIL import Image
from StringIO import StringIO
from bs4 import BeautifulSoup

@click.command()
@click.argument('name', required=False)
def main(name):
    	URL='https://www.buriramunited.com/team'
	html=requests.get(URL)
	b=BeautifulSoup(html.content,'html.parser')
	search=b.find_all('div',{'class','img-box'})
	for x in range(len(search)):
		
		people=search[x].img['alt']
		print(people)
		if name==people:
			url=search[x].img['src']
			break
		
	req=requests.get(url)
    	img = Image.open(StringIO(req.content))
    	img.show()
