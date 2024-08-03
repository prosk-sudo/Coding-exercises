#include <stdio.h>

int main() {
  int a, b, c, max = 0;
  scanf("%d %d %d", &a, &b, &c);
  int length[3] = {a, b, c};
  for (int i = 0; i < 3; i++) {
    if (max < length[i]) {
      max = length[i]; 
    }
  }
  printf("%s\n", ((a + b + c) > (2 * max)) ? "yes" : "no");
  return 0;
}
