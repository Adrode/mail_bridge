from bs4 import BeautifulSoup

with open("test.html", encoding="UTF-8") as file:
  html = file.read()

soup = BeautifulSoup(html, "html.parser")

def get_basic_claim_data(soup, element):
  return soup.find("label", string=element).parent.parent

def get_basic_claim_value(soup, val):
  element = get_basic_claim_data(soup, val)
  return element.select_one(".col-value .field-wrapper .form-control").get_text(strip=True)

def get_user_data(soup, element):
  return soup.find("label", string=element).parent

def get_user_value(soup, val):
  element = get_user_data(soup, val)
  return element.select_one(".input-wrapper .form-control").get_text(strip=True)

def get_car_data(soup, element):
  return soup.find("span", string=element).parent.parent

def get_car_value(soup, val):
  element = get_car_data(soup, val)
  return element.select_one(".vehicle-value").get_text(strip=True)

def get_car_identification_value(soup, element):
  return soup.find("span", {"class": element}).get_text(strip=True)

def get_claim_event_data(soup, element):
  return soup.find("td", string=lambda text: text and text.strip() == element).parent

def get_claim_event_value(soup, val):
  element = get_claim_event_data(soup, val)
  return element.select_one(".value-cell").get_text(strip=True)

claim = {
  "Numer szkody": get_basic_claim_value(soup, "Numer szkody:"),
  "Data zgłoszenia": get_basic_claim_value(soup, "Data zgłoszenia:"),
  "Status": get_basic_claim_data(soup, "Status:").select_one(".col-value .field-wrapper .status").get_text(strip=True),
  "Imię i nazwisko": get_user_value(soup, "Imię i nazwisko"),
  "Email": get_user_value(soup, "Adres e-mail"),
  "Numer telefonu": get_user_value(soup, "Telefon"),
  "Marka pojazdu": get_car_value(soup, "Marka:"),
  "Model pojazdu": get_car_value(soup, "Model:"),
  "Numer rejestracyjny": get_car_identification_value(soup, "registration-number"),
  "VIN": get_car_identification_value(soup, "vin"),
  "Data zdarzenia": get_claim_event_value(soup, "Data zdarzenia"),
  "Miejsce zdarzenia": get_claim_event_value(soup, "Miejsce zdarzenia"),
  "Rodzaj zdarzenia": get_claim_event_value(soup, "Rodzaj zdarzenia")
}

print(claim)
