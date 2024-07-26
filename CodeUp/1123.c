#include <stdio.h>

int main() {
  int celsius;
  scanf("%d", &celsius);
  printf("%.3f\n", (float)celsius * 9/5 + 32);
  return 0;
}
