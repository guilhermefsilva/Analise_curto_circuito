import csv
from Barra import *

with open('C:/Users/guilh/OneDrive/Documentos/Python/Linha.csv','r') as linha:

    csvreader_linha = csv.DictReader(linha)

    linha_ID = []
    impedancia_positiva_Linha = []
    impedancia_negativa_Linha = []
    impedancia_zero_Linha = []
    comprimento_Linha = []
    barra_primario_Linha = []
    barra_secundario_Linha = []

    for row_linha in csvreader_linha:

        linha_ID.append(int(row_linha['Linha']))
        impedancia_positiva_Linha.append(complex(row_linha['Impedancia_positiva']))
        impedancia_negativa_Linha.append(complex(row_linha['Impedancia_negativa']))
        impedancia_zero_Linha.append(complex(row_linha['Impedancia_zero']))
        comprimento_Linha.append(float(row_linha['Comprimento']))
        barra_primario_Linha.append(int(row_linha['Primario']))
        barra_secundario_Linha.append(int(row_linha['Secundario']))

def admitancia_Linha():

    admitancia_positiva_Linha = []
    admitancia_negativa_Linha = []
    admitancia_zero_Linha = []

    for i1 in range(len(linha_ID)):
        for o1 in range (len(barra_ID)):
            if barra_primario_Linha[i1] == barra_ID[o1]:
                admitancia_positiva_Linha.append(1/(complex(impedancia_positiva_Linha[i1])*comprimento_Linha[i1]/(((tensao_Barra[o1])**2)/potencia_Base)))

    for i2 in range(len(linha_ID)):
        for o2 in range (len(barra_ID)):
            if barra_primario_Linha[i2] == barra_ID[o2]:
                admitancia_negativa_Linha.append(1/(complex(impedancia_negativa_Linha[i2])*comprimento_Linha[i2]/(((tensao_Barra[o2])**2)/potencia_Base)))

    for i0 in range(len(linha_ID)):
        for o0 in range (len(barra_ID)):
            if barra_primario_Linha[i0] == barra_ID[o0]:
                admitancia_zero_Linha.append(1/(complex(impedancia_zero_Linha[i0])*comprimento_Linha[i0]/(((tensao_Barra[o0])**2)/potencia_Base)))

    return

admitancia_Linha()