#include <stdio.h>

int main() {
  int num, result;
  char op;
  scanf("%d", &result);
  while (1) {
    scanf("%c", &op);
    if (op == '=') { break; }
    scanf("%d", &num);
    switch (op) {
      case '+':
        result += num;
        break;
      case '-':
        result -= num;
        break;
      case '*':
        result *= num;
        break;
      case '/':
        result /= num;
        break;
      default:
        return 1;
    }
  }
  printf("%d\n", result);
  return 0;
}
