

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup



def nasdaqinfo(url):
    '''
    Esta función descarga un csv de la web Yahoo finance usando Selenium.
    Takes: url
    Returns: un .csv
    '''


    # open chrome
    driver = webdriver.Chrome()
    driver.implicitly_wait(30) # Esperar 30s para cargar
    
    # abrir la url que le damos
    driver.get(url)
    
    
    #1 Abrir desplegable fecha
    WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[1]/div[1]/div/div/div/span')))\
    .click()                                                          
     
    #2 seleccionar fecha
    WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[1]/div[1]/div/div/div/div/div/ul[2]/li[3]/button')))\
    .click()    
        
    
          
    #2 boton apply
    WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[1]/button')))\
    .click()
    
    #2 Selec download
    WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[2]/span[2]/a/span')))\
    .click()
    
    
    #close google
    driver.quit()
    
    return "Task done!"
    