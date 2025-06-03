from bs4 import BeautifulSoup

with open('ws2.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

for row in rows[1:]:
    cols = row.find_all('td')
    data = [col.text.strip() for col in cols]
    print(data)
