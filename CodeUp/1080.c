#include <stdio.h>

int main() {
	int n, sum = 0, i = 1;
	scanf("%d", &n);
	for (; sum + i + 1 <= n; i++) {
		sum += i;
	}
	printf("%d\n", i);
	return 0;
}
