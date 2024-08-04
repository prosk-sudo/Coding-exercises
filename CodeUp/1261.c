#include <stdio.h>

int main() {
  int num;
  for (int i = 0; i < 10; i++) {
    scanf("%d", &num);
    if (num % 5 == 0) {
      printf("%d\n", num);
      return 0;
    }
  }
  printf("%d\n", 0);
  return 0;
}
