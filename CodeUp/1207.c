#include <stdio.h>

int main() {
  int a, b, c, d;
  scanf("%d %d %d %d", &a, &b, &c, &d);
  int sum = a + b + c + d;
  if (sum == 0) {
    printf("모");
  } else if (sum == 1) {
    printf("도");
  } else if (sum == 2) {
    printf("개");
  } else if (sum == 3) {
    printf("걸");
  } else {
    printf("윷");
  }
  printf("\n");
  return 0;
}
