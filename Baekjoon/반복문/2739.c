#include <stdio.h>

int main() {
  int n;
  scanf("%d", &n);
  printf(
    "%d * 1 = %d\n"
    "%d * 2 = %d\n"
    "%d * 3 = %d\n"
    "%d * 4 = %d\n"
    "%d * 5 = %d\n"
    "%d * 6 = %d\n"
    "%d * 7 = %d\n"
    "%d * 8 = %d\n"
    "%d * 9 = %d\n",
    n, n,
    n, n * 2,
    n, n * 3,
    n, n * 4,
    n, n * 5,
    n, n * 6,
    n, n * 7,
    n, n * 8,
    n, n * 9
  );
  return 0;
}
