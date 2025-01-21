#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Implement a program that continuously reads two integers from the console, sends them to another process, gets back from that process their sum and product, and display them to the console. The program stops when the sum and the product are equal.

int main(int argc, char** argv) {
    int p2c[2], c2p[2], a, b, s, p;
    pipe(p2c);
    pipe(c2p);

    if (fork() == 0) {
        close(p2c[1]); close(c2p[0]);
        while (1) {
            if (read(p2c[0], &a, sizeof(int)) <= 0)
                break;
            if (read(p2c[0], &b, sizeof(int)) <= 0)
                break;
            s = a + b;
            p = a * b;
            write(c2p[1], &s, sizeof(int));
            write(c2p[1], &p, sizeof(int));
            if (s == p)
                break;
        }
        close(p2c[0]); close(c2p[1]);
        exit(0);
    }
    
    close(p2c[0]); close(c2p[1]);
    while(1) {
        printf("a = ");
        scanf("%d", &a);
        printf("b = ");
        scanf("%d", &b);
        write(p2c[1], &a, sizeof(int));
        write(p2c[1], &b, sizeof(int));
        if (read(c2p[0], &s, sizeof(int)) <= 0)
            break;
        if (read(c2p[0], &p, sizeof(int)) <= 0)
            break;
        printf(" a + b = %d\n a * b = %d\n", s, p);
        if (s == p)
            break;
    }
    close(p2c[1]); close(c2p[0]);
    wait(0);

    return 0;
}
