#include <stdio.h>

int gcd(int u, int v) {
  int shift;

  if (u == 0 || v == 0) { return u | v; }

  for (shift = 0; ((u | v) & 1) == 0; shift++) {
    u >>= 1;
    v >>= 1;
  }

  while ((u & 1) == 0) { u >>= 1; }

  do {
    while ((v & 1) == 0) { v >>= 1; }

    if (u < v) {
      v -= u;
    } else {
      int diff = u - v;
      u = v;
      v = diff;
    }
    v >>= 1;
  } while (v != 0);

  return u << shift;
}

int gcd3(int a, int b, int c) {
  return gcd(gcd(a, b), c);
}

int main() {
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c);

  int res = gcd3(a, b, c);

  printf("%d\n", res);
  return 0;
}
