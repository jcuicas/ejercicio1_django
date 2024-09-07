'''
Httprequest     -> Objeto para recibir peticiones desde un cliente.
HttpResponse    -> Objeto para enviar respuestas desde el servidor.
'''
from django.http import HttpResponse
from datetime import datetime

def inicio(resquest):
    respuesta = '''
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <title>Página de inicio</title>
            </head>
            <body>
                <h1>Bienvenidos a la página de inicio</h1>
            </body>
        </html>
    '''
    
    return HttpResponse(respuesta)

def nosotros(request):
    respuesta = '''
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <title>Página de nosotros</title>
            </head>
            <body>
                <h1>Página de nosotros</h1>
            </body>
        </html>
    '''
    
    return HttpResponse(respuesta)

def contacto(request):
    respuesta = '''
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <title>Página de contacto</title>
            </head>
            <body>
                <h1>Página de contacto</h1>
            </body>
        </html>
    '''
    
    return HttpResponse(respuesta)

def imc(request, peso, altura):
    titulo = 'Calculadora IMC'
    calculo_imc = float(peso) / pow(float(altura), 2)
    encabezado = f'El indice de masa corporal es {calculo_imc:.2f}'
    fecha_actual = datetime.now().strftime('%d-%m-%Y - %I:%M:%S %p')
    
    #Status IMC
    if calculo_imc < 18.5:
        status = 'bajo peso'
    elif calculo_imc >= 18.5 and calculo_imc < 24.9:
        status = 'peso normal'
    elif calculo_imc >= 24.9 and calculo_imc < 29.9:
        status = 'sobrepeso'
    else:
        status = 'obesidad'
    
    respuesta = f'''
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <title>{titulo}</title>
            </head>
            <body>
                <h1>{encabezado}</h1>
                <h2>{status.upper()}</h2>
                <h3>Fecha: {fecha_actual}</h3>
            </body>
        </html>
    '''
    
    return HttpResponse(respuesta)