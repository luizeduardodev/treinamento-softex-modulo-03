# Faça um algoritmo de ordenação utilizando o método insertion sort.
# Crie um método que execute as seguintes operações:

# - Tamanho do vetor: 30;
# - Utilize números ímpares;
# - Opere em ordem crescente.

# Realize essa atividade no WORD ou no Bloco de Notas, suba esse arquivo para algum repositório e compartilhe o link no campo ao lado para que outros desenvolvedores possam analisá-lo.

def insertionSort(array):
  for step in range(1, len(array)):
    key = array[step]
    j = step - 1

    while j >= 0 and key < array[j]:  
      array[j + 1] = array[j]
      j = j - 1
    
    array[j + 1] = key

vetor = [13, 39, 7, 11, 15, 17, 21, 23, 49, 25, 27, 29, 1, 31, 33, 5, 35, 37, 3, 59, 41, 43, 45, 9, 47, 51, 53, 55, 57, 19]
insertionSort(vetor)

print("Array em ordem crescente: " + str(vetor))