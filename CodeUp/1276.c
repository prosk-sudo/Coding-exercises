#include <stdio.h>

int main() {
  int n, answer = 1;
  scanf("%d", &n);
  for (n; n > 1; n--) {
    answer *= n;
  }
  printf("%d\n", answer);
  return 0;
}
