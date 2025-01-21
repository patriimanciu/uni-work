#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    if (fork() == 0) {
        if (execlp("echo", "echo", "c.txt", NULL) == -1) {
            perror("something went bad\n");
            exit(0);
        }
    }
    printf("we echoed\n");
    wait(0);
    return 0;
}
