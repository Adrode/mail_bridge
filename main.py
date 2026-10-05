from bs4 import BeautifulSoup

with open("test.html") as file:
  html = file.read()

soup = BeautifulSoup(html, "html.parser")

