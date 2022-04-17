from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get('https://roc.myrb.io/s1/forms/M6I8P2PDOZFDBYYG')

# Elementos del formulario a completar y enviar
def completar_formulario(entrada):
    
    # Selecciona el "dropdown menu" y elijr en función del texto que muestra. Otra opción es por "value" (codigo numerico - 1, 2, 3...)
    proceso = Select(driver.find_element_by_id("process"))
    # Se utiliza un 'Error handler' para cubir la posibilidad que haya un error de tipeo en el tablero que no coincida con los valores definidos para el campo.
    try:
        proceso.select_by_visible_text(entrada['Auditoría/Proceso'].rstrip())
    except:
        mensaje = "El valor de la fila {} no coincide con las opciones posibles para 'Proceso'"
        return mensaje.format(entrada['Fila'])
    
    tipo_riesgo = driver.find_element_by_id("tipo_riesgo")
    tipo_riesgo.send_keys(entrada['Tipo de Riesgo '])

    # Idem Proceso
    severidad = Select(driver.find_element_by_id("severidad"))
    # Idem Proceso
    try: 
        severidad.select_by_visible_text(entrada['Severidad\nObservación'].rstrip())
    except:
        mensaje = "El valor de la fila {} no coincide con las opciones posibles para 'Severidad'"
        return mensaje.format(entrada['Fila'])
    
    responsable = driver.find_element_by_id("res")
    responsable.send_keys(entrada['Responsable'])

    fecha_compromiso = driver.find_element_by_id("date")
    fecha_compromiso.send_keys(str(entrada['Fecha\nCompromiso'].date()))

    observacion= driver.find_element_by_id("obs")
    observacion.send_keys(entrada['Observación'])
    
    driver.find_element_by_id("submit").click()
    
    return "OK"
