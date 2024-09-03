import xlsxwriter as xls
from tabelaMaker.calc_m import *

def criar_tabela_de_classes(dados_brutos):
    workbook = xls.Workbook('./planilhas/Tarefa de estatística 01 - Tabela de Classes.xlsx')
    worksheet = workbook.add_worksheet()

    negrito = workbook.add_format({'bold': 1})
    porcentagem = workbook.add_format({'num_format': '##%'})

    sz = [], 0
    rol = []
    n_de_classes, amplitude, amplitude_local = 0, 0, 0
    classes = []
    media_est, mediana_est, moda_est = 0, 0, []

    rotulos = ["fi", "fp", "fp(%)", "fac", "fac(%)", "média estimada", "mediana estimada", "moda estimada"];
    sz = len(dados_brutos)
    rol = sorted(dados_brutos)
    while(n_de_classes**2 < sz): n_de_classes += 1
    amplitude = rol[-1] - rol[0]
    amplitude_local = amplitude/n_de_classes

    lim = rol[0]
    for _ in range(n_de_classes):
        classes.append([[round(lim, 1), round(lim + amplitude_local, 1)], 0, 0, 0, 0])
        lim += amplitude_local

    lim = rol[0] + amplitude_local
    n = 0

    fac = 0
    for dado in rol:
        if dado >= lim and n != n_de_classes-1:
            fac += classes[n][1]
            n += 1
            lim += amplitude_local
            classes[n][3] += fac
            classes[n][4] += fac/sz

        classes[n][1] += 1
        classes[n][2] += 1/sz
        classes[n][3] += 1
        classes[n][4] += 1/sz

    ## rótulo
    worksheet.write('A1', "Tabela de classes", negrito)

    j = 1

    worksheet.write('A2', "Classes", negrito)
    for rotulo in rotulos:
        worksheet.write(1, j, rotulo, negrito)
        j += 1

    i = 2
    j = 0
    ## rótulo

    for classe in classes:

        worksheet.write(i, 0, f"{classe[0][0]} |- {classe[0][1]}")
        worksheet.write(i, 1, classe[1])
        worksheet.write(i, 2, classe[2])
        worksheet.write(i, 3, classe[2], porcentagem)
        worksheet.write(i, 4, classe[3])
        worksheet.write(i, 5, classe[4], porcentagem)
        i += 1

    media_est = calc_media_classe(classes)
    mediana_est = calc_mediana_classe(classes, amplitude_local)
    moda_est = calc_moda_classe(classes, amplitude_local)

    worksheet.write(2, 6, round(media_est, 3))
    worksheet.write(2, 7, round(mediana_est, 3))
    if len(moda_est) != 0:
        worksheet.write_column(2, 8, moda_est)
    else:
        worksheet.write(2, 8, "Não há moda")

    workbook.close()