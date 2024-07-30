#include <stdio.h>

int main() {
  int n;
  scanf("%d", &n);
  printf("%s\n", (n % 7 == 0) ? "multiple" : "not multiple");
  return 0;
}
