#include <stdio.h>

int main() {
  int a, b, sum = 0;
  scanf("%d %d", &a, &b);
  if (a % 3 != 0) { a += (-(a % 3) + 3); }
  for (a; a <= b; a += 3) {
    sum += a;
  }
  printf("%d\n", sum);
  return 0;
}
