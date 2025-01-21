#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// 2. Să se scrie un program C care creează un proces copil cu care comunică prin pipe.
// Procesul părinte citeşte de la tastatură un număr natural şi îl trimite prin pipe procesului copil,
// iar procesul copil verifică şi afişează dacă acest număr este prim.

int main(int argc, char** argv) {
    int c2p[2], p2c[2];
    pipe(c2p);
    pipe(p2c);

    int f = fork();
    if (f == 0) {
        close(c2p[0]); close(p2c[1]);
        int n;
        read(p2c[0], &n, sizeof(int));
        
        int isPrime = 1;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                isPrime = 0;
                break;
            }
        }
        write(c2p[1], &isPrime, sizeof(int));
        close(p2c[0]); close(c2p[1]);
        exit(0);
    }
    close(c2p[1]); close(p2c[0]);
    int n;
    printf("Enter a number: "); scanf("%d", &n);
    write(p2c[1], &n, sizeof(int));
    int isPrime;
    wait(0);
    read(c2p[0], &isPrime, sizeof(int));
    close(p2c[1]); close(c2p[0]);
    if (isPrime) {
        printf("The number is prime\n");
    } else {
        printf("The number is not prime\n");
    }

    return 0;
}
