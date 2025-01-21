#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char ** argv) {
    int a2b, b2a;
    a2b = open("a2b", O_WRONLY);
    b2a = open("b2a", O_RDONLY);

    FILE *file = fopen(argv[1], "r");
    int a, b;
    char c;
    while (0 < fscanf(file, "%d %d %c", &a, &b, &c)) {
        int res;
        // fscanf(file, "%d %d %c", &a, &b, &c);
        write(a2b, &a, sizeof(int));
        write(a2b, &b, sizeof(int));
        write(a2b, &c, sizeof(char));
        
        read(b2a, &res, sizeof(int));
        printf("%d %c %d = %d\n", a, c, b, res);
    }
    fclose(file);
    close(a2b);
    close(b2a);
    return 0;
}
