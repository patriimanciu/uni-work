#include <stdio.h>
#include <unistd.h>

int main(int argc, char** argv) {
    for(int i = 0; i < 3; i++) {
        printf("before %d %d\n", getpid(), getppid());
        fork();
        printf("after %d %d\n", getpid(), getppid());
    }
    return 0;
}
