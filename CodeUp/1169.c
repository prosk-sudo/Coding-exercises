#include <stdio.h>

int main() {
  int age;
  scanf("%d", &age);
  printf("%d %d\n", (2012 - age + 1) % 100, ((2012 - age + 1) / 100 == 19) ? 1 : 3);
  return 0;
}
