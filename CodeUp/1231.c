#include <stdio.h>

int main() {
  double a, b;
  char oper;
  scanf("%lf%c%lf", &a, &oper, &b);
  switch (oper) {
    case '+':
      printf("%.0lf", a + b);
      break;
    case '-':
      printf("%.0lf", a - b);
      break;
    case '*':
      printf("%.0lf", a * b);
      break;
    case '/':
      printf("%.2lf", a / b);
      break;
    default:
      printf("Unknown operator");
      break;
  }
  printf("\n");
  return 0;
}
