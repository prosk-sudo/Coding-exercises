#include <stdio.h>

int main() {
  int birthdate, code;
  scanf("%d %d", &birthdate, &code);
  if (code == 1 || code == 2) {
    printf("%d\n", 2012 - (1900 + (birthdate / 10000)) + 1);
  } else {
    printf("%d\n", 2012 - (2000 + (birthdate / 10000)) + 1);
  }
  return 0;
}
