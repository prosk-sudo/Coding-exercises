#include <stdio.h>

int main() {
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c);
  printf("%s\n", (a > 170 && b > 170 && c > 170) ? "PASS" : "CRASH");
  return 0;
}
