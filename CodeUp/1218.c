#include <stdio.h>

void sort(int *a, int *b, int *c) {
    int temp;
    if (*a > *b) {
        temp = *a;
        *a = *b;
        *b = temp;
    }
    if (*b > *c) {
        temp = *b;
        *b = *c;
        *c = temp;
    }
    if (*a > *b) {
        temp = *a;
        *a = *b;
        *b = temp;
    }
}

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    sort(&a, &b, &c);

    if (a + b <= c) {
        printf("삼각형아님\n");
        return 0;
    }

    if (a == b && b == c) {
        printf("정삼각형\n");
        return 0;
    }

    if (a == b || b == c || a == c) {
        printf("이등변삼각형\n");
        return 0;
    }

    if (a * a + b * b == c * c) {
        printf("직각삼각형\n");
        return 0;
    }

    printf("삼각형\n");
    return 0;
}
