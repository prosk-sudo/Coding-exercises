#include <stdio.h>

int main() {
  double a, b;
  int percent;
  scanf("%lf", &a);
  scanf("%lf", &b);
  double tmp = a;
  for (int i = 0; i < (int)b; i++) {
    scanf("%d", &percent);
    tmp *= (1 + percent/100.0);
  }
  double profit = tmp - a;
  printf("%.0lf\n", profit);
  if (profit >= 0.5) {
    printf("good");
  } else if (profit <= -0.5) {
    printf("bad");
  } else {
    printf("same");
  }
  printf("\n");
  return 0;
}
