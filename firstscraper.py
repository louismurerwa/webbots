from urllib.request import urlopen as uRep

from bs4 import BeautifulSoup as soup

my_url = 'https://www.ebay.com/b/Apple-iPhone-X/9355/bn_86757102'

uClient = uRep(my_url)

#opening file
page_html=uClient.read()

 #close file

uClient.close()

#html parser
page_soup=soup(page_html,"html.parser")

#find specic class
containers = page_soup.findAll("div",{"class":"b-info"})
filename ="products.csv"
headers = "productname,productprice,pshipping\n"
f.write(" ")


for container in containers:
	
	name = container.findAll("div",{"class":"b-info__title"})
	productname = name[0].text.strip()
	price = container.findAll("span",{"class":"b-info__trendprice"})
	productprice = price[0].text.strip()
		
	
	
	
	pshipping = container.findAll("div",{"class":"b-info__iteminfo"})
	pshipping= pshipping[0].text.strip()

	print("brand: "+productname)
	print("price"+productprice)
	print("pshipping"+pshipping)
	f.write(productname.replace(",","|")+","+productprice.replace(",","|")+","+pshipping.replace(",","|"))

