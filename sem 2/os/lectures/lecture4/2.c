#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    int pid;
    pid = fork();
    printf("before\n");
    if (pid == 0) {
        printf("Child specific code pid =%d for fork return=%d.\n", getpid(), pid);
        exit(0);
    }
    printf("parent specific code child PID=%d.\n", pid);
    wait(0);
    return 0;
}
