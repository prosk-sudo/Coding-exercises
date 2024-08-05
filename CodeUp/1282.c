#include <stdio.h>

int main() {
  int n, i = 1;
  scanf("%d", &n);
  for (i; i*i < n; i++);
  printf("%d %d\n", n - (i-1)*(i-1), i-1);
  return 0;
}
