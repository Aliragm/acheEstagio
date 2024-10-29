from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from bs4 import BeautifulSoup
import pandas as pd
import time



def scroll_down(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

estados = {
    1: ['Acre', 'AC'],
    2: ['Alagoas', 'AL'],
    3: ['Amapá', 'AP'],
    4: ['Amazonas', 'AM'],
    5: ['Bahia', 'BA'],
    6: ['Ceará', 'CE'],
    7: ['Distrito Federal', 'DF'],
    8: ['Espírito Santo', 'ES'],
    9: ['Goiás', 'GO'],
    10: ['Maranhão', 'MA'],
    11: ['Mato Grosso', 'MT'],
    12: ['Mato Grosso do Sul', 'MS'],
    13: ['Minas Gerais', 'MG'],
    14: ['Pará', 'PA'],
    15: ['Paraíba', 'PB'],
    16: ['Paraná', 'PR'],
    17: ['Pernambuco', 'PE'],
    18: ['Piauí', 'PI'],
    19: ['Rio de Janeiro', 'RJ'],
    20: ['Rio Grande do Norte', 'RN'],
    21: ['Rio Grande do Sul', 'RS'],
    22: ['Rondônia', 'RO'],
    23: ['Roraima', 'RR'],
    24: ['Santa Catarina', 'SC'],
    25: ['São Paulo', 'SP'],
    26: ['Sergipe', 'SE'],
    27: ['Tocantins', 'TO']
}

title, link = [], []

##estagiotrainee
driver = webdriver.Safari()
driver.get("https://www.estagiotrainee.com/blog/categories/estágio")

scroll_down(driver)

soup = BeautifulSoup(driver.page_source, 'html.parser')
oportunities = soup.find_all('a', {'class':'O16KGI pu51Xe x_FPRX xs2MeC'})

print("Escolha o estado para buscar vagas de estágio:")
for numero, estado in estados.items():
    print(f"{numero}. {estado[0]} ({estado[1]})")

escolha = int(input("Digite o número do estado desejado: "))

if escolha in estados:
    param = estados[escolha]
    print(f"\nBuscando vagas para o estado: {param[0]} ({param[1]})")
else:
    print("Opção inválida.")



for oportunity in oportunities:
    driver.get(oportunity['href'])
    scroll_down(driver)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    requisites = soup.find_all('ul', {'class':'jnuVW mcSBi'})
    if any(p in requisite.text for requisite in requisites for p in param):            
        title.append(oportunity.text)
        link.append(oportunity['href'])

##remotar https://remotar.com.br/search/jobs?t=10 div class = featured

driver.get("https://remotar.com.br/search/jobs?t=10")
scroll_down(driver)

soup = BeautifulSoup(driver.page_source, 'html.parser')
oportunities = soup.find_all('div', {'class':'featured'})

for oportunity in oportunities:
    titulo = oportunity.find('p', {'class': 'h1'}).text
    href = oportunity.find('a')['href']
    title.append(titulo)
    link.append("https://remotar.com.br" + href)

driver.quit()

data = pd.DataFrame({'Titulo': title, 'Link': link})
data.to_html('teste.html')
data.to_json('teste.json')