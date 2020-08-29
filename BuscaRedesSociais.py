from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()

driver.implicitly_wait(10)


email = " "
senha = " "



driver.get("https://discord.com/login")

#Encontra e preenche o campo email
campo_user = driver.find_element_by_name("email")
campo_user.send_keys(email)

#Encontra e rpeenche o campo senha
campo_senha = driver.find_element_by_name("password")

campo_senha.send_keys(senha)

botao = driver.find_element_by_css_selector(".button-3k0cO7")
botao.click()

#Server do Behind the code
brcode = driver.find_element_by_xpath("//a[@aria-label='Behind the Code BR']")
brcode.click()

#Canal network
network = driver.find_element_by_id("channels-12")
network.click()
#Esta parte sobe até o topo da pagina

linkedin = []
instagram = []
github = []
redeSociais = {}



def sobetopo():
    #Esta função faz scroll na página até o topo
    foi = "nao"
    while foi != "sim":
        driver.execute_script('document.querySelector(".scroller-2LSbBU").scrollTo(0,0);')
        foi = driver.execute_script('return document.querySelector(".header-3uLluP") !== null ? "sim" : "nao"')

def retornalinks(listaAs):
    #Esta função recebe uma lista de elementos do selenium e retorna apenas os links
    links = []
    for l in listaAs:
        links.append(l.text)
    return links

def geraJson(redeSociais):
    #Esta função um dicionário de links das redes sociais linkedin, instagram e github
    #E coloca tudo em um arquivo json
    with open("redessocials.json", "w") as outfile:  
        json.dump(redeSociais, outfile)


def retornarbeak(ponto):
    #Esta função serve para encontrar o fim da pagina
    #A partir de 3 scrolls da página existe duas classes wrapper-3vR61M
    #No final da página ele vira 1, assim é possivel encontrar o fim da pagina
    if ponto > 5:     
        if len(driver.find_elements_by_class_name("wrapper-3vR61M")) == 1:
            print("Fim")
            return True
        else:
            return False




sobetopo()


ponto = 0
while True:

    atual = driver.find_elements_by_class_name("message-2qnXI6")

    if ponto == 0:
        antes = atual[:]
        listaAs = driver.find_elements_by_tag_name('a')
        links = retornalinks(listaAs)
        atual[-1].location_once_scrolled_into_view
        print(atual[-1].get_attribute('id'))
        print("vazio")
        ponto += 1
    else:

        if len(antes) == len(atual):
            print("iguais")
            if retornarbeak(ponto):
                break
            pass
        else:

            antes = atual[:]  
            listaAs = driver.find_elements_by_tag_name('a')
            links = links + retornalinks(listaAs)
            atual[-1].location_once_scrolled_into_view
            print(atual[-1].get_attribute('id'))
            print("adicionou a lista")
            ponto += 1
            if retornarbeak(ponto):
                break

            
#Esta parte filtra os links de acordo com a rede social e adiciona a uma lista
for l in links:
    if l.startswith("https://www.linkedin.com/in/"):
        linkedin.append(l)

    if l.startswith("https://instagram.com/"):
        instagram.append(l)

    if l.startswith("https://github.com/"):
        github.append(l)

#A função set aqui faz uma filtragem na lista de links repetidos
redeSociais["linkedin"] = list(set(linkedin))
redeSociais["github"] = list(set(github))
redeSociais["instagram"] = list(set(instagram))
geraJson(redeSociais)

driver.close()