#include <stdio.h>

int main() {
  int n;
  scanf("%d", &n);
  printf("%s\n", (n < 10) ? "small" : "big");
  return 0;
}
