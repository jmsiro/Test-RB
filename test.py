from datos import armado_matriz
from formulario import completar_formulario
from mail import enviar_mail


tablero = armado_matriz('/home/user/Escritorio/Programacion/Prueba_Rocketbot/Base/Base Seguimiento Observ Auditoría al_30042021.xlsx')

for linea in range(2,len(tablero)):
    mensajes_error = []
    if tablero[linea]["Estado"] == "Regularizado":
        mje = completar_formulario(tablero[linea])
        if mje == "OK":
            completados =+ 1
        else:
            mensajes_error.append(mje)
    elif tablero[linea]["Estado"] == "Atrasado":
        enviar_mail(tablero[linea])
        mails_enviados =+1
    else:
        if tablero[linea]["Estado"] == "Pendiente":
            pendientes =+1
        else:
            desconocidos =+1
            
print(completados)
print(mensajes_error)
print(mails_enviados)
print(pendientes)
print(desconocidos)