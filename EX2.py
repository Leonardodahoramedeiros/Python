import openpyxl

# Criar um novo arquivo Excel
workbook = openpyxl.Workbook()

# Selecionar a planilha ativa
sheet = workbook.active

# Escrever o valor inicial na célula A1
sheet['A1'] = 1

# Preencher as células de A2 a A100 com valores crescentes
valor = 1
for i in range(2, 101):
    valor += 1
    sheet.cell(row=i, column=1).value = valor

# Salvar as alterações no arquivo Excel
workbook.save(r"C:\Users\Leonardo\Desktop\Python.xlsx")
