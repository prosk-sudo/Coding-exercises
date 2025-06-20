#include <stdio.h>
#include <limits.h>

int main() {
  int n, min = INT_MAX, max = INT_MIN;
  scanf("%d", &n);

  for (; n > 0; n--) {
    int grade;
    scanf("%d", &grade);

    if (min > grade) { min = grade; }
    if (max < grade) { max = grade; }
  }

  printf("%d %d\n", max, min);
  return 0;
}
