#include <stdio.h>

int main() {
  int hour, minute;
  scanf("%d %d", &hour, &minute);
  if (hour == 0 && minute < 30) {
    printf("%d %d\n", 23, minute + 30);
  } else if (minute < 30) {
    printf("%d %d\n", hour - 1, minute + 30);
  } else {
    printf("%d %d\n", hour, minute - 30);
  }
  return 0;
}
