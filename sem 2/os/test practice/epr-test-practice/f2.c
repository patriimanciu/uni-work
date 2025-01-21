#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

int main(int argc, char** argv) {
    int f, n;
    char *s;

    f = open("w2r", O_RDONLY);
    read(f, &n, sizeof(int));
    s = (char*)malloc(n);
    read(f, s, n);
    free(s);
    close(f);
    return 0;
} 
