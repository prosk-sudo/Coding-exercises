#include <stdio.h>

int main() {
  int h, m, h_answer, m_answer;
  scanf("%d %d", &h, &m);
  h_answer = h * 60 + m;
  h_answer -= 30;
  h_answer = 24 * 60 + h_answer;
  h_answer %= (24 * 60);
  h_answer /= 60;
  m_answer = (m + 30) % 60;
  printf("%d %d\n", h_answer, m_answer);
  return 0;
}
