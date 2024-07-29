#include <stdio.h>

int main() {
  char msg[31];
  fgets(msg, 31, stdin);
  printf("%s", msg);
  return 0;
}
