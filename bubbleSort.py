# Construa um algoritmo de ordenação, utilizando o método bubble sort estudado. (Lembre-se que se trata de uma série de instruções que devem ser seguidas passo a passo).
# Para isso, você deve criar um método em que o tamanho do vetor seja dez e deve estar em ordem crescente.

# O vetor deverá:
# - comparar seus elementos dois a dois adjacentes;
# - se os elementos não estiverem em ordem, então ordenar;
# - senão, avançar para o próximo par;
# - repetir a operação até que nenhuma troca possa ser feita no vetor inteiro.

# Realize essa atividade no WORD ou no Bloco de Notas, suba esse arquivo para algum repositório e compartilhe o link no campo ao lado para que outros desenvolvedores possam analisá-lo.

vetor = [24, 26, 21, 27, 22, 33, 1, 80, 10, 11]

def bubble_sort(vetor):
    elementos = len(vetor) - 1 #9
    ordenado = False

    while not ordenado: #Enquanto for verdadeiro
        ordenado = True
        for i in range(elementos):
            if (vetor[i] > vetor[i+1]):
              vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
              ordenado = False        
    return vetor

resultado = bubble_sort(vetor)
print(resultado)