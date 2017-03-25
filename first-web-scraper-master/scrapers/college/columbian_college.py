import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://columbian.gwu.edu/2010-2011'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
    	list_of_cells.append(cell.text.encode('utf-8').strip())
    list_of_rows.append(list_of_cells)

outfile = open("2010-11.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["department", "faculty", "sponsor", "title"])
writer.writerows(list_of_rows)
