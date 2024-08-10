#include <stdio.h>

int main() {
  int arr[5] = {};
  scanf("%d", &arr[0]);
  int min = arr[0], max = arr[0];
  for (int i = 1; i < 5; i++) {
    scanf("%d", &arr[i]);
    if (min > arr[i]) { min = arr[i]; }
    if (max < arr[i]) { max = arr[i]; }
  }
  printf("%d\n%d\n", max, min);
  return 0;
}
