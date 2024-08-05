#include <stdio.h>

int main() {
  int n, count = 1;
  scanf("%d", &n);
  while (n / 10 != 0) {
    count++;
    n /= 10;
  }
  printf("%d\n", count);
  return 0;
}
