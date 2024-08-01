#include <stdio.h>

int main() {
  int a, b;
  scanf("%d %d", &a, &b);

  if (a % 2 == 0) {
    printf("짝수");
  } else {
    printf("홀수");
  }

  printf("+");

  if (b % 2 == 0) {
    printf("짝수");
  } else {
    printf("홀수");
  }

  printf("=");

  if ((a % 2 == 0 && b % 2 == 0) || (a % 2 == 1 && b % 2 == 1)) {
    printf("짝수");
  } else {
    printf("홀수");
  }

  printf("\n");
  return 0;
}
