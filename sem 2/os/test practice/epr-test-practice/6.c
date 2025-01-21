#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
// Create a C program that generates N random integers (N given at the command line). It then creates a child, sends the numbers via pipe. The child calculates the average and sends the result back.

int main(int argc, char** argv) {
    int n = atoi(argv[1]);
    int *numbers =(int*) malloc(n * sizeof(int));
    int sum = 0;
    float avg;
    int p2c[2], c2p[2];
    pipe(p2c); pipe(c2p);

    int f = fork();
    if (f == 0) {
        close(p2c[1]); close(c2p[0]);
        read(p2c[0], numbers, n * sizeof(int));
        for (int i = 0; i < n; i++) {
            sum += numbers[i];
        }
        avg = (float) sum / n;
        write(c2p[1], &avg, sizeof(float));
        close(p2c[0]); close(c2p[1]);
        free(numbers);
        exit(0);
    }
    
    srand(getpid());
    close(p2c[0]); close(c2p[1]);
    for (int i = 0; i < n; i++) {
        numbers[i] = rand() % 100;
    }
    write(p2c[1], numbers, n * sizeof(int));
    close(p2c[1]);
    wait(0);
    read(c2p[0], &avg, sizeof(float));
    printf("Average: %f\n", avg);
    close(c2p[0]);
    free(numbers);

    return 0;
}
