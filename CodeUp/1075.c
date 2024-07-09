#include <stdio.h>

int main() {
	int countdown;
	scanf("%d", &countdown);
	while (countdown > 0) {
		countdown--;
		printf("%d\n", countdown);
	}
	return 0;
}
