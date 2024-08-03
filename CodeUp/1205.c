#include <stdio.h>
#include <math.h>

int main() {
  int a, b;
  float max = 0.0;
  scanf("%d %d", &a, &b); 
  float c[8] = {a+b, a-b, b-a, a*b, a/b, b/a, pow(a, b), pow(b, a)};
  for (int i = 0; i < 8; i++) {
    if (max < c[i]) {
      max = c[i];
    }
  }
  printf("%.6f\n", max);
  return 0;
}
