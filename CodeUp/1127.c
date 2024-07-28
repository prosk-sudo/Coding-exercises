#include <stdio.h>

int main() {
  float a;
  int b;
  float result = 0.0;
  for (int i = 0; i < 3; i++) {
    scanf("%f %d", &a, &b);
    result += (a * b);
  }
  printf("%.1f\n", result);
  return 0;
}
