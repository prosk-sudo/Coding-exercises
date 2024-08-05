#include <stdio.h>

int main() {
  int n;
  scanf("%d", &n);
  if (n == 2) { printf("prime"); }
  else if (n == 3) { printf("prime"); }
  else {
    for (int i = 2; i < n; i++) {
      if (n % i == 0) { printf("not prime\n"); return 0; }
    }
    printf("prime");
  }
  printf("\n");
  return 0;
}
