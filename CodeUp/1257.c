#include <stdio.h>

int main() {
  int a, b;
  scanf("%d %d", &a, &b);
  if (a % 2 == 0) {
    a += 1;
  }
  for (a; a <= b; a += 2) {
    printf("%d ", a);
  }
  printf("\n");
  return 0;
}
