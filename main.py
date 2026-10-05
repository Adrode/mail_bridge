from bs4 import BeautifulSoup

with open("test.html", encoding="UTF-8") as file:
  html = file.read()

soup = BeautifulSoup(html, "html.parser")

claim_number_label_parent = soup.find("label", string="Numer szkody:").parent.parent
claim_date_label_parent = soup.find("label", string=lambda text: text and "Data zgłoszenia:" in text).parent.parent

claim = {
  "Numer szkody": claim_number_label_parent.select_one(".col-value .field-wrapper .form-control").get_text(strip=True),
  "Data zgłoszenia": claim_date_label_parent.select_one(".col-value .field-wrapper .form-control").get_text(strip=True),
}

print(claim)

  # 'Data zgĹ‚oszenia:'

# Data zgłoszenia
# Status
# Imię i nazwisko
# E-mail
# Telefon
# Marka
# Model
# Rejestracja
# VIN
# Data zdarzenia
# Miejsce zdarzenia
# Rodzaj zdarzenia