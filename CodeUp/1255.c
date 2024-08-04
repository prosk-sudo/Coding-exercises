#include <stdio.h>

int main() {
  double a, b;
  scanf("%lf %lf", &a, &b);
  for (a; a <= b; a += 0.01) {
    printf("%.2lf ", a);
  }
  printf("\n");
  return 0;
}
