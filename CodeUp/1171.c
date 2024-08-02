#include <stdio.h>

int main() {
  int grade, class, number;
  scanf("%d %d %d", &grade, &class, &number);
  printf("%d\n", grade * 100000 + class * 1000 + number);
  return 0;
}
