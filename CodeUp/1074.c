#include <stdio.h>

int main() {
	int countdown;
	scanf("%d", &countdown);
	while (countdown > 0) {
		printf("%d\n", countdown);
		countdown--;
	}
	return 0;
}
