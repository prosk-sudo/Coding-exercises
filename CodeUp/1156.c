#include <stdio.h>

int main() {
  int n;
  scanf("%d", &n);
  printf("%s\n", (n % 2 == 0) ? "even" : "odd");
  return 0;
}
