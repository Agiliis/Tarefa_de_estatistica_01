import xlsxwriter as xls
import numpy as np

def criar_tabela_de_frequencias(dados_brutos):
    workbook = xls.Workbook('./planilhas/Tarefa de estatística 01 - Tabela de Frequencias.xlsx')
    worksheet = workbook.add_worksheet()

    negrito = workbook.add_format({'bold': 1})

    rotulos = ["fi", "fp", "fp(%)", "fac", "fac(%)", "média", "mediana", "moda"];
    sz = [], 0
    rol = []
    freq_abs, freq_rel = {}, {}
    media, mediana, moda = 0, 0, []

    sz = len(dados_brutos)
    rol = sorted(dados_brutos)
    for dado in rol:
        if dado not in freq_abs:
            freq_abs[dado] = 1
        else:
            freq_abs[dado] = freq_abs[dado] + 1
    for dado, freq in freq_abs.items():
        freq_rel[dado] = freq/sz


    media = np.sum(rol)/sz
    if sz%2 == 1:
        mediana = rol[sz//2]
    else:
        mediana = (rol[sz/2] + rol[sz/2 + 1])/2


    worksheet.write('A1', "Tabela de frequências", negrito)

    j = 1

    worksheet.write('A2', "Dados", negrito)
    for rotulo in rotulos:
        worksheet.write(1, j, rotulo, negrito)
        j += 1

    i = 2
    j = 0

    fac = 0

    for dado, freq in freq_abs.items():
        fac += freq

        worksheet.write(i, 0, dado)
        worksheet.write(i, 1, freq)
        worksheet.write(i, 2, freq_rel[dado])
        worksheet.write(i, 3, f"{freq_rel[dado]*100}%")
        worksheet.write(i, 4, fac)
        worksheet.write(i, 5, f"{fac/sz*100}%")

        i += 1
        
    worksheet.write(2, 6, media)
    worksheet.write(2, 7, mediana)

    workbook.close()