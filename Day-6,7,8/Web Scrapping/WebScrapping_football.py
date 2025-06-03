from bs4 import BeautifulSoup

# Example: Assume you have an HTML file or content as a string
# For this code, read the HTML content from a file
with open('index1.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'lxml')

# Locate the table in the HTML
table = soup.find('table')

# Extract table headers
headers = [th.text.strip() for th in table.find_all('th')]

# Extract table rows
rows = []
for tr in table.find_all('tr')[1:]:  # Skip the header row
    cells = [td.text.strip() for td in tr.find_all('td')]
    if cells:
        rows.append(cells)

# Print the extracted data
print("Headers:", headers)
print("Rows:")
for row in rows:
    print(row)

# Optional: Convert data to a list of dictionaries
data_list = [dict(zip(headers, row)) for row in rows]

print("\nData as dictionaries:")
for item in data_list:
    print(item)
