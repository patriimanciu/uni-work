#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    for(int i=0; i<3; i++) {
        if(fork() > 0) {
            printf("Parent i = %d on wait 1.\n", i);
            wait(0);
            printf("Parent i = %d on wait 2.\n", i);
            wait(0);
            exit(0);
        }
        printf("Child i = %d.\n", i);
    }
}
