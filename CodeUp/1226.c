#include <stdio.h>

int main() {
  int n1, n2, n3, n4, n5, n6, bonus;
  int a, b, c, d, e, f;
  int count = 0, bonus_count = 0;
  scanf("%d %d %d %d %d %d %d", &n1, &n2, &n3, &n4, &n5, &n6, &bonus);
  scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);
  int answer[6] = {n1, n2, n3, n4, n5, n6};
  int attempt[6] = {a, b, c, d, e, f};

  for (int i = 0; i < 6; i++) {
    if (attempt[i] == bonus) { bonus_count++; }
    for (int j = 0; j < 6; j++) {
      if (attempt[i] == answer[j]) { count++; }
    }
  }

  if (count <= 2) { printf("%d\n", 0); }
  else if (count == 3) { printf("%d\n", 5); }
  else if (count == 4) { printf("%d\n", 4); }
  else if (count == 5 && bonus_count == 0) { printf("%d\n", 3); }
  else if (count == 5 && bonus_count == 1) { printf("%d\n", 2); }
  else { printf("%d\n", 1); }
  return 0;
}
