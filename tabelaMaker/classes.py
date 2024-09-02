import xlsxwriter as xls

def criar_tabela_de_classes(dados_brutos):
    workbook = xls.Workbook('./planilhas/Tarefa de estatística 01 - Tabela de Classes.xlsx')
    worksheet = workbook.add_worksheet()

    negrito = workbook.add_format({'bold': 1})

    sz = [], 0
    rol = []
    n_de_classes, amplitude, amplitude_local = 0, 0, 0
    classes = []
    media_est, mediana_est, moda_est = 0, 0, 0

    rotulos = ["fi", "fp", "fp(%)", "fac", "fac(%)", "média estimada", "mediana estimada", "moda estimada"];
    sz = len(dados_brutos)
    rol = sorted(dados_brutos)
    while(n_de_classes**2 < sz): n_de_classes += 1
    amplitude = rol[-1] - rol[0]
    amplitude_local = amplitude/n_de_classes

    lim = rol[0]
    for _ in range(n_de_classes):
        classes.append([[lim, lim + amplitude_local], 0, 0])
        lim += amplitude_local

    lim = rol[0] + amplitude_local
    n = 0

    for dado in rol:
        if dado >= lim and n != n_de_classes-1:
            n += 1
            lim += amplitude_local

        classes[n][1] += 1
        classes[n][2] += 1/sz

    worksheet.write('A1', "Tabela de classes", negrito)

    j = 1

    worksheet.write('A2', "Classes", negrito)
    for rotulo in rotulos:
        worksheet.write(1, j, rotulo, negrito)
        j += 1

    i = 2
    j = 0

    fac = 0
    for classe in classes:
        fac += classe[1]

        worksheet.write(i, 0, f"{classe[0][0]} |- {classe[0][1]}")
        worksheet.write(i, 1, classe[1])
        worksheet.write(i, 2, classe[2])
        worksheet.write(i, 3, f"{classe[2]*100}%")
        worksheet.write(i, 4, fac)
        worksheet.write(i, 5, f"{fac/sz*100}%")
        i += 1

    # media_est = calc_media()
    # mediana_est = calc_mediana_classe()
    # moda_est = calc_moda_classe()

    worksheet.write(2, 6, media_est)
    worksheet.write(2, 7, mediana_est)
    worksheet.write(2, 8, moda_est)

    workbook.close()