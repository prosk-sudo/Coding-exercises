#include <stdio.h>

int main() {
  int X, N, total = 0;
  scanf("%d\n%d", &X, &N);

  for (int i = 0; i < N; i++) {
    int a, b;
    scanf("%d %d", &a, &b);
    total += a * b;
  }

  printf("%s", (total == X) ? "Yes" : "No");
  return 0;
}
