from bs4 import BeautifulSoup




with open("test.html", "r")as f:
    html = f.read()


soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())