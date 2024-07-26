#include <stdio.h>

int main() {
  int i, j;
  int x = 1, y = 1; 
  int a[10][10]; // 10*10 grid

  // initialise the elements of the array to 0
  for (i = 0; i < 10; i++) {
    for (j = 0; j < 10; j++) {
      a[i][j] = 0;
    }
  }

  // take the input from the user and save the values in the array
  for (i = 0; i < 10; i++) {
    for (j = 0; j < 10; j++) {
      scanf("%d", &a[i][j]);
    }
  }

  while (1) {
    if (a[x][y] == 0) {
      a[x][y] = 9;
      y++;
    } else if (a[x][y] == 1) {
      x++;
      y--;
    } else {
      a[x][y] = 9;
      break;
    }
  }

  // print the resulting grid
  for (i = 0; i < 10; i++) {
    for (j = 0; j < 10; j++) {
      printf("%d ", a[i][j]);
    }
    printf("\n");
  }
  return 0;
}
