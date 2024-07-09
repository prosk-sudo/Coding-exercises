#include <stdio.h>

int main() {
	int n;
		reload:
	scanf("%d", &n);
	if (n != 0) {
		printf("%d\n", n);
		goto reload;
	}
//	while (n != 0) {
//		printf("%d\n", n);
//		scanf("%d", &n);
//	}
	return 0;
}

