#include <stdio.h>

int main() {
  int a, b, answer = 0;
  scanf("%d %d", &a, &b);
  for (a; a <= b; a++) {
    if (a % 2 == 0) {
      printf("-%d", a);
      answer -= a;
    } else {
      printf("+%d", a);
      answer += a;
    }
  }
  printf("=%d\n", answer);
  return 0;
}
