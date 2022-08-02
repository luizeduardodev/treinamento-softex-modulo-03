// Crie um vetor com ponteiros utilizando alocação dinâmica na linguagem C, que:

// - use a função realloc;
// - use a função sizeof;
// - que tenha tamanho 22 de vetor;
// - depois libere o bloco utilizando a função free.

// Realize essa atividade no WORD ou no Bloco de Notas, suba esse arquivo para algum repositório e compartilhe o link no campo ao lado para que outros desenvolvedores possam analisá-lo.

#include <stdio.h>
#include <stdlib.h>

int main(void){
  int i, a, *array;

  a = 5;
  array = (int *)malloc(a * sizeof(int));

  if (!array){
    printf("** Erro: Memória insuficiente **");
    exit;
  }

  for (i = 1; i <= a; i++){
    array[i] = i;
  }

  printf("Vetor com %d posições \n\n", a);
  for (i = 1; i <= a; i++){
    printf("Posicão: %d \n", array[i]);
  }

  printf("\n");

  a = 22;
  array = (int *) realloc(array, a * sizeof(int));

   if (!array){
    printf("** Erro: Memória insuficiente **");
    exit;
  }

  for(i = 1; i <= a; i++){
    array[i] = i;
  }

  printf("Vetor com %d posições \n\n", a);
  for (i = 1; i <= a; i++){
    printf("Posicão: %d \n", array[i]);
  }

  free(array);

  return 0;
}