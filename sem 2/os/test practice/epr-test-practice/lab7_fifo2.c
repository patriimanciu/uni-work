#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char** argv) {
    int a2b, b2a, a, b, s, p;
    a2b = open("a2b", O_RDONLY);
    b2a = open("b2a", O_WRONLY);

    while(1) {
        if (read(a2b, &a, sizeof(int)) <= 0)
            break;
        if (read(a2b, &b, sizeof(int)) <= 0)
            break;
        s = a + b;
        p = a * b;
        write(b2a, &s, sizeof(int));
        write(b2a, &p, sizeof(int));
        if (p == s)
            break;
    }
    close(a2b);
    close(b2a);
    return 0;
}
