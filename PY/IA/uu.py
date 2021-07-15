import string
import random

class IA:
    teste = []
    treinamento = []
    def atividade1(file, split, treinamento=[], teste=[]):
        arquivo = open(file,"r")
        base_dados = []
        m = []
       

        for x in range(1, 151):
            linha = arquivo.readline()
            base_dados.append(m)
            base_dados[x] = [(y) for y in linha.split(',') if y.strip()]
            float(base_dados[x][0])
            float(base_dados[x][1])
            float(base_dados[x][2])
            float(base_dados[x][3])
            print(base_dados[x])

        for x in range(len(base_dados)-1):
            rand = random.randint(0,150)
            if rand < split and (len(teste)<(100-split)):
                teste.append(base_dados[x])
            else:
                treinamento.append(base_dados[x])

        print(len(base_dados))
            

        
        arquivo.close()

    atividade1("iris.data.txt",70, treinamento, teste)

    
