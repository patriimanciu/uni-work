#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

int main(int argc, char** argv) {
    int f, n;
    char *s = "Hello!";

    f = open("w2r", O_WRONLY);
    n = strlen(s) + 1;

    write(f, &n, sizeof(int));
    write(f, s, n);
    close(f);
    return 0;
} 
