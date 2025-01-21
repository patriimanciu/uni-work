#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
// Write a C program that creates a linear hierarchy of n processes (a parent process creates a child process, which in turn creates a child process, and so on).

int main(int argc, char** argv) {
    int n = 5;
    for (int i = 0; i < n; i++) {
        int f = fork();
        if (f == 0) {
            printf("Child PID: %d - Parent PID: %d\n", getpid(), getppid());
            wait(0);
        }
        else if (f > 0){
            exit(0);
        }
        else {
            printf("Error\n");
            exit(1);
        }
    }
    return 0;
}
