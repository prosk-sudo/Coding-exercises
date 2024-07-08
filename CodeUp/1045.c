#include <stdio.h>

int main() {
	long int a, b;
	scanf("%ld %ld", &a, &b);
	printf("%ld\n%ld\n%ld\n%ld\n%ld\n%.2f\n", a+b, a-b, a*b, a/b, a%b, (float)a/b);
	return 0;
}
