#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
  int c = 0, h = 0;
  int answer = 0;
  int i = 0;
  char a[8] = {};

  scanf("%s", a);

  i++;
  while (i < strlen(a) && isdigit(a[i])) {
    c = c * 10 + (a[i] - 48);
    i++;
  }

  if (c == 0) { c = 1; }

  if (i < strlen(a) && a[i] == 'H') {
    i++;
    while (i < strlen(a) && isdigit(a[i])) {
      h = h * 10 + (a[i] - 48);
      i++;
    }
  }

  if (h == 0) { h = 1; }

  int molecular_mass = (12 * c) + h;

  printf("%d\n", molecular_mass);
  return 0;
}
