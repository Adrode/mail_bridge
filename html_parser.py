from bs4 import BeautifulSoup

def parse_html(html):
  soup = BeautifulSoup(html, "html.parser")

  with open("html_result.txt", "w", encoding="UTF-8") as f:
    f.write(html)