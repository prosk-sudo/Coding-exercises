#include <stdio.h>

int main() {
  int time, score;
  scanf("%d %d", &time, &score);
  while (time < 90) {
    score += 1;
    time += 5;
  }
  printf("%d\n", score);
  return 0;
} 
