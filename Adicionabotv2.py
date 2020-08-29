from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import json


def bt_Concluido():
    #Este botão esta no pop up que pede email e nota para conectar
    driver.find_element_by_xpath("//button[@aria-label='Concluído']").click()

def adiciona_nota(nota):
    #Esta função adiciona uma mensagem na nota de conecção
    driver.find_element_by_xpath("//button[@aria-label='Adicionar nota']").click()
    driver.find_element_by_xpath("//textarea[@name='message']").send_keys(nota)

def clickabtAzul():
    #Esta função clicka no primeiro botão azul de conectar da pagina
    driver.find_element_by_class_name("pv-s-profile-actions.pv-s-profile-actions--connect.ml2.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view").click()

def clicka_lst_mais():
    #Esta função clicka para abrir a lista

    driver.find_elements_by_class_name("pv-s-profile-actions__overflow-toggle.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.artdeco-dropdown__trigger.artdeco-dropdown__trigger--placement-bottom.ember-view")[0].click()


def bt_adiciona_da_lista():
    
    driver.find_element_by_class_name("pv-s-profile-actions.pv-s-profile-actions--connect.pv-s-profile-actions__overflow-button.full-width.text-align-left.artdeco-dropdown__item.artdeco-dropdown__item--is-dropdown.ember-view").click()

def fld_reg_email(email):
    driver.find_element_by_id("email").send_keys(email)

def login(email, senha, url):
    driver.get(url)

    campo_user = driver.find_element_by_id("username")
    campo_user.send_keys(email)

    campo_pass = driver.find_element_by_id("password")
    campo_pass.send_keys(senha)

    driver.find_element_by_xpath("//button[@type='submit']").click()


def principal(nota, email):
    try:
        driver.implicitly_wait(2)
        clickabtAzul()
        adiciona_nota(nota)
        bt_Concluido()
        driver.implicitly_wait(5)
        
    except Exception as msgerro:

        try:
            clicka_lst_mais()
            bt_adiciona_da_lista()
            idemail = driver.find_element_by_id("send-invite-modal").text
            if idemail == 'Você pode personalizar este convite':
                adiciona_nota(nota)
                bt_Concluido()
            else:
                try:
                    fld_reg_email(email)                             
                    adiciona_nota(nota)
                    bt_Concluido()
                except Exception as msgerro2:
                    print("Campo email não encontrado")               
            

        except Exception as msgerro1:
        
            if driver.find_elements_by_class_name("profile-unavailable") == []:
                print("Erro não encontrado")
            else:
                print("Perfil não existe")


driver = webdriver.Chrome()
driver.implicitly_wait(5)
url = "https://www.linkedin.com/uas/login"
email = ""
senha = ''
nota = "Olá, Sou participante do Desafio IBM, estou conectando todos do chat network. \n Fiz uma automação usando python se quiser usar acesse meu github. \n https://github.com/VinasRibeiro/AdicionaBot \n Boa sorte."

login(email, senha, url)
principal(nota, email)

with open('redessocials.json') as json_file:
    data = json.load(json_file)

for l in data["linkedin"]:
    driver.get(l)
    principal(nota, email)

driver.close()
