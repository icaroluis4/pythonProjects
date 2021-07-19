
def mod(a,b): # mod function
    if(a<b):
        return a
    else:
        c=a%b
        return c



def cifra(words,e,n): # obtem as palavras e computa a cifra
    tam = len(words)
    i = 0
    lista = []
    while(i < tam):
        letter = words[i]
        k = ord(letter)
        k = k**e
        d = mod(k,n)
        lista.append(d)
        i += 1
    return lista



texto = input("Digite sua mensagem: ")
arq = open('chave_publica.txt','r')
n = int(arq.readline())
e = int(arq.readline())
arq.close()
print("e: ",e ," -- n:",n)
texto_cifrado = cifra(texto,e,n)
print('Your encrypted message:', texto_cifrado)
mensagem = open('mensagem_cifrada.txt','w',encoding ="utf8")
for x in range(len(texto_cifrado)):
        mensagem.write("%s\n" % texto_cifrado[x])    
mensagem.close()
