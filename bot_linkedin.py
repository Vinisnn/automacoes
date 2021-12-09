from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

#Processo de login no site

driver.get("https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
login = driver.find_element(By.ID, "username")
login.send_keys("vinicius_samaritano@yahoo.com.br")
senha = driver.find_element(By.ID, "password")
senha.send_keys("98889803")
driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()
time.sleep(2)


#Procurando conexões em Data Science

assunto = input("Insira o assunto desejado: ")
assunto = assunto.split()
busca_assunto = assunto[0] + '%20' + assunto[1]
driver.get(f'https://www.linkedin.com/search/results/people/?keywords={busca_assunto}&origin=GLOBAL_SEARCH_HEADER&sid=i8o')
time.sleep(2)

#Procurando os botões cujo texto contido seja o "Conectar"
mudar_pag = 1
while 1:
    botoes = driver.find_elements(By.TAG_NAME, 'button')
    conectar = [btn for btn in botoes if btn.text == "Conectar"]

#Realizando as conexões e enviando mensagem personalizada

    for btn in conectar:
        btn.click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'mr1').click()
        mensagem = driver.find_element(By.ID, "custom-message").send_keys("Olááá !!! Boa tarde ! Me chamo Vinicius e sou graduando de Analise e Dev de Sistemas. Gostaria de expandir minha rede de conexões aqui no Linkedin com o intuito de me aprimorar profissionalmente e aprender com aqueles que possuem uma bagagem de conhecimento maior na área Ciência de Dados !")
        time.sleep(6)
        driver.find_element(By.CLASS_NAME, 'ml1').click()
        time.sleep(6)
    mudar_pag += 1   
    driver.get(f'https://www.linkedin.com/search/results/people/?keywords={busca_assunto}&origin=GLOBAL_SEARCH_HEADER&page={mudar_pag}&sid=UU-')
    time.sleep(2)

