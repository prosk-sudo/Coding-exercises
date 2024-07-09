#include <stdio.h>

int main() {
	int num;
	scanf("%d", &num);
	switch (num) {
		case 3:
		case 4:
		case 5:
			printf("spring\n");
			break;
		case 6:
		case 7:
		case 8:
			printf("summer\n");
			break;
		case 9:
		case 10:
		case 11:
			printf("fall\n");
			break;
		case 12:
		default:
			printf("winter\n");
	}
	return 0;
}
