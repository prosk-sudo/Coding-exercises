#include <stdio.h>

int main() {
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c);
  int height[3] = {a, b, c};
  for (int i = 0; i < 3; i++) {
    if (height[i] <= 170) {
      printf("CRASH %d\n", height[i]);
      return 0;
    }
  }
  printf("PASS\n");
  return 0;
}
