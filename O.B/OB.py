
def velasVector():
    print("Digite o vetor de velas")
    velas=[]
    while(len(velas) != 10):
        velas.append(input())

    return velas;

def mhiOriginal(velas[]):
    x=2;
    mh1 = 0
    mh2 = 0
    mh3 = 0
    mh4 = 0
    mh5 = 0
    for x in velas:
        if (velas[x] == 'a' and velas[x+1]=='a' or velas[x+2] =='a'):
                if(velas[x+3] =='b'):
                    mh1 = mh1+1
                if(velas[x+4] =='b'):
                    mh1 = mh2+1
                if(velas[x+5] =='b'):
                    mh1 = mh3+1
                if(velas[x+6] =='b'):
                    mh1 = mh4+1
                if(velas[x+7] =='b'):
                    mh1 = mh5+1

        if (velas[x] == 'b' and velas[x+1]=='b' or velas[x+2] =='b'):
                if(velas[x+3] =='a'):
                    mh1 = mh1+1
                if(velas[x+4] =='a'):
                    mh1 = mh2+1
                if(velas[x+5] =='a'):
                    mh1 = mh3+1
                if(velas[x+6] =='a'):
                    mh1 = mh4+1
                if(velas[x+7] =='a'):
                    mh1 = mh5+1
                
        x=x+3;
        
            

    mh1 = mh1*100/120;
    mh2 = mh1*100/120;
    mh3 = mh1*100/120;
    mh4 = mh1*100/120;
    mh5 = mh1*100/120;

    print("Taxa de acertos: MH1 = ",mh1,"  MH2 = ",mh2,"  MH3 = ",mh3,"  MH4 = ",mh4,"  MH5 = ",mh5);
    

while(1):
    velas = velasVector()
    print(velas);
    opcao= input("Selecione uma opcao: 1: MHI(Tradicional");
    if(opcao == 1):
        mhiOriginal(velas)
