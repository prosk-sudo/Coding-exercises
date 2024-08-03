#include <stdio.h>

int main() {
  int num;
  scanf("%d", &num);
  if (num == 11 || num == 12 || num == 13) {
    printf("%dth\n", num);
    return 0;
  }
  if (num % 10 == 1) {
    printf("%dst", num);
  } else if (num % 10 == 2) {
    printf("%dnd", num);
  } else if (num % 10 == 3) {
    printf("%drd", num);
  } else {
    printf("%dth", num);
  }
  printf("\n");
  return 0;
}
