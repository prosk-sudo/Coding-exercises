#include <stdio.h>

int main() {
  int n, count = 0;
  scanf("%d", &n);
  for (int i = 1; i <= n; i += 10) {
    count += 1;
  }
  printf("%d\n", count);
  return 0;
}
