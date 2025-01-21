#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char ** argv) {
    int a2b, b2a;
    a2b = open("a2b", O_RDONLY);
    b2a = open("b2a", O_WRONLY);

    while (1) {
        int a, b, res;
        char c;
        read(a2b, &a, sizeof(int));
        read(a2b, &b, sizeof(int));
        read(a2b, &c, sizeof(char));
        if (c == '+') {
            res = a + b;
        } else if (c == '-') {
            res = a - b;
        } else if (c == '*') {
            res = a * b;
        } else if (c == '/') {
            res = a / b;
        } else {
            break;
        }
        write(b2a, &res, sizeof(int));
    }
    close(a2b);
    close(b2a);
    return 0;
}
