#include <stdio.h>

int main() {
  char name[20];
  int age;
  char department_code;
  float security_key;

  scanf("%s", name);
  scanf("%d", &age);
  getchar();
  scanf("%c", &department_code);
  scanf("%f", &security_key);

  printf("%s\n", name);
  printf("%d\n", age);
  printf("%c\n", department_code);
  printf("%g\n", security_key);
  
  return 0;
}
