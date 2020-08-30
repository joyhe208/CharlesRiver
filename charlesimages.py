from charlesmap import *


html_doc = open('CharlesRiverCrossings.html', 'r')
soup = BeautifulSoup(html_doc, 'html.parser')
table = soup.table	
table_rows = table.find_all('tr')
table_rows.remove(table_rows[4])
table_rows.remove(table_rows[0])
	# for i in range(len(lats)):
	# 	print(i)
	# 	dividers = table_rows[i].find_all('td')
	# 	if len(dividers[len(dividers)-1].find_all('img', limit = 1))!=0:
	# 		image = str(dividers[len(dividers)-1].find('img').get('src'))
	# 		image = image.replace("/thumb", "")
	# 		try:
	# 			image = image.split(".jpg")[0]
	# 			image = "https:" + image + ".jpg"
	# 		except:
	# 			image = image.split("/400px")[0]
	# 			image = "https:" + image 

	# 		dl_img(image, "pic" + str(i))

	