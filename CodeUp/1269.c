#include <stdio.h>

int main() {
  int a, b, c, n;
  scanf("%d %d %d %d", &a, &b, &c, &n);
  for (int i = 1; i < n; i++) {
    a = a * b + c;
  }
  printf("%d\n", a);
  return 0;
}
