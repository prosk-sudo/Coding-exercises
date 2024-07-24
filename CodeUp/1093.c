#include <stdio.h>

int main() {
  int n, i, t;
  int a[24] = {};
  scanf("%d", &n);
  for (i = 0; i < n; i++) {
    scanf("%d", &t);
    a[t] += 1;
  }
  for (i = 1; i <= 23; i++) {
    printf("%d ", a[i]);
  }
  printf("\n");
  return 0;
}
