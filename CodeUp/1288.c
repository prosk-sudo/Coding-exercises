#include <stdio.h>

int main() {
  int n, r;
  double res = 1;
  scanf("%d %d", &n, &r);

  if (n == r) { printf("1\n"); return 0; }
  else {
    for (r; r > 0; r--) {
      res *= n;
      res /= r;
      n--;
    }
  }
  printf("%.0f\n", res);
  return 0;
}
