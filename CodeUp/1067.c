#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	if (n < 0) {
		printf("minus\n");

		if (n % 2 == 0) {
			printf("even\n");
		} else {
			printf("odd\n");
		}

	} else {
		printf("plus\n");

		if (n % 2 == 0) {
			printf("even\n");
		} else {
			printf("odd\n");
		}
	}
	return 0;
}
