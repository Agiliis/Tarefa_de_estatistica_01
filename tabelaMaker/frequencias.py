import xlsxwriter as xls
from tabelaMaker.calc_m import *

def criar_tabela_de_frequencias(dados_brutos):
    workbook = xls.Workbook('./planilhas/Tarefa de estatística 01 - Tabela de Frequencias.xlsx')
    worksheet = workbook.add_worksheet()

    negrito = workbook.add_format({'bold': 1})
    porcentagem = workbook.add_format({'num_format': '##%'})

    rotulos = ["fi", "fp", "fp(%)", "fac", "fac(%)", "média", "mediana", "moda"];
    sz = 0
    rol = []
    dados = {}
    media, mediana, moda = 0, 0, []

    sz = len(dados_brutos)
    rol = sorted(dados_brutos)
    for dado in rol:
        if dado not in dados:
            dados[dado] = [1, 1/sz]
        else:
            dados[dado][0] += 1
            dados[dado][1] += 1/sz

    media = calc_media(rol)
    mediana = calc_mediana(rol)
    moda = calc_moda(dados)

    ## rótulos
    worksheet.write('A1', "Tabela de frequências", negrito)

    j = 1

    worksheet.write('A2', "Dados", negrito)
    for rotulo in rotulos:
        worksheet.write(1, j, rotulo, negrito)
        j += 1

    i = 2
    j = 0
    ## rótulos

    fac = 0

    for dado, freq in dados.items():
        fi = freq[0]
        fp = freq[1]

        fac += fi

        worksheet.write(i, 0, dado)
        worksheet.write(i, 1, fi)
        worksheet.write(i, 2, round(fp, 2))
        worksheet.write(i, 3, round(fp, 2), porcentagem)
        worksheet.write(i, 4, fac)
        worksheet.write(i, 5, round(fac/sz, 2), porcentagem)

        i += 1
        
    worksheet.write(2, 6, media)
    worksheet.write(2, 7, mediana)
    if len(moda) != 0:
        worksheet.write_column(2, 8, moda)
    else:
        worksheet.write(2, 8, "Não há moda")

    workbook.close()