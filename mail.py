import smtplib, ssl

def enviar_mail(entrada):
    port = 465  # puerto para SSL
    
    # email_remitente = input("Ingresar email: ")
    email_remitente = 'parapruebas.dev@gmail.com'
    
    email_receptor=entrada['Correo responsable']
    
    mensaje = """Estimado {responsable}, el proceso {proceso} se encuentra {estado} segun nuestro resgistros.
    La fecha de compromiso fijada fue {fecha_compromiso}.
    La observación consignada fue: '{observacion}'.
    Atte."""
        
    mensaje = mensaje.format(responsable=entrada['Responsable'], proceso=entrada['Auditoría/Proceso'],estado=entrada['Estado'],fecha_compromiso=str(entrada['Fecha\nCompromiso'].date()),observacion=entrada['Observación'])
    
    # password = input("Ingresar password: ")
    password = 'Parapruebas123'
    
    # Crea contexto seguro para SSL
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(email_remitente, password)
        server.sendmail(email_remitente, email_receptor, mensaje.encode('utf-8'))