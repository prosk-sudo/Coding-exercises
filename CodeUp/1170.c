#include <stdio.h>

int main() {
  int grade, class, number;
  scanf("%d %d %d", &grade, &class, &number);
  printf("%d\n", grade * 1000 + class * 100 + number);
  return 0;
}
