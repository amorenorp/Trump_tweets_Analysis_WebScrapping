
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


import source.fun_datacleaning as fnd
import source.fun_selenium as fns

url = "https://finance.yahoo.com/quote/%5EIXIC/history/?guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANi58iX0WyXEeycCs7bVqEPQtLiFIv6oysL-5MGFfFkudqCZ_mYT6ed9mAHMO_FcykTJzelOaVAHUiA2_njjmJZRUl2Ya3Vpj4gQrqePDwacxt1w_G7lL-6ZBnhG3aeoPskleuYSZJmcr8ImjTUMT9It6iMZKFQ7Um7ozY80jlZ1&guccounter=2"
archivo_yahoo = "^IXIC (5).csv"

def funcion_final():

    fns.nasdaqinfo(url)
    print('Ya he acabado con el Selenium')

    fnd.descargaclean(archivo_yahoo)
    print('Ya he limpiado la tabala de selenium')

    limpiar_unir=  fnd.unir_tablas('nasdaq_clean.csv',"trumptweets.csv")
    print('Acabo de limpiar y unir las tablas finales, te dejo un head')
    print(limpiar_unir)
    
    limpiar_unir.to_csv('output/tabla_final.csv', index=False,)
    print('Ya he guardado el csv para que juegues con los graficos. ')
    
    return limpiar_unir


funcion_final()