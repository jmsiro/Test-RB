import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Firefox()
driver.get('https://roc.myrb.io/s1/forms/M6I8P2PDOZFDBYYG')

# Elementos del formulario a completar y enviar
proceso = Select(driver.find_element_by_id("process"))
proceso.select_by_visible_text('Financiero')

tipo_riesgo = driver.find_element_by_id("tipo_riesgo")
tipo_riesgo.send_keys("a")

severidad = Select(driver.find_element_by_id("severidad"))
severidad.select_by_visible_text('Medio')

responsable = driver.find_element_by_id("res")
responsable.send_keys("Juan")

fecha_compromiso = driver.find_element_by_id("date")
fecha_compromiso.send_keys("2022-04-08")

observacion= driver.find_element_by_id("obs")
observacion.send_keys("Anduvo?")