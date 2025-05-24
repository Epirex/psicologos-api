import requests
from bs4 import BeautifulSoup
import json

url = "https://psicologoscatamarca.com.ar/psicoweb/listado-de-profesionales-activos/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

data = []
for row in rows[1:]:
    cols = row.find_all('td')
    data.append({
        'M.P': cols[0].text.strip(),
        'nombre': cols[1].text.strip(),
        'domicilio_laboral': cols[2].text.strip(),
        'telefono': cols[3].text.strip(),
        'orientacion': cols[4].text.strip(),
        'clinica': cols[5].text.strip(),
        'domicilio': cols[6].text.strip(),
        'obra_social': cols[7].text.strip(),
    })

with open('psicologos.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
