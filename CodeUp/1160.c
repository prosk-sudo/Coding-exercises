#include <stdio.h>

int main() {
  int day;
  scanf("%d", &day);
  printf("%s\n", day % 2 == 0 ? "enjoy" : "oh my god");
  return 0;
}
