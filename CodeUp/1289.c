#include <stdio.h>

int main() {
  int w, l, max = 0;
  for (int i = 0; i < 3; i++) {
    scanf("%d %d", &w, &l);
    if (max < (w * l)) { max = (w * l); }
  }
  printf("%d\n", max);
  return 0;
}
