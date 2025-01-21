#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>
// Write a C program that creates two child processes. The two child processes will alternate sending random integers between 1 and 10 (inclusively) to one another until one of them sends the number 10. Print messages as the numbers are sent.


int main(int argc, char** argv) {
    srand(getpid());
    int a2b[2], b2a[2];
    int num;
    pipe(a2b); pipe(b2a);
    int p1 = fork();
    if (p1 == 0) {
        // child p1
        close(a2b[0]); close(b2a[1]);
        do {
            num = rand() % 10 + 1;
            write(a2b[1], &num, sizeof(int));
            printf("Child 1 sent %d\n", num);
            read(b2a[0], &num, sizeof(int));
            printf("Child 1 received %d\n", num);
        } while (num != 10);
        close(a2b[1]); close(b2a[0]);
        exit(0);
    }
    else {
        int p2 = fork();
        if (p2 == 0) {
            // child p2

            close(a2b[1]); close(b2a[0]);
            do {
                read(a2b[0], &num, sizeof(int));
                printf("Child 2 received %d\n", num);
                num = rand() % 10 + 1;
                num = rand() % 10 + 1;
                printf("Child 2 sent %d\n", num);
                write(b2a[1], &num, sizeof(int));
            } while (num != 10);
            close(a2b[0]); close(b2a[1]);
            exit(0);
        }
        else {
            // parent
            close(a2b[0]); close(a2b[1]);
            close(b2a[0]); close(b2a[1]);
            wait(0);
            wait(0);
        }
    }
    return 0;
}
