#include <stdio.h>

int main() {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	printf("%d\n", ((a < b) ? a : b) < c ? ((a < b) ? a : b) : c);
	return 0;
}
