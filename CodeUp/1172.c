#include <stdio.h>

int main() {
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c);
  if ((a <= b) && (b <= c) && (a <= c)) {
    printf("%d %d %d\n", a, b, c);
  } else if ((a <= b) && (b >= c) && (a <= c)) {
    printf("%d %d %d\n", a, c, b);
  } else if ((a >= b) && (b <= c) && (a <= c)) { 
    printf("%d %d %d\n", b, a, c);
  } else if ((a <= b) && (b >= c) && (a >= c)) {
    printf("%d %d %d\n", c, a, b);
  } else if ((a >= b) && (b <= c) && (a >= c)) {
    printf("%d %d %d\n", b, c, a);
  } else if ((a >= b) && (b >= c) && (a >= c)) {
    printf("%d %d %d\n", c, b, a);
  }
  return 0;
}
