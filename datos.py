from openpyxl import Workbook, load_workbook

libro = load_workbook(filename='Base/Base Seguimiento Observ Auditoría al_30042021.xlsx', read_only=True)

hoja = libro.active

matriz = []
datos = {}

for c in range(1,20):
    if hoja.cell(row=1, column=c).value == None:
        break
    else:
        for r in range(2,10):
            datos[hoja.cell(row=1, column=c).value] = hoja.cell(row=r, column=c).value
        matriz.append(datos)

print(matriz[2])
