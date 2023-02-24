import csv

potencia_Base = 1E+8

with open('../Analise_curto_circuito/Barra.csv','r') as barra:

    csvreader_barra = csv.DictReader(barra)

    barra_ID = []
    tensao_Barra = []

    for row_barra in csvreader_barra:

        barra_ID.append(int(row_barra['Barra']))
        tensao_Barra.append(float(row_barra['Tensao']))

s = len(barra_ID)-1