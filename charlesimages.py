from charlesmap import *


html_doc = open('CharlesRiverCrossings.html', 'r')
soup = BeautifulSoup(html_doc, 'html.parser')
if __name__ == '__main__':
	print(soup.prettify())