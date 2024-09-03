import numpy as np

def calc_media(rol):
    media = np.sum(rol)/len(rol)
    return media

def calc_mediana(rol):
    mediana = 0
    sz = len(rol)
    
    if sz%2 == 1:
        mediana = rol[sz//2]
    else:
        mediana = (rol[sz/2] + rol[sz/2 + 1])/2

    return mediana

def calc_moda(dados):
    moda = []
    amodal = True
    maior_freq = dados[list(dados)[0]][0]

    for freqs in dados.values():
        if freqs[0] != maior_freq: 
            amodal = False
            maior_freq = max(maior_freq, freqs[0])
    
    if amodal: 
        return moda

    for dado, freqs in dados.items():
        if freqs[0] == maior_freq:
            moda.append(dado)

    return moda

def calc_media_classe(classes):
    media = 0
    medianas = []

    for classe in classes:
        mediana = (classe[0][1] + classe[0][0])/2
        for _ in range(classe[1]):
            medianas.append(mediana)

    media = calc_media(medianas)

    return media

def calc_mediana_classe(classes, h):
    mediana = 0
    sz = classes[-1][3]
    mediana_classe = 0
    mediana_pos = sz//2

    n = 0
    for classe in classes:
        if mediana_pos <= classe[3]:
            mediana_classe = n
            break

        n += 1

    Li = classes[mediana_classe][0][0]
    fac_ant = 0
    if mediana_classe != 0: 
        fac_ant = classes[mediana_classe - 1][3]
    fi = classes[mediana_classe][1]

    mediana = Li + (sz/2 - fac_ant)*h / fi

    return mediana

def calc_moda_classe(classes, h):
    moda = []
    amodal = True
    maior_freq = classes[0][1]

    for classe in classes:
        if classe[1] != maior_freq:
            amodal = False
            maior_freq = max(maior_freq, classe[1])

    if amodal:
        return moda
    
    n = 0
    delta_ant = 0
    for classe in classes:
        if classe[1] == maior_freq:
            Li = classe[0][0]
            delta_ant = classe[1] - delta_ant
            delta_post = classe[1]
            if n < len(classes)-1:
                delta_post -= classes[n + 1]

            formula = Li + (delta_ant)/(delta_ant + delta_post) * h

            moda.append(round(formula, 3))

        delta_ant = classe[1]
        n += 1

    return moda