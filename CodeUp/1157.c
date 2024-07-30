#include <stdio.h>

int main() {
  float n;
  scanf("%f", &n);
  printf("%s\n", (n >= 50 && n <= 60) ? "win" : "lose");
  return 0;
}
