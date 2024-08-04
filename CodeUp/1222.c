#include <stdio.h>

int main() {
  int time, score_1, score_2;
  scanf("%d %d %d", &time, &score_1, &score_2);
  while (time < 90) {
    score_1 += 1;
    time += 5;
  }
  if (score_1 > score_2) {
    printf("win");
  } else if (score_1 < score_2) {
    printf("lose");
  } else {
    printf("same");
  }
  printf("\n");
  return 0;
}
