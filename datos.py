from openpyxl import Workbook, load_workbook

# Abro libro. Los flags indican que es modo lectura y que muesta los resultados de las formulas del excel.
libro = load_workbook(filename='Base/Base Seguimiento Observ Auditoría al_30042021.xlsx', read_only=True, data_only=True)

#En este caso que es una sola hoja tomo la hoja activa, pero en caso que haya mas de una deberia seleccionarla utilizando el nombre de la misma como si fuera un diccionario.
hoja = libro['Hoja1']

matriz = []
matriz_atr = []
datos = {}

# Loop 1 = Recorre filas
# Loop 2 = Recorre Columnas
# Se crea una Lista de Diccionarios donde las 'Keys' son los titulos de las columnas y el 'Value' el valor de esa columna para cada fila.
for r in range(2,10):
    if hoja.cell(row=r, column=1).value == None:
        break
    else:
        for c in range(1,20):
            if hoja.cell(row=1, column=c).value == None:
                matriz.append(datos.copy()) # Se genera una copia del diccionario y se incopora a la lista
                datos.clear() # Se limpia del diccionario original para la proxima vuelta del loop
                break
            else:
                datos[hoja.cell(row=1, column=c).value] = hoja.cell(row=r, column=c).value
                
for i in range(0,len(matriz)):
    print(matriz[i])