#include <stdio.h>

int main() {
	int n, sum = 0;
	scanf("%d", &n);
	for (int i = 1;;i++) {
		sum += i;
		if (sum >= n) {
			break;
		}
	}
	printf("%d\n", sum);
	return 0;
}
