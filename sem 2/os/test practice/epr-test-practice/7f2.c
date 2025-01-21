#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

//Write two C programs that communicate via fifo. The two processes will alternate sending random integers between 1 and 10 (inclusively) to one another until one of them sends the number 10. Print messages as the numbers are sent. One of the two processes must be responsible for creating and deleting the fifos.

int main(int argc, char** argv) {
    int a2b, b2a;
    a2b = open("a2b", O_RDONLY);
    b2a = open("b2a", O_WRONLY);
    int num;
    srand(getpid());
    do {
        read(a2b, &num, sizeof(int));
        printf("B recieved %d\n", num);
        num = rand() % 10 + 1;
        printf("B sent %d\n", num);
        write(b2a, &num, sizeof(int));
        if (num == 10) {
            break;
        }
    } while (num != 10);
    close(a2b);
    close(b2a);
    return 0;
}
