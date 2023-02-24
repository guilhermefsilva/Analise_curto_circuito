import csv


with open('Gerador.csv','r') as gerador:

    csvreader_gerador = csv.DictReader(gerador)

    gerador_ID = []
    tensao_Gerador = []
    impedancia_positiva_Gerador = []
    impedancia_negativa_Gerador = []
    impedancia_zero_Gerador = []
    impedancia_aterramento_Gerador = []
    conexao_Gerador = []
    potencia_Gerador = []
    barra_Gerador = []

    for row_gerador in csvreader_gerador:

        gerador_ID.append(int(row_gerador['Gerador']))
        tensao_Gerador.append(float(row_gerador ['Tensao']))
        impedancia_positiva_Gerador.append(float(row_gerador ['Impedancia_positiva']))
        impedancia_negativa_Gerador.append(float(row_gerador ['Impedancia_negativa']))
        impedancia_zero_Gerador.append(float(row_gerador ['Impedancia_zero']))
        impedancia_aterramento_Gerador.append(complex(row_gerador['Impedancia_aterramento']))
        conexao_Gerador.append(row_gerador['Conexao_gerador'])
        potencia_Gerador.append(float(row_gerador['Potencia']))
        barra_Gerador.append(int(row_gerador['Barra_conexao']))