# -*- encoding: utf-8 -*-

import requests
import pandas as pd
import selenium.webdriver.support.ui as ui
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json

#Pegar conteúdo HTML a partir da URL
#ToDo: Deixar o cliente selecionar os grupos


# url1 = input("URL do primeiro grupo: ")
url1 = input("URL of first group: ")
#url2 = input("URL do segundo grupo: ")
url2 = input("URL of the second group: ")

if url2 != '0':
    url3 = input("URL do terceiro grupo: ")
    if url3 != '0':
        url4 = input("URL do quarto grupo: ")
        if url4 != '0':
            url5 = input("URL do quinto grupo: ")

def openMenu():
    menu = driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[1]/div/div/div[2]/div/div[1]")
    menu.click()

    #Iniciar o elemento "encaminhar"
    element = driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[1]/div/div/div[2]/div/div[1]/ul/li[1]/a")
    element.click()
    sleep(1)

def findMessages(groupX):
    f = open(groupX, 'r')
    p = f.readline()
    f.close()

    all_div = driver.find_elements_by_xpath("//div[@class='im_message_outer_wrap hasselect']")
    for x in range(0,len(all_div)):
        idMessage = all_div[x].get_attribute('data-msg-id')
        if int(idMessage) > int(p.strip()):    
            all_div[x].click()
            fp = open(groupX, 'w')
            fp.writelines(idMessage)
            print("Encontradas mensagens a serem selecionadas")


def forwardMessages():
    #Clicar no botão para encaminhar
    #encaminhar = driver.find_element_by_xpath("//*[@id='ng-app']/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[1]/div[2]/a[2]")
    try:
    # Insert your scraping action here
        if driver.find_element_by_xpath("//a[@class='btn btn-primary im_edit_forward_btn disabled']") != 0 :     
            print("Nenhuma mensagem nova")
            return False

    except NoSuchElementException:
    # Just append a None or ""
        print("Há mensagens novas")

    encaminhar = driver.find_element_by_xpath("//a[@class='btn btn-primary im_edit_forward_btn']")
    encaminhar.click()
    sleep(4)
    #Encontrar o grupo para enviar
    #ToDo: encontrar uma maneira nova de selecionar o grupo
    group = driver.find_element_by_xpath("//*[@id='ng-app']/body/div[6]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/ul/li[2]")
    group.click()
    print("GrupoSelecionado com sucesso")

    return True

def sendMessages():
    enviar = driver.find_element_by_xpath("//button[@type='submit']")
    wait = ui.WebDriverWait(driver,10)
    enviar.click()
    print("SendMessages")
    sleep(3)
    enviar.click()

while True:
    print("Iniciando primeira url")
    #Carregar cookies para manter a conta logada e evitar bloqueio
    option = Options()
    option.add_argument("user-data-dir=C:\\Users\\gusta\\AppData\\Local\\Google\\Chrome\\User Data\\Default ")
    driver = webdriver.Chrome(options=option)
    driver.get("https://www.google.com")

    driver.get(url1)
    sleep(5)

    openMenu()

    findMessages("group1.js")
    
    sleep(2)

    if forwardMessages():

        sleep(2)

        sendMessages()

        print("ForwardMessages Finalizado")

    driver.quit()
    print("Processo Finalizado URL1")



    #-------------------------------------------------------------------------------------------------------------------------#
    if url2 != '0':
        print("Iniciando segunda url")
        #Carregar cookies para manter a conta logada e evitar bloqueio
        option = Options()
        option.add_argument("user-data-dir=C:\\Users\\gusta\\AppData\\Local\\Google\\Chrome\\User Data\\Default ")
        driver = webdriver.Chrome(options=option)
        driver.get("https://www.google.com")

        driver.get(url2)
        sleep(5)

        openMenu()

        findMessages("group2.js")
        
        sleep(2)

        if forwardMessages():

            sleep(2)

            sendMessages()

            print("ForwardMessages Finalizado")


        driver.quit()
        print("Processo Finalizado URL2")
    #-------------------------------------------------------------------------------------------------------------------------#
        if url3 != '0':
            print("Iniciando terceira url")
            #Carregar cookies para manter a conta logada e evitar bloqueio
            option = Options()
            option.add_argument("user-data-dir=C:\\Users\\gusta\\AppData\\Local\\Google\\Chrome\\User Data\\Default ")
            driver = webdriver.Chrome(options=option)
            driver.get("https://www.google.com")

            driver.get(url3)
            sleep(5)

            openMenu()

            findMessages("group3.js")
            
            sleep(2)

            if forwardMessages():

                sleep(2)

                sendMessages()

                print("ForwardMessages Finalizado")


            driver.quit()
            print("Processo Finalizado URL3")
        #-------------------------------------------------------------------------------------------------------------------------#
            if url4 != '0':
                print("Iniciando quarta url")
                #Carregar cookies para manter a conta logada e evitar bloqueio
                option = Options()
                option.add_argument("user-data-dir=C:\\Users\\gusta\\AppData\\Local\\Google\\Chrome\\User Data\\Default ")
                driver = webdriver.Chrome(options=option)
                driver.get("https://www.google.com")

                driver.get(url4)
                sleep(5)

                openMenu()

                findMessages("group4.js")
                
                sleep(2)

                if forwardMessages():

                    sleep(2)

                    sendMessages()

                    print("ForwardMessages Finalizado")

                driver.quit()
                print("Processo Finalizado URL4")
            #-------------------------------------------------------------------------------------------------------------------------#
                if url5 != '0':
                    print("Iniciando quinta url")
                    #Carregar cookies para manter a conta logada e evitar bloqueio
                    option = Options()
                    option.add_argument("user-data-dir=C:\\Users\\gusta\\AppData\\Local\\Google\\Chrome\\User Data\\Default ")
                    driver = webdriver.Chrome(options=option)
                    driver.get("https://www.google.com")

                    driver.get(url5)
                    sleep(7)

                    openMenu()

                    findMessages("group5.js")
                    
                    sleep(2)

                    if forwardMessages():

                        sleep(2)

                        sendMessages()

                        print("ForwardMessages Finalizado")

                    driver.quit()
                    print("Processo Finalizado URL5")
                #-------------------------------------------------------------------------------------------------------------------------#

    