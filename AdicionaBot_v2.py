#Este programa gera uma tela com campo email e senha, ainda não implementei o campo nota, para inserir uma nota ao adicionar uma pessoa
#Falta ativar o comando para clickar no botão adicionar

from tkinter import  *
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import json

def switchButtonState():
    if (button1['state'] == tk.NORMAL):
        button1['state'] = tk.DISABLED
    else:
        button1['state'] = tk.NORMAL
        
    Principal()
    

def Principal():
    
    url = "https://www.linkedin.com/uas/login"
    email = e.get()
    senha = ps.get()
    nota = "teste"

    login(email, senha, url)

    with open('redessocials.json') as json_file:
        data = json.load(json_file)

    for l in data["linkedin"]:
        driver.get(l)

        try:
            driver.implicitly_wait(2)
            clickabtAzul()
            adiciona_nota(nota)
            #driver.find_elements_by_xpath("//button[@aria-label='Concluído']")[0].click()
            driver.implicitly_wait(5)

        except Exception as msgerro:

            try:
                clicka_lst_mais()
                bt_adiciona_da_lista()
                idemail = driver.find_element_by_id("send-invite-modal").text
                if idemail == 'Você pode personalizar este convite':
                    adiciona_nota(nota)
                else:
                    try:
                        fld_reg_email(email)                             
                        adiciona_nota(nota)
                    except Exception as msgerro2:
                        print("Campo email não encontrado")               
                

            except Exception as msgerro1:
            
                if driver.find_elements_by_class_name("profile-unavailable") == []:
                    print("Erro não encontrado")
                else:
                    print("Perfil não existe")


    driver.quit()     

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

app = tk.Tk()
app.title("Adiciona Linkedin")
driver = webdriver.Chrome()
driver.implicitly_wait(5)
app.geometry("300x100")

e = Entry(app, width=30, borderwidth=5)
e.grid(row=0, column=2)
#e.pack(side=tk.RIGHT)
myLabel = Label(app, text="Email")
myLabel.grid(row=0, column=1)

ps = Entry(app, width=30, borderwidth=5)
ps.grid(row=1, column=2)

myLabel2 = Label(app, text="Senha")
myLabel2.grid(row=1, column=1)

button1 = tk.Button(app, text="Começar", command = switchButtonState)
button1.grid(row=3, column=1)
#button1.pack(side=tk.LEFT)


app.mainloop()
