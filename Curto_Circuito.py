import math
import cmath
from Barra import *
from Matriz import *

class calculo_curto:
    
    def curto_circuito():
        
        matriz_Inversa_Pos, matriz_Inversa_Neg, matriz_Inversa_0 = matriz_Inversa(matriz_Pos, matriz_Neg, matriz0)

        impedancia_pos_Barra = []
        impedancia_neg_Barra = []
        impedancia_0_Barra = []
        CC_Trifasico = []
        CC_Fase_Terra = []
        CC_Fase_Fase = []
        CC_Fase_Fase_Terra_A = []
        CC_Fase_Fase_Terra_B = []
        CC_Fase_Fase_Terra_C = []


        for b in range(len(barra_ID)):

            impedancia_pos_Barra.append(matriz_Inversa_Pos[b,b])
            impedancia_neg_Barra.append(matriz_Inversa_Neg[b,b])
            impedancia_0_Barra.append(matriz_Inversa_0[b,b])

            CC_Trifasico.append(abs(1/impedancia_pos_Barra[b]))
            CC_Fase_Terra.append(abs(3/(impedancia_pos_Barra[b] + impedancia_neg_Barra[b] + impedancia_0_Barra[b])))
            CC_Fase_Fase.append(abs(math.sqrt(3)/(impedancia_pos_Barra[b] + impedancia_neg_Barra[b])))
            CC_Fase_Fase_Terra_A.append(abs((3 * impedancia_neg_Barra[b]) / ((impedancia_pos_Barra[b] * impedancia_neg_Barra[b]) + (impedancia_pos_Barra[b] * impedancia_0_Barra[b]) + (impedancia_neg_Barra[b] * impedancia_0_Barra[b]))))
            CC_Fase_Fase_Terra_B.append(abs(complex(0,-1) * (math.sqrt(3) * (impedancia_0_Barra[b] - impedancia_neg_Barra[b] * cmath.rect(1, 2 * math.pi/3))) / ((impedancia_pos_Barra[b] * impedancia_neg_Barra[b]) + (impedancia_pos_Barra[b] * impedancia_0_Barra[b]) + (impedancia_neg_Barra[b] * impedancia_0_Barra[b]))))
            CC_Fase_Fase_Terra_C.append(abs(complex(0,1) * (math.sqrt(3) * (impedancia_0_Barra[b] - impedancia_neg_Barra[b] * cmath.rect(1, -2 * math.pi/3))) / ((impedancia_pos_Barra[b] * impedancia_neg_Barra[b]) + (impedancia_pos_Barra[b] * impedancia_0_Barra[b]) + (impedancia_neg_Barra[b] * impedancia_0_Barra[b]))))

        Curto_circuito = list(zip(barra_ID,CC_Trifasico,CC_Fase_Terra,CC_Fase_Fase,CC_Fase_Fase_Terra_A,CC_Fase_Fase_Terra_B,CC_Fase_Fase_Terra_C))

        with open('Curto_circuito.csv', mode='w', newline='') as file:

            writer = csv.writer(file)
            writer.writerow(['barra_ID','CC_Trifasico','CC_Fase_Terra','CC_Fase_Fase','CC_Fase_Fase_Terra_A','CC_Fase_Fase_Terra_B','CC_Fase_Fase_Terra_C'])

            for row in Curto_circuito:
                writer.writerow(row)