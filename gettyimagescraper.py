import requests
from bs4 import BeautifulSoup as bs
import os

#url with pictures
my_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTriDXmnDzRrA8mYmm6ZFb-97EkTITSMWwuuukDUOYhuaiPzEcgV_NaN0efyADZ2RYm_xA-kjw_eTFN/pubhtml'

#down load page
page=requests.get(my_url)
soup = bs(page.text,'html.parser')

#find specic class of imgs

image_tags = soup.findAll('tr')

#create a directory for images
if not os.path.exists('models'):
	os.makedirs('models')

#move to new directory
os.chdir('models')

#image file name variable
x=0

#writing the images
for image in image_tags:
	try:
		url = image['src']
		source = requests.get(url)
		if source.status_code == 200:
			with open('model'+str(x)+'.jpg','wb') as f:
				f.write(requests.get(url).content)
				f.close()
				x=x+1
	except:
		pass
