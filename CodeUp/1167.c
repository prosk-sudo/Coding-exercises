#include <stdio.h>

int main() {
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c);
  if ((a <= b) && (b <= c) && (a <= c)) {
    printf("%d\n", b);
  } else if ((a <= b) && (b >= c) && (a <= c)) {
    printf("%d\n", c);
  } else if ((a >= b) && (b <= c) && (a <= c)) { 
    printf("%d\n", a);
  } else if ((a <= b) && (b >= c) && (a >= c)) {
    printf("%d\n", a);
  } else if ((a >= b) && (b <= c) && (a >= c)) {
    printf("%d\n", c);
  } else if ((a >= b) && (b >= c) && (a >= c)) {
    printf("%d\n", b);
  }
  return 0;
}
