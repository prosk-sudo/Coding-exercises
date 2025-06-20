#include <stdio.h>
#include <string.h>

int main() {
  int MAX_MSG_LEN = 100;
  int SHIFT = 3;
  char msg[MAX_MSG_LEN];
  char res[MAX_MSG_LEN];
  fgets(msg, MAX_MSG_LEN, stdin);

  size_t msg_len = strlen(msg) - 1;
  for (int i = 0; i < msg_len; i++) {
    if (msg[i] == ' ') { res[i] = ' '; }
    else { res[i] = 'a' + ((msg[i] - 'a') + SHIFT) % 26; }
  }
  res[msg_len] = '\0';

  fputs(res, stdout);
  fputc('\n', stdout);
  return 0;
}

// Input:
// never trust brutus
//
// Output on my machine:
// qhyhu wuxvw euxwxv
//
// Output on codeup:
// qhyhu wuxvw euxwx

// Why does this happen?
// fgets() and strlen() problem?
//
// Personal guess.. probably because CodeUp input file has no trailing newline, so fgets stores "never trust brutus" without the newline at the end?
//
// My guess was correct:
//
// ➜  CodeUp git:(main) ✗ printf "never trust brutus" > 1294.in
// ➜  CodeUp git:(main) ✗ ./1294 < 1294.in
// qhyhu wuxvw euxwx
// ➜  CodeUp git:(main) ✗ od -c 1294.in
// 0000000   n   e   v   e   r       t   r   u   s   t       b   r  
//  u   t
// 0000020   u   s
// 0000022
//
// printf instead of echo, since echo also adds \n at the end.
