#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

//4. Să se scrie un program C care creează un proces copil cu care comunică prin pipe.
//Procesul părinte citeşte de la tastatură două numere întregi pe care le trimite prin pipe procesului copil,
//iar procesul copil returnează prin pipe suma lor.


int main(int argc, char** argv) {
    int c2p[2], p2c[2];
    pipe(c2p);
    pipe(p2c);

    int f = fork();
    if (f == 0) {
        close(c2p[0]); close(p2c[1]);
        int a, b;
        read(p2c[0], &a, sizeof(int));
        read(p2c[0], &b, sizeof(int));

        int sum;
        sum = a + b;
        write(c2p[1], &sum, sizeof(int));
        close(p2c[0]); close(c2p[1]);
        exit(0);
    }
    close(c2p[1]); close(p2c[0]);
    int a, b;
    printf("> "); scanf("%d %d", &a, &b);
    write(p2c[1], &a, sizeof(int));
    write(p2c[1], &b, sizeof(int));
    wait(0);
    int sum;
    read(c2p[0], &sum, sizeof(int));
    close(p2c[1]); close(c2p[0]);
    printf("Sum: %d\n", sum);

    return 0;
}
