#include <stdbool.h>
#include <stdio.h>
#include <string.h>

void sieve(int n, bool is_prime[]) {
  memset(is_prime, true, (n + 1) * sizeof(bool));
  is_prime[0] = false;
  is_prime[1] = false;
  for (int p = 2; p * p <= n; p++) {
    if (is_prime[p]) {
      for (int i = p * p; i <= n; i += p) {
        is_prime[i] = false;
      }
    }
  }
}

int main() {
  int num;
  scanf("%d", &num);

  if (num < 4) {
    printf("wrong number\n");
    return 0;
  }

  bool is_prime[num + 1];
  sieve(num, is_prime);

  for (int p = 2; p <= num / 2; p++) {
    if (is_prime[p] && num % p == 0) {
      int q = num / p;
      if (q >= 2 && q <= num && is_prime[q]) {
        printf("%d %d\n", p, q);
        return 0;
      }
    }
  }

  printf("wrong number\n");
  return 0;
}
