#include <stdio.h>

int main() {
  int n;
  scanf("%d", &n);
  if (!n) {
    printf("%d\n", 0);
    return 0;
  }
  printf("%s\n", (n > 0) ? "양수" : "음수");
  return 0;
}
