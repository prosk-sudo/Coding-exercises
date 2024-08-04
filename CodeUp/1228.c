#include <stdio.h>

int main() {
  double height, weight;
  scanf("%lf %lf", &height, &weight);
  double standard_weight = (height - 100) * 0.9;
  double obesity_index = (weight - standard_weight) * 100 / standard_weight;
  if (obesity_index <= 10) { printf("정상"); }
  else if (obesity_index <= 20) { printf("과체중"); }
  else { printf("비만"); }
  printf("\n");
  return 0;
}
