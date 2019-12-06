import sys
import os
import pdb
from random import *
from copy import deepcopy
import item as itens
import bin as bins
import decoder as Dec

QTD_ITENS = 0
TAM_MAX_PACOTE = 0
ITENS = []
NUM_REST = 0
TAM_POPULACAO = 100
TAXA_ELITE = 0.30
TAXA_MUTACAO = 0.10


def lerArquivo():

    global QTD_ITENS
    global TAM_MAX_PACOTE
    global ITENS

    #leitura do arquivo passado como primeiro parametro
    arquivo = open('Istanze/'+sys.argv[1], 'r')
    info = arquivo.readline()
    graph = arquivo.readlines()
    arquivo.close()
    
    #armazenamento das informacoes
    info = info.split( )

    QTD_ITENS = info[0]
    TAM_MAX_PACOTE = info[1]
    
    #preenchimento dos dados dos itens
    for i in graph :
        token = i.split()
        if token :
            aux = itens.Item( token[0], token[1], token[2:])
            ITENS.append(aux)
    print('italo')        

def GeraPopulacao(popSize):
	
    global QTD_ITENS
    
    solucao = []
    populacao = []

    for i in range(popSize): 
        for j in range (int(QTD_ITENS)):
            solucao.append(uniform(0,1))
        populacao.append(deepcopy(solucao)) 		
        solucao*= 0		

    return populacao

def crossover(pA,pB):
    
    global QTD_ITENS
    pfilho = []
    
    for i in range(int(QTD_ITENS)):
        
        num = uniform(0,1)
        if num <= 0.7:
            pfilho.append(pA[0][i])
        else:
            pfilho.append(pB[0][i])
    
    return pfilho        

def dividePop(populacao):
    
    popE = []
    popNe = []
    global TAM_POPULACAO
    global TAXA_ELITE

    for i in range(len(populacao)):
        if(len(popE) <= TAXA_ELITE * TAM_POPULACAO):

            popE.append(populacao[i])
        else:
            popNe.append(populacao[i])          
    return popE,popNe

def saida(nomeArq, instancia, parametro, objetivo):

    dir =  f'{nomeArq}.out'

    if os.path.isfile(f'{dir}'):
         opcao = 'a' 
    else:
        opcao = 'w'
        with open(dir,opcao) as arq :
                arq.writelines(f'Instancia\tParametro\tObjetivo\n')
        opcao = 'a'

    with open(dir,opcao) as arq :
        arq.write(f'{instancia}\t{parametro}\t{objetivo}\n')  

def main():
    
    global TAM_POPULACAO
    global TAXA_MUTACAO
    maxInter = 0
    

    lerArquivo()
    
    #gera a populacao inicial 
    populacao = GeraPopulacao(TAM_POPULACAO)    

    while maxInter <= 100:
        #para cada um dos individos da populacao gera uma solucao e retorna o fitness
        proxPop = []
        filhos = []
        for i in populacao:
           
            decodificador = Dec.Decoder(ITENS,i,TAM_MAX_PACOTE)
            #solucao = decodificador.geraSolucao()
            #fitness = len(solucao)
            fitness = decodificador.solucao2()
            i.append(fitness)
            
        #ordena a populacao inicial    
        populacao.sort(key = lambda x: x[int(QTD_ITENS)])        
       
        
        melhor = populacao[0][int(QTD_ITENS)] 
        print("Melhor:",melhor)
        #particiona populacao em popE e popNe#dividir a populacao em elite e nao elite
        popE,popNe = dividePop(populacao)
        #print("fora",popE[0][0])

        #retira o fitness do fim de  cada solucao para nao atrapalhar
        for i in popE: 
            i.pop()

            
        #proxima polpulacao recebe todos os individuos de elite da polpulacao anterior.    
        proxPop += popE
    
        for i in range(TAM_POPULACAO  - (int(TAXA_ELITE * TAM_POPULACAO))-1):#gera n filhos 

            paiA = sample(popE,1)#sorteia da populacao de elite
            paiB = sample(popNe,1)#sorteia da populacao nao elite

            filhos.append(crossover(paiA,paiB))
        
        proxPop += filhos
        qtdmut = int(TAXA_MUTACAO * TAM_POPULACAO)
        proxPop = proxPop[:TAM_POPULACAO - qtdmut]
        popMut = GeraPopulacao(qtdmut)#gera uma quantida de individuos mutantes, de acordo com a taxa de mutação.
        proxPop += popMut#proxima poulacao recebe os individuos mutantes.
         
        maxInter +=1
        
        populacao = proxPop 

    parametros = ('Tam Pop: ',str(TAM_POPULACAO),'Taxa Elite: ',str(TAXA_ELITE),'Taxa Mut: ',str(TAXA_MUTACAO),'Qtd Geracoes: ',maxInter-1)    
    instancia = sys.argv[1][0:]
    saida(sys.argv[1],instancia,parametros,melhor)    
main()
