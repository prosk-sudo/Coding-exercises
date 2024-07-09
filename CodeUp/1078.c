#include <stdio.h>

int main() {
	int num, sum = 0;
	scanf("%d", &num);
	for (int i = 0; i <= num; i += 2) {
		sum += i;
	}
	printf("%d\n", sum);
	return 0;
}
