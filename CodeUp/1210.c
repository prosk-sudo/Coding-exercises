#include <stdio.h>

int main() {
  int menu1, menu2, calorie = 0;
  scanf("%d %d", &menu1, &menu2);
  if (menu1 == 1) { calorie += 400; }
  else if (menu1 == 2) { calorie += 340; }
  else if (menu1 == 3) { calorie += 170; }
  else if (menu1 == 4) { calorie += 100; }
  else { calorie += 70; }
 
  if (menu2 == 1) { calorie += 400; }
  else if (menu2 == 2) { calorie += 340; }
  else if (menu2 == 3) { calorie += 170; }
  else if (menu2 == 4) { calorie += 100; }
  else { calorie += 70; }

  printf("%s\n", (calorie > 500) ? "angry" : "no angry");
  return 0;
}
