#include <stdio.h>

int main() {
  int num;
  scanf("%d", &num);

  int tmp = num, len = 0, pow10 = 1;

  while (tmp > 0) {
    len++;
    if (tmp >= 10) { pow10 *= 10; }
    tmp /= 10;
  }

  int digit_sum = 0;
  for (int i = 0; i < len; i++) {
    int digit = num / pow10;
    digit_sum += digit;

    num %= pow10;
    pow10 /= 10;
  }

  printf("%s\n", (digit_sum % 7 == 4) ? "suspect" : "citizen");
  return 0;
}
