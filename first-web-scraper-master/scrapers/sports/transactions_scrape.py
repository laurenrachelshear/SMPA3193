import csv
from BeautifulSoup import BeautifulSoup
import urllib

r = urllib.urlopen('http://m.nationals.mlb.com/roster/transactions/2017/03').read()
soup = BeautifulSoup(r)
print type(soup)

print soup.prettify()[0:1000]

outfile = open("transactions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["date", "url", "text"])
writer.writerows(list_of_rows)
