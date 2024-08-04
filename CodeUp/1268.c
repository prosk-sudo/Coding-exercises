#include <stdio.h>

int main() {
  int n, num, count = 0;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &num);
    if (num % 2 == 1) {
      count += 1;
    }
  }
  printf("%d\n", count);
  return 0;
}
