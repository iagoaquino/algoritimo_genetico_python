import random
matriz_distancia = []
cidade_1 = [0,4,5,6,1]
cidade_2 = [4,0,5,6,1]
cidade_3 = [5,5,0,6,1]
cidade_4 = [6,6,6,0,1]
cidade_5=  [1,1,1,1,0]
matriz_distancia.append(cidade_1)
matriz_distancia.append(cidade_2)
matriz_distancia.append(cidade_3)
matriz_distancia.append(cidade_4)
matriz_distancia.append(cidade_5)
print(matriz_distancia[0][1])
def listar_cidades(tam):
    lista_cidades = []
    for i in range(tam):
        lista_cidades.append(i+1)        
    return lista_cidades


def generate_populacao(quant,tam):
    populacao = []
    lista_cidades = listar_cidades(tam)
    i = 0
    while i != quant:
        individuo = []
        for j in range(len(lista_cidades)):
            individuo.append(lista_cidades[j])
        pos_de_troca_1 = random.randint(individuo[0],len(individuo)) - 1
        pos_de_troca_2 = random.randint(individuo[0],len(individuo)) - 1
        auxiliar = individuo[pos_de_troca_2]
        individuo[pos_de_troca_2] = individuo[pos_de_troca_1]
        individuo[pos_de_troca_1] = auxiliar
        populacao.append(individuo)
        individuo.append(individuo[0])
        i+= 1
    return populacao

def checar_faltando(individuo,tam):
    faltando = []
    for i in range(tam):
        if i+1 not in individuo:
            faltando.append(i+1)
    return faltando

def cross_over(individuo_1,individuo_2,tam):
    ponto = int(tam/3)
    filho_parte_1 = individuo_1[0:ponto+1]
    filho_parte_2 = individuo_2[ponto+1:len(individuo_2)-1]
    filho = []
    for i in range(len(filho_parte_1)):
        filho.append(filho_parte_1[i])
    for i in range(len(filho_parte_2)):
        if filho_parte_2[i] in filho:
            filho.append(-1)
        else:
            filho.append(filho_parte_2[i])
    faltando = checar_faltando(filho,tam)
    for i in range(len(filho)):
        if filho[i] == -1:
            filho[i] = faltando.pop()
    filho.append(filho[0])
    print(filho)

def aplicar_elitismo(populacao,tam):
    nova_populacao = []
    for i in range(tam):
        min_distancia = 10000000000
        pos_min = -1
        for j in range(len(populacao)):
            distancia = 0
            for k in range(len(populacao[j]) - 1):
                distancia += matriz_distancia[populacao[j][k] - 1][populacao[j][k+1] - 1]
            if distancia < min_distancia :
                min_distancia = distancia
                pos_min = j

        print("adcionado a nova populacao individuo:"+str(pos_min))
        print(populacao[pos_min])
        print("com a distancia de :"+str(min_distancia))
        nova_populacao.append(populacao.pop(pos_min))
    print(nova_populacao)
            

populacao = []
populacao = generate_populacao(10,5)
print(populacao)
cross_over(populacao[1],populacao[2],5)
aplicar_elitismo(populacao,5)
