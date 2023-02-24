import numpy as nb
import csv
from Barra import *
from Transformador import *
from Gerador import *
from Linha import *
from Admitancia import *

def matriz_Positiva (admitancia_pos_Linha, admitancia_Trafo, admitancia_pos_Gerador):

    matriz_Pos = nb.zeros((len(barra_ID),len(barra_ID)), dtype = complex)

    for m1 in range(len(barra_ID)):
        for n1 in range (len(barra_ID)):

            if m1 == n1:

                admitancia_Positiva = complex(0,0)

                for t1 in range(len(transformador_ID)):

                    if barra_primario_Transformador [t1] == barra_ID [m1] or barra_secundario_Transformador [t1] == barra_ID [n1]:
                        admitancia_Positiva = admitancia_Positiva + admitancia_Trafo[t1]
                

                for g1 in range(len(gerador_ID)):

                    if barra_Gerador [g1] == barra_ID [m1]:
                        admitancia_Positiva = admitancia_Positiva + admitancia_pos_Gerador[g1]
            
                
                for l1 in range(len(linha_ID)):

                    if barra_primario_Linha [l1] == barra_ID [m1] or barra_secundario_Linha [l1] == barra_ID [n1]:
                        admitancia_Positiva = admitancia_Positiva + admitancia_pos_Linha[l1]
              

                matriz_Pos [m1,n1] = admitancia_Positiva
            
            else:

                admitancia_Positiva = complex(0,0)

                for t1 in range(len(transformador_ID)):

                    if barra_primario_Transformador [t1] == barra_ID [m1] and barra_secundario_Transformador [t1] == barra_ID [n1]:
                        admitancia_Positiva = admitancia_Positiva + admitancia_Trafo[t1]
                    
                    elif barra_primario_Transformador [t1] == barra_ID [n1] and barra_secundario_Transformador [t1] == barra_ID [m1]:
                        admitancia_Positiva = admitancia_Positiva + admitancia_Trafo[t1]
                               
                for l1 in range(len(linha_ID)):

                    if barra_primario_Linha [l1] == barra_ID [m1] and barra_secundario_Linha [l1] == barra_ID [n1]:
                        admitancia_Positiva = admitancia_Positiva + admitancia_pos_Linha[l1]
                    
                    elif barra_primario_Linha [l1] == barra_ID [n1] and barra_secundario_Linha [l1] == barra_ID [m1]:
                        admitancia_Positiva = admitancia_Positiva + admitancia_pos_Linha[l1]
              
                matriz_Pos [m1,n1] = -1 * admitancia_Positiva
    
    with open('matrizpos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in matriz_Pos:
            writer.writerow(row)

    return matriz_Pos

def matriz_Negativa (admitancia_neg_Linha, admitancia_Trafo, admitancia_neg_Gerador):

    matriz_Neg = nb.zeros((len(barra_ID),len(barra_ID)), dtype = complex)
    
    for m2 in range(len(barra_ID)):
        for n2 in range (len(barra_ID)):

            if m2 == n2:

                admitancia_Negativa = complex(0,0)

                for t2 in range(len(transformador_ID)):

                    if barra_primario_Transformador [t2] == barra_ID [m2] or barra_secundario_Transformador [t2] == barra_ID [n2]:
                        admitancia_Negativa = admitancia_Negativa + admitancia_Trafo[t2]
                

                for g2 in range(len(gerador_ID)):

                    if barra_Gerador [g2] == barra_ID [m2]:
                        admitancia_Negativa = admitancia_Negativa + admitancia_neg_Gerador[g2]
            
                
                for l2 in range(len(linha_ID)):

                    if barra_primario_Linha [l2] == barra_ID [m2] or barra_secundario_Linha [l2] == barra_ID [n2]:
                        admitancia_Negativa = admitancia_Negativa + admitancia_neg_Linha[l2]
              

                matriz_Neg[m2,n2] = admitancia_Negativa
            
            else:

                admitancia_Negativa = complex(0,0)

                for t2 in range(len(transformador_ID)):

                    if barra_primario_Transformador [t2] == barra_ID [m2] and barra_secundario_Transformador [t2] == barra_ID [n2]:
                        admitancia_Negativa = admitancia_Negativa + admitancia_Trafo[t2]

                    elif barra_primario_Transformador [t2] == barra_ID [n2] and barra_secundario_Transformador [t2] == barra_ID [m2]:
                        admitancia_Negativa = admitancia_Negativa + admitancia_Trafo[t2]
                               
                for l2 in range(len(linha_ID)):

                    if barra_primario_Linha [l2] == barra_ID [m2] and barra_secundario_Linha [l2] == barra_ID [n2]:
                        admitancia_Negativa = admitancia_Negativa + admitancia_neg_Linha[l2]
                    
                    elif barra_primario_Linha [l2] == barra_ID [n2] and barra_secundario_Linha [l2] == barra_ID [m2]:
                        admitancia_Negativa = admitancia_Negativa + admitancia_neg_Linha[l2]
              
                matriz_Neg[m2,n2] = -1 * admitancia_Negativa
    
    with open('matrizneg.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in matriz_Neg:
            writer.writerow(row)

    return matriz_Neg

def matriz_Zero (admitancia0_Linha, admitancia0_Trafo, admitancia0_Gerador):

    matriz_0 = nb.zeros((len(barra_ID),len(barra_ID)), dtype = complex)

    for m0 in range(len(barra_ID)):
        for n0 in range (len(barra_ID)):

            if m0 == n0:

                admitancia_Zero = complex(0,0)

                for t0 in range(len(transformador_ID)):

                    if barra_primario_Transformador [t0] == barra_ID [m0]:
                        if conexao_Transformador[t0] == "YaYa" or conexao_Transformador[t0] == "YaYad" or conexao_Transformador[t0] == "YadYa" or conexao_Transformador[t0] == "YaD":
                            admitancia_Zero = admitancia_Zero + admitancia0_Trafo[t0]

                    elif barra_secundario_Transformador [t0] == barra_ID [n0]:
                        if conexao_Transformador[t0] == "YaYa" or conexao_Transformador[t0] == "YaYad" or conexao_Transformador[t0] == "YadYa" or conexao_Transformador[t0] == "DYa":
                            admitancia_Zero = admitancia_Zero + admitancia0_Trafo[t0]

                for g0 in range(len(gerador_ID)):

                    if barra_Gerador [g0] == barra_ID [m0]:
                        if conexao_Gerador[g0] == "Ya":
                            admitancia_Zero = admitancia_Zero + admitancia0_Gerador[g0]
            
                
                for l0 in range(len(linha_ID)):

                    if barra_primario_Linha [l0] == barra_ID [m0] or barra_secundario_Linha [l0] == barra_ID [n0]:
                        admitancia_Zero = admitancia_Zero + admitancia0_Linha[l0]
              

                matriz_0 [m0,n0] = admitancia_Zero
            
            else:

                admitancia_Zero = complex(0,0)

                for t0 in range(len(transformador_ID)):

                    if barra_primario_Transformador [t0] == barra_ID [m0] and barra_secundario_Transformador [t0] == barra_ID [n0]:
                        if conexao_Transformador[t0] == "YaYa" or conexao_Transformador[t0] == "YadYa" or conexao_Transformador[t0] == "YaYad":    
                            admitancia_Zero = admitancia_Zero + admitancia0_Trafo[t0]
                    
                    elif barra_primario_Transformador [t0] == barra_ID [n0] and barra_secundario_Transformador [t0] == barra_ID [m0]:
                        if conexao_Transformador[t0] == "YaYa" or conexao_Transformador[t0] == "YadYa" or conexao_Transformador[t0] == "YaYad":
                            admitancia_Zero = admitancia_Zero + admitancia0_Trafo[t0]
                               
                for l0 in range(len(linha_ID)):

                    if barra_primario_Linha [l0] == barra_ID [m0] and barra_secundario_Linha [l0] == barra_ID [n0]:
                        admitancia_Zero = admitancia_Zero + admitancia0_Linha[l0]
                    
                    elif barra_primario_Linha [l0] == barra_ID [n0] and barra_secundario_Linha [l0] == barra_ID [m0]:
                        admitancia_Zero = admitancia_Zero + admitancia0_Linha[l0]
              
                matriz_0 [m0,n0] = -1 * admitancia_Zero
    
    with open('matriz0.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in matriz_0:
            writer.writerow(row)

    return matriz_0

def matriz_Inversa(matriz_Pos, matriz_Neg, matriz0):

    matriz_inversa_Positiva = nb.linalg.inv(matriz_Pos)
    matriz_inversa_Negativa = nb.linalg.inv(matriz_Neg)
    matriz_inversa_Zero = nb.linalg.inv(matriz0)

    with open('matrizInv+.csv', mode='w', newline='') as file1:
        writer = csv.writer(file1)
        for row1 in matriz_inversa_Positiva:
            writer.writerow(row1)
    
    with open('matrizInv-.csv', mode='w', newline='') as file2:
        writer = csv.writer(file2)
        for row2 in matriz_inversa_Negativa:
            writer.writerow(row2)

    with open('matrizInv0.csv', mode='w', newline='') as file0:
        writer = csv.writer(file0)
        for row0 in matriz_inversa_Zero:
            writer.writerow(row0)
    
    return matriz_inversa_Positiva, matriz_inversa_Negativa, matriz_inversa_Zero

admitancia_pos_Linha, admitancia_neg_Linha, admitancia0_Linha = admitancia_Linha()
admitancia_Trafo, admitancia0_Transformador = admitancia_Transformador()
admitancia_pos_Gerador, admitancia_neg_Gerador, admitancia0_Gerador = admitancia_Gerador()

matriz_Pos = matriz_Positiva(admitancia_pos_Linha, admitancia_Trafo, admitancia_pos_Gerador)
matriz_Neg = matriz_Negativa(admitancia_neg_Linha, admitancia_Trafo, admitancia_neg_Gerador)
matriz0 = matriz_Zero(admitancia0_Linha, admitancia0_Transformador, admitancia0_Gerador)