vizinhos = {
 'Arnor':('Eriador','Forodwaith','Rhovaríon'),
 'Rhovaríon':('Mordor','Rhûr','Eriador','Rohan','Arnor','Forodwaith'),
 'Gondor':('Rohan','Mordor','Eriador'),
 'Forodwaith':('Arnor','Rhovaríon','Rhûr'),
 'Mordor':('Rohan','Haradwaith','Rhûr','Gondor','Rhovaríon'),
 'Rhûr':('Mordor','Rhovaríon','Forodwaith'),
 'Rohan':('Gondor','Eriador','Mordor','Rhovaríon'),
 'Eriador':('Rohan','Arnor','Gondor'),
 'Haradwaith':('Mordor',),
}

distancias={
 'Arnon':(140,118,75),
 'Rhovaríon':(120,138,146,87,80,211),
 'Gondor':(140,99,151),
 'Forodwaith':(118,211,138),
 'Mordor':(140,111,138,100,75),
 'Rhûr':(120,75,211),
 'Rohan':(100,146,120,75),
 'Eriador':(140,),
 'Rohan':(211,90,101,85),
 'Eriador':(90,80,100),
 'Haradwaith':(120,),
}



def busca_em_profundidade (cidade_origem, cidade_destino):
    caminho = []
    borda = []
    custo = 0

    if cidade_origem not in vizinhos or cidade_destino not in vizinhos:
        return 'Uma ou as duas cidades nao existem'

    if cidade_origem != cidade_destino:
        borda.append(cidade_origem)
        explorado = []
        no_pai = {}
    else:
        caminho.append(cidade_origem)
        caminho.append(custo)
        return {"Caminho": (caminho)}

    while True:
        if borda == []:
            return 'Não há solução'

        no = borda.pop()
        explorado.append(no)

        for chave, valor in enumerate(vizinhos[no]):
            no_filho = [valor, distancias[no][chave]]
            
            if no_filho[0] not in explorado and no_filho[0] not in borda:
                no_pai[no_filho[0]] = no, no_filho[1]
                if no_filho[0] == cidade_destino:
                    i = no_filho[0]

                    while i != cidade_origem:
                        custo += no_pai[i][1]
                        caminho.append(i)
                        i = no_pai[i][0]

                    caminho.append(i)
                    caminho.reverse()
                    caminho.append(custo)
                    return {"Caminho": (caminho)}
                
                borda.append(no_filho[0])


cidade_origem = input('Cidade origem: ')
cidade_destino = input('Cidade destino: ')

print (busca_em_profundidade (cidade_origem, cidade_destino))
