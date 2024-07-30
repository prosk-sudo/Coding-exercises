#include <stdio.h>

int main() {
  int n;
  char msg[5] = "small";
  scanf("%d", &n);
  if (n < 10) {
    printf("%s\n", msg);
  }
  return 0;
}
