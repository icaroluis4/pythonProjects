import random



#Calcula o totiente do numero primo

def totient(number): 
    if(prime(number)):
        return number-1
    else:
        return False

    

#Verifica se um numero gerado é primo

def prime(n): 
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n%2 == 0 or n%3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n%i == 0 or n%(i+2) == 0):
           return False
        i+=6
    return True




#Gera um numero aleatório E, satisfazendo as condições

def generate_E(num): 
    def mdc(n1,n2):
        rest = 1
        while(n2 != 0):
            rest = n1%n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        e = random.randrange(2,num) 
        if(mdc(num,e) == 1):
            return e

        

#Gera um numero primo aleatório

def generate_prime(): 
    while True:
        x=random.randrange(1,100) # -> Define o intervalo em que se vai encontrar o numero primo
        if(prime(x)==True):
            return x

#Função modular entre dois números

def mod(a,b): 
    if(a<b):
        return a
    else:
        c=a%b
        return c





#Descriptografa um texto criptografado

def descifra(cifra,n,d):
    lista = []
    i = 0
    tamanho = len(cifra)
    # texto=cifra ^ d mod n
    while i < tamanho:
        result = int(cifra[i])**d
        texto = mod(result,n)
        letra = chr(texto)
        lista.append(letra)
        i += 1
    return lista



#Calcula a chave privada

def calculate_private_key(toti,e):
    d = 0
    while(mod(d*e,toti)!=1):
        d += 1
    return d




## MAIN
if __name__=='__main__':
    escolha = int(input('Escolha uma opção: \n 1:Gerar chaves privada e publica \n 2:Descriptografar texto \n'))
    if(escolha == 1):
            #text = input("Insert message: ")
            p = generate_prime() # generates random P
            q = generate_prime() # generates random Q
            n = p*q # compute N
            y = totient(p) # compute the totient of P
            x = totient(q) # compute the totient of Q
            totient_de_N = x*y # compute the totient of N
            e = generate_E(totient_de_N) # generate E
            public = [n,e]
            debug = [p,q]
            
            print (public)
            print (debug)
            #text_cipher = cipher(text,e,n)
            #print('Your encrypted message:', text_cipher)
            d = calculate_private_key(totient_de_N,e)
            print('Your private key is:', d)
            arquivo = open('chave_publica.txt', 'w' , encoding="utf8")
            for x in range(len(public)):
                arquivo.write("%d\n" % public[x])
            arquivo.close()
            private=[n,d]
            arquivo2 = open('chave_privada.txt', 'w' , encoding="utf8")
            for x in range(len(private)):
                arquivo2.write("%d\n" % private[x])
            arquivo2.close()
    if( escolha == 2):
        arq = open('mensagem_cifrada.txt','r')
        msg_cifrada = arq.readlines()
        print(" THIS " , msg_cifrada)
        arq.close()
        arq2 = open('chave_privada.txt','r')
        n = int(arq2.readline())
        d = int(arq2.readline())
        arq2.close()
        texto_decifrado = descifra(msg_cifrada,n,d)
        j = ''
        texto_decifrado = j.join(texto_decifrado)
        print('Seu texto decifrado é:',texto_decifrado)
