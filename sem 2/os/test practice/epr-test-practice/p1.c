#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char** argv) {
    int a[4] = {1, 2, 3, 4};
    int pid, p[2]; // p is gonna be the pipe
    
    pipe(p);
    pid = fork();
    if (pid == 0) {
        close(p[0]); // close the read end
        a[2] += a[3];
        write(p[1], &a[2], sizeof(int));
        close(p[1]);
        exit(0);
    }
    close(p[1]); // close the write end
    a[0] += a[1];
    read(p[0], &a[2], sizeof(int));
    close(p[0]);
    wait(0);
    a[0] += a[2];
    printf("%d\n", a[0]); // should print 10
    return 0;
}
