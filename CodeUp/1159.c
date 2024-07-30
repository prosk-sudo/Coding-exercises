#include <stdio.h>

int main() {
  int n;
  scanf("%d", &n);
  printf("%s\n", (n >= 50 && n <= 70) || (n % 6 == 0) ? "win" : "lose");
  return 0;
}
