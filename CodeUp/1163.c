#include <stdio.h>

int main() {
  int y, m, d;
  scanf("%d %d %d", &y, &m, &d);
  printf("%s\n", (((y + m + d) / 100) % 2 == 0) ? "대박" : "그럭저럭");
  return 0;
} 
