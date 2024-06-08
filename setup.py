# -*- encoding: utf-8 -*-

import requests
import selenium.webdriver.support.ui as ui
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json

def doingGroup(groupY, urlX):
        #Carregar cookies para manter a conta logada e evitar bloqueio
        option = Options()
        option.add_argument("user-data-dir=C:\\Users\\gusta\\AppData\\Local\\Google\\Chrome\\User Data\\Default ")
        driver = webdriver.Chrome(options=option)
        driver.get("https://www.google.com")

        driver.get(urlX)
        sleep(5)

        openMenu(driver)

        findMessages(groupY, driver)
        print(groupY)
            
        sleep(2)

        driver.quit()
        print("Processo Finalizado.")


def openMenu(driverX):
    menu = driverX.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[1]/div/div/div[2]/div/div[1]")
    menu.click()

    #Iniciar o elemento "encaminhar"
    element = driverX.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[1]/div/div/div[2]/div/div[1]/ul/li[1]/a")
    element.click()
    sleep(1)

def findMessages(groupX, driverY):
    f = open(groupX, 'r')
    p = f.readline()
    f.close()

    all_div = driverY.find_elements_by_xpath("//div[@class='im_message_outer_wrap hasselect']")
    for x in range(0,len(all_div)):
        idMessage = all_div[x].get_attribute('data-msg-id')
        if int(idMessage) > int(p.strip()):    
            all_div[x].click()
            fp = open(groupX, 'w')
            fp.writelines(idMessage)

def newIDGroups():
    # answerX = input("Qual grupo deseja configurar? (0 = Nenhum | 1 = Grupo 1 | 2 = Grupo 2 | 3 = Grupo 3 | 4 = Grupo 4 | 5 = Grupo 5 | 9 = Todos os grupos\n")
    answerX = input("Which group do you want to configure? (0 = None | 1 = Group 1 | 2 = Group 2 | 3 = Group 3 | 4 = Group 4 | 5 = Group 5 | 9 = All groups\n")
    if answerX == '0':
        return False

    if answerX != '0':
        filterGroups(answerX)

    
    # again = input("Deseja configurar outro grupo? (0 = Não | Qualquer outro caractere = Sim\n")
    again = input("Do you want to configure another group? (0 = No | Any other character = Yes\n")

    if again != '0':
        newIDGroups()

def filterGroups(answer1):
    print(answer1)
    if answer1 == '9':
        #url1 = input("Insira URL do Grupo 1: ")
        url1 = input("Enter Group 1 URL: ")
        doingGroup("group1.js", url1)

        # url2 = input("Insira URL do Grupo 2: ")
        url2 = input("Enter Group 2 URL: ")
        doingGroup("group2.js", url2)

        #url3 = input("Insira URL do Grupo 3: ")
        url3 = input("Enter Group 3 URL: ")
        doingGroup("group3.js", url3)

        # url4 = input("Insira URL do Grupo 4: ")
        url4 = input("Enter Group 4 URL: ")
        doingGroup("group4.js", url4)

        # url5 = input("Insira URL do Grupo 5: ")
        url5 = input("Enter Group 5 URL: ")
        doingGroup("group5.js", url5)
        
    if answer1 == '1':
        # url1 = input("Insira URL do Grupo 1: ")
        url1 = input("Enter Group 1 URL: ")
        doingGroup("group1.js", url1)
        return 0


    if answer1 == '2':
        # url2 = input("Insira URL do Grupo 2: ")
        url2 = input("Enter Group 2 URL: ")
        doingGroup("group2.js", url2)   
        return 0


    if answer1 == '3':
        # url3 = input("Insira URL do Grupo 3: ")
        url3 = input("Enter Group 3 URL: ")
        doingGroup("group3.js", url3)
        return 0


    if answer1 == '4':
        # url4 = input("Insira URL do Grupo 4: ")
        url4 = input("Enter Group 4 URL: ")
        doingGroup("group4.js", url4)
        return 0


    if answer1 == '5':
        # url5 = input("Insira URL do Grupo 5: ")
        url5 = input("Enter Group 5 URL: ")
        doingGroup("group5.js", url5)
        return 0


newAccount = input("Deseja adicionar uma nova conta? (0 = Não | Qualquer outro caractere = Sim )\n")

if newAccount != '0':
    option = Options()
    option.add_argument("user-data-dir=C:\\Users\\gusta\\AppData\\Local\\Google\\Chrome\\User Data\\Default ")
    driver = webdriver.Chrome(options=option)
    driver.get("https://www.google.com")

    driver.get("https://web.telegram.org")

    # print("Por favor, entre manualmente a sua conta no Browser que foi aberto\n")
    print("Please manually log in to your account in the browser you opened\n")

    # print("Depois de 30 segundos, será possível continuar\n")
    print("After 30 seconds, you can continue\n")
    sleep(120)
    # input("Ao terminar, insira qualquer caractere para continuar...\n")
    input("When finished, enter any character to continue...\n")

# newID = input("Deseja configurar novos grupos? (0 = Não | Qualquer outro caractere = Sim )\n")
newID = input("Want to set up new groups? (0 = No | Any other character = Yes)\n")
if newID != '0':
    newIDGroups()
