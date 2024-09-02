from tabelaMaker.frequencias import criar_tabela_de_frequencias as freq
from tabelaMaker.classes import criar_tabela_de_classes as classes

with open('dados_brutos.txt', encoding="utf-8") as f:
    ler_dados = f.read()

dados_brutos = [int(x) for x in ler_dados.split()]

freq(dados_brutos)
classes(dados_brutos)