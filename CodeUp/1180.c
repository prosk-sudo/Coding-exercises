#include <stdio.h>

int main() {
  int n, answer;
  scanf("%d", &n);
  answer = ((2 * (10 * (n % 10) + (n / 10))) % 100);
//  if (answer <= 50) {
//    printf("%d\n%s\n", answer, "GOOD");
//  } else {
//    printf("%d\n%s\n", answer, "OH MY GOD");
//  }
  printf("%d\n%s\n", answer, (answer <= 50) ? "GOOD" : "OH MY GOD");
  return 0;
}
