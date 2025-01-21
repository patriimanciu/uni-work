#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char** argv) {
    int a2b, b2a, a, b, s, p;
    a2b = open("a2b", O_WRONLY);
    b2a = open("b2a", O_RDONLY);

    while(1) {
        printf("a = "); scanf("%d", &a);
        printf("b = "); scanf("%d", &b);
        write(a2b, &a, sizeof(int));
        write(a2b, &b, sizeof(int));
        if (read(b2a, &s, sizeof(int)) <= 0)
            break;
        if (read(b2a, &p, sizeof(int)) <= 0)
            break;
        printf("a + b = %d\na * b = %d\n", s, p);
        if (p == s)
            break;
    }
    close(a2b);
    close(b2a);
    return 0;
}
