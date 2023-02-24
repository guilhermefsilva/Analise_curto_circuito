from Linha import *
from Transformador import *
from Gerador import *
from Barra import *

def admitancia_Linha():

    admitancia_positiva_Linha = []
    admitancia_negativa_Linha = []
    admitancia_zero_Linha = []

    for i1 in range(len(linha_ID)):
        for o1 in range (len(barra_ID)):
            if barra_primario_Linha[i1] == barra_ID[o1]:
                admitancia_positiva_Linha.append(1/(impedancia_positiva_Linha[i1]*comprimento_Linha[i1]/(((tensao_Barra[o1])**2)/potencia_Base)))

                admitancia_negativa_Linha.append(1/(impedancia_negativa_Linha[i1]*comprimento_Linha[i1]/(((tensao_Barra[o1])**2)/potencia_Base)))

                admitancia_zero_Linha.append(1/(impedancia_zero_Linha[i1]*comprimento_Linha[i1]/(((tensao_Barra[o1])**2)/potencia_Base)))

    return admitancia_positiva_Linha, admitancia_negativa_Linha, admitancia_zero_Linha

def admitancia_Transformador():

    admitancia_Trafo = []
    admitancia_zero_Trafo = []
    impedancia_aterramento_Primario = []
    impedancia_aterramento_Secundario = []

    for t1 in range(len(transformador_ID)):
        for r1 in range(len(barra_ID)):
            if barra_primario_Transformador [t1] == barra_ID [r1]:
                admitancia_Trafo.append(1/complex(0,((impedancia_Transformador[t1])/100)*(((tensao_primario_Transformador[t1])/(tensao_Barra[r1]))**2)*((potencia_Base)/(potencia_Transformador[t1]))))
                
                if complex(aterramento_primario_Transformador[t1]).real != 0 or complex(aterramento_primario_Transformador[t1]).imag:
                    impedancia_aterramento_Primario.append(aterramento_primario_Transformador[t1]*((potencia_Base)/((tensao_Barra[r1])**2)))
                else:
                    impedancia_aterramento_Primario.append(0)

            if barra_secundario_Transformador [t1] == barra_ID [r1]:
                
                if complex(aterramento_secundario_Transformador[t1]).real != 0 or complex(aterramento_secundario_Transformador[t1]).imag:
                    impedancia_aterramento_Secundario.append(aterramento_secundario_Transformador[t1]*((potencia_Base)/((tensao_Barra[r1])**2)))
                else:
                    impedancia_aterramento_Secundario.append(0)
            
        if conexao_Transformador[t1] == "YaY" or conexao_Transformador[t1] == "YaD" or conexao_Transformador[t1] == "YaYad":
            admitancia_zero_Trafo.append(1/(1/admitancia_Trafo[t1] + (impedancia_aterramento_Primario[t1])*3))

        elif conexao_Transformador[t1] == "YYa" or conexao_Transformador[t1] == "DYa" or conexao_Transformador[t1] == "YadYa":
            admitancia_zero_Trafo.append(1/(1/admitancia_Trafo[t1] + (impedancia_aterramento_Secundario[t1])*3))

        elif conexao_Transformador[t1] == "YaYa":
            admitancia_zero_Trafo.append(1/(1/admitancia_Trafo[t1] + (impedancia_aterramento_Primario[t1])*3 + (impedancia_aterramento_Secundario[t1])*3))
        
        else:
            admitancia_zero_Trafo.append(admitancia_Trafo[t1])

    return admitancia_Trafo, admitancia_zero_Trafo

def admitancia_Gerador():

    admitancia_positiva_Gerador = []
    admitancia_negativa_Gerador = []
    admitancia_zero_Gerador = []
    aterramento_Gerador = []

    for g1 in range(len(gerador_ID)):
        for f1 in range(len(barra_ID)):

            if barra_Gerador[g1] == barra_ID [f1]:
                admitancia_positiva_Gerador.append(1/(complex(0,(impedancia_positiva_Gerador[g1]) * (((tensao_Gerador[g1])/(tensao_Barra[f1]))**2) * (potencia_Base/potencia_Gerador[g1]))))
                admitancia_negativa_Gerador.append(1/(complex(0,(impedancia_negativa_Gerador[g1]) * (((tensao_Gerador[g1])/(tensao_Barra[f1]))**2) * (potencia_Base/potencia_Gerador[g1]))))
                aterramento_Gerador.append(impedancia_aterramento_Gerador[g1] * (tensao_Gerador[g1]/tensao_Barra[f1])**2 * (potencia_Base/potencia_Gerador[g1]))
                
                if conexao_Gerador[g1] == "Ya":
                    admitancia_zero_Gerador.append(1/(complex(0,impedancia_zero_Gerador[g1] * (((tensao_Gerador[g1])/(tensao_Barra[f1]))**2) * (potencia_Base/potencia_Gerador[g1])) + aterramento_Gerador[g1]*3))
                else:
                    admitancia_zero_Gerador.append(0)

    return admitancia_positiva_Gerador, admitancia_negativa_Gerador, admitancia_zero_Gerador