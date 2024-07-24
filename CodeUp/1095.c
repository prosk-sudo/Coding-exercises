#include <stdio.h>

int main() {
  int n, i;
  int min = 24;
  int a[10000] = {};
  scanf("%d", &n);
  for (i = 0; i < n; i++) {
    scanf("%d", &a[i]);
    if (a[i] < min) {
      min = a[i];
    } 
  }
  printf("%d\n", min);
  return 0;
}
