from datos import armado_matriz
from formulario import *
from correo import enviar_email

# Ruta de acceso al archivo 'Base' - Podria definirse como un input
ruta = '/home/user/Escritorio/Programacion/Prueba_Rocketbot/Base/Base Seguimiento Observ Auditoría al_30042021.xlsx'

# Mediante la función 'armado_matriz' se procesa la base de datos
tablero = armado_matriz(ruta)

# Se inicializan las variables de conteo para evitar errores al imprimir el 'informe' final - Me parecio mas simple que usar "try/except"
completados = 0
mensajes_error = 0
emails_enviados = 0
pendientes = 0
desconocidos = 0
mensajes_error = []

# Por cada linea de la base de datos se evalua si se envia el formulario de auditoria; se notifica el retraso al responsable o se ignora.
# Adicionalmente computa errores de la base de datos, para los casos en que el campo tiene opciones fijas.
for linea in range(0,len(tablero)):
    print(tablero[linea])
    if tablero[linea]["Estado"] == "Regularizado":
        mje = completar_formulario(tablero[linea])
        if mje == "OK":
            completados +=1
        else:
            mensajes_error.append(mje)
    elif tablero[linea]["Estado"] == "Atrasado":
        enviar_email(tablero[linea])
        emails_enviados +=1 
    else:
        if tablero[linea]["Estado"] == "Pendiente":
            pendientes +=1
        else:
            desconocidos +=1
        
print(f"""Proceso finalizado con exito!
    - Se enviaron {completados} Formularios de Auditoria
    - Se registraron los siguientes errores al completar los formularios:
    {mensajes_error}
    - Se realizaron {emails_enviados} notificaciones por atrasos.
    - Aun se encuentra pendientes {pendientes} observaciones de auditoria.
    - Se encontraron {desconocidos} clasificaciones de estado desconocidas.
    """)

cerrar_formulario()