#include <stdio.h>

int main() {
  int k, h, sum = 0;
  scanf("%d %d", &k, &h);
  if (k % 2 == 0) {
    sum += k * 5;
  } else {
    sum += (k + 1) / 2;
  }

  if (h % 2 == 0) {
    sum += h * 5;
  } else {
    sum += (h + 1) / 2;
  }
  printf("%d\n", sum);
  return 0;
}
