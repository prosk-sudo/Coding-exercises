#include <stdio.h>

int main(void) {
  int N;
  scanf("%d", &N);

  int rep = N / 4;
  int bufsize = rep * 5 + 4;

  char msg[bufsize];
  int idx = 0;

  for (int i = 0; i < rep; i++) {
    msg[idx++] = 'l';
    msg[idx++] = 'o';
    msg[idx++] = 'n';
    msg[idx++] = 'g';
    msg[idx++] = ' ';
  }
  msg[idx++] = 'i';
  msg[idx++] = 'n';
  msg[idx++] = 't';
  msg[idx] = '\0';

  printf("%s\n", msg);
  return 0;
}
