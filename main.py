from bs4 import BeautifulSoup

with open("test.html", encoding="UTF-8") as file:
  html = file.read()

soup = BeautifulSoup(html, "html.parser")

claim_number_label_parent = soup.find("label", string="Numer szkody:").parent.parent
claim_date_label_parent = soup.find("label", string="Data zgłoszenia:").parent.parent
claim_status_label_parent = soup.find("label", string="Status:").parent.parent
claim_name_label_parent = soup.find("label", string="Imię i nazwisko").parent
claim_email_label_parent = soup.find("label", string="Adres e-mail").parent
claim_phone_label_parent = soup.find("label", string="Telefon").parent
claim_brand_span_parent = soup.find("span", string="Marka:").parent.parent
claim_model_span_parent = soup.find("span", string="Model:").parent.parent
claim_registration_span = soup.find("span", {"class": "registration-number"}).get_text(strip=True)
claim_VIN_span = soup.find("span", {"class": "vin"}).get_text(strip=True)
claim_event_date_td_parent = soup.find("td", string=lambda text: text and text.strip() == "Data zdarzenia").parent
claim_event_place_td_parent = soup.find("td", string=lambda text: text and text.strip() == "Miejsce zdarzenia").parent
claim_event_type_td_parent = soup.find("td", string=lambda text: text and text.strip() == "Rodzaj zdarzenia").parent


# print(claim_event_place_td_parent)

claim = {
  "Numer szkody": claim_number_label_parent.select_one(".col-value .field-wrapper .form-control").get_text(strip=True),
  "Data zgłoszenia": claim_date_label_parent.select_one(".col-value .field-wrapper .form-control").get_text(strip=True),
  "Status": claim_status_label_parent.select_one(".col-value .field-wrapper .status").get_text(strip=True),
  "Imię i nazwisko": claim_name_label_parent.select_one(".input-wrapper .form-control").get_text(strip=True),
  "Email": claim_email_label_parent.select_one(".input-wrapper .form-control").get_text(strip=True),
  "Numer telefonu": claim_phone_label_parent.select_one(".input-wrapper .form-control").get_text(strip=True),
  "Marka pojazdu": claim_brand_span_parent.select_one(".vehicle-value").get_text(strip=True),
  "Model pojazdu": claim_model_span_parent.select_one(".vehicle-value").get_text(strip=True),
  "Numer rejestracyjny": claim_registration_span,
  "VIN": claim_VIN_span,
  "Data zdarzenia": claim_event_date_td_parent.select_one(".value-cell").get_text(strip=True),
  "Miejsce zdarzenia": claim_event_place_td_parent.select_one(".value-cell").get_text(strip=True),
  "Rodzaj zdarzenia": claim_event_type_td_parent.select_one(".value-cell").get_text(strip=True)
}

print(claim)
