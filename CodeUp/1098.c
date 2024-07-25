#include <stdio.h>

int main() {
  int h, w;
  scanf("%d %d", &h, &w);
  int n;
  int l, d, x, y;
  int a[h+1][w+1];
  for (int i = 1; i <= h; i++) {
    for (int j = 1; j <= w; j++) {
      a[i][j] = 0;
    }
  }
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%d %d %d %d", &l, &d, &x, &y);
    if (d) {
      for (int j = 0; j < l; j++) {
        a[x+j][y] = 1;
      }
    } else {
      for (int j = 0; j < l; j++) {
        a[x][y+j] = 1;
      }
    }
  }
  for (int i = 1; i <= h; i++) {
    for (int j = 1; j <= w; j++) {
      printf("%d ", a[i][j]);
    }
    printf("\n");
  }
  return 0;
}
