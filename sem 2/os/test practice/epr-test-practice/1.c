#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
// Write a C program that creates n child processes. Each child process will print its PID and its parent PID. The parent process will print its PID and the PID of each of the child processes.

int main(int argc, char** argv) {
    int n = atoi(argv[1]);
    for (int i = 0; i < n; i++) {
        int f = fork();
        if (f == 0) {
            printf("Child PID: %d - Parent PID: %d\n", getpid(), getppid());
            break;
        }
        else if (f < 0) {
            printf("Error\n");
            return 1;
        }
    }
    return 0;
}
