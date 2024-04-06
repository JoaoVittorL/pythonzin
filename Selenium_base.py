from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
import os

# servico = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service = servico)
CAMINHO = os.path.join(os.getcwd(),"Downloads_Selenium")

options = webdriver.ChromeOptions()
#ESSE APP STATE É PARA AJUSTAR AS CONFIGS DE BAIXAR PDF POR MEIO DO SCRIPT  "execute_script("window.print();")" QUE BASICAMENTE EXECUTA CTRL+P
appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local"
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(appState),
         'savefile.default_directory':CAMINHO,
         'download.prompt_for_download': False,
         'download.directory_upgrade': True,
         'plugins.always_open_pdf_externally': True,
         'download.default_directory' : CAMINHO}
options.add_experimental_option("prefs",prefs)
options.add_argument('--kiosk-printing')

chrome = webdriver.Chrome(service= Service(os.path.join(os.getcwd(),"chromedriver.exe")), options=options)


chrome.get('https://gps.performance-al.com.br/login/login.xhtml') 
chrome.maximize_window()

WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="j_username"]')))
chrome.find_element('xpath', '//*[@id="j_username"]').send_keys("joao_vittor")
WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="j_password"]')))
chrome.find_element('xpath', '//*[@id="j_password"]').send_keys("ECO@2012")
WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/form/button')))
chrome.find_element('xpath', '//*[@id="login"]/form/button').click()

chrome.get("https://gps.performance-al.com.br/secure/report/replay/#?vhc=808941342&date=20240405")

WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/form/div[2]/input')))
chrome.find_element('xpath', '/html/body/div[2]/div[1]/div/form/div[2]/input').clear()
chrome.find_element('xpath', '/html/body/div[2]/div[1]/div/form/div[2]/input').send_keys("04 de abril de 2024")


# WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/form/a')))
# chrome.find_element('xpath', '/html/body/div[2]/div[1]/div/form/a').click()

# WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-container"]/div/div[1]/div/div[3]/div[2]')))
# chrome.find_element('xpath', '//*[@id="main-container"]/div/div[1]/div/div[3]/div[2]').click()


# WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-container"]/div/div[1]/div/div[3]/div[2]')))
# chrome.find_element('xpath', '//*[@id="main-container"]/div/div[1]/div/div[3]/div[2]').click()

# divs = chrome.find_elements(By.XPATH, '//*[@class="card-body"]/div[contains(@class, "travel-card")]')

# primeira_div = divs[0]
# ultima_div = divs[-1]

# print(primeira_div.text[:13].rsplit(" - ",1)[0])

# array.append(['PLACA', primeira_div.text[:13].rsplit(" - ",1)[0],primeira_div.text[:13].rsplit(" - ",1)[1],ultima_div.text[:13].rsplit(" - ",1)[1]])

# print(array)

#COLOCA O LINK E COMECE 
# chrome.switch_to.default_content()
# WebDriverWait(chrome, 200).until(EC.frame_to_be_available_and_switch_to_it((By.ID, ''))) #By.NAME
# WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '')))
# chrome.find_element('xpath', '').click()
# chrome.find_element('xpath', '').send_keys('')



class MinhaClasse:
    """Classe tal"""
    def __init__(self, user : str) -> None:
        # , 'OUM3F93', 'PGO2I86'
        self.array : list = ['JRF9524']
        self.username : str = "joao_vittor"
        self.password : str = "ECO@2012"
        self.data : str = "04 de abril de 2024"
    def imprimir_placas(self):

        try:
            for placa in self.array:
                ## ABRE O DROPDOWN DE PLACAS             
                WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/form/div[1]/div/div[1]')))
                chrome.find_element('xpath', '/html/body/div[2]/div[1]/div/form/div[1]/div/div[1]').click()
                ## ABRE O DROPDOWN DE PLACAS             
                                
                ## ESCOLHE A PLACA
                chrome.find_element('xpath', '/html/body/div[2]/div[1]/div/form/div[1]/div/div[1]/input').send_keys("JRF9524")
                chrome.find_element('xpath', '/html/body/div[2]/div[1]/div/form/div[1]/div/div[1]/input').send_keys(Keys.ENTER)                
                ## ESCOLHE A PLACA
                
                
                
                # WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/form/a')))
                # chrome.find_element('xpath', '/html/body/div[2]/div[1]/div/form/a').click()
                
                # WebDriverWait(chrome, 200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-container"]/div/div[1]/div/div[3]/div[2]')))
                # chrome.find_element('xpath', '//*[@id="main-container"]/div/div[1]/div/div[3]/div[2]').click()
              
                
                while True:
                    try:
                        comand = input("Comand: ")
                        eval(comand)
                    except Exception as erro:
                        print(erro)
                        pass
               
        except Exception as erro:
            print(erro)
            while True:
                try:
                    comand = input("Comand: ")
                    eval(comand)
                except Exception as erro:
                    print(erro)
                    pass
                pass
        
if __name__ == "__main__":
    minha_instancia = MinhaClasse(user="joao")
    minha_instancia.imprimir_placas()

input('Wait')# USO ESSE COMANDO APENAS PARA PARAR O SELENIUM E IMPEDIR QUE ELE FECHE AO DAR ERRO