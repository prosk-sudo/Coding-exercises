#include <stdio.h>

int main() {
  char alp1, alp2;
  scanf("%c %c", &alp1, &alp2);
  for (alp1; alp1 <= alp2; alp1++) {
    printf("%c ", alp1);
  }
  printf("\n");
  return 0;
}
