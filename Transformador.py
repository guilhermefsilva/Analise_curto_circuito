import csv

with open('C:/Users/guilh/OneDrive/Documentos/Python/Transformador.csv','r') as transformador:

    csvreader_transformador = csv.DictReader(transformador)

    transformador_ID = []
    impedancia_Transformador = []
    aterramento_primario_Transformador = []
    aterramento_secundario_Transformador = []
    tensao_primario_Transformador = []
    tensao_secundario_Transformador = []
    potencia_Transformador = []
    conexao_Transformador = []
    barra_primario_Transformador = []
    barra_secundario_Transformador = []


    for row_transformador in csvreader_transformador:

        transformador_ID.append(int(row_transformador['Transformador']))
        impedancia_Transformador.append(float(row_transformador['Impedancia_percentual']))
        aterramento_primario_Transformador.append(complex(row_transformador['Impedancia_aterramento_primario']))
        aterramento_secundario_Transformador.append(complex(row_transformador['Impedancia_aterramento_secundario']))
        tensao_primario_Transformador.append(float(row_transformador['Tensao primario']))
        tensao_secundario_Transformador.append(float(row_transformador['Tensao secundario']))
        potencia_Transformador.append(float(row_transformador['Potencia']))
        conexao_Transformador.append(row_transformador['Tipo_de_conexao'])
        barra_primario_Transformador.append(int(row_transformador['Conexao_primario']))
        barra_secundario_Transformador.append(int(row_transformador['Conexao_secundario']))