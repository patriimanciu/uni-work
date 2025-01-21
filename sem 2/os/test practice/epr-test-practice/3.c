#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

// P -> C0 + C1 + C2
// C0 -> C00 + C01 + C02
// C1 -> C10 + C11 + C12
// C2 -> C20 + C21 + C22

int main() {
    for (int i = 0; i < 3; i++) {
        int f = fork();
        if (f == 0) {
            // child
            printf("Child C%d: PID=%d, PPID=%d\n", i, getpid(), getppid());
            for (int j = 0; j < 3; j++) {
                int f2 = fork();
                if (f2 == 0) {
                    // grandchild
                    printf("Grandchild C%d%d: PID=%d, PPID=%d\n", i, j, getpid(), getppid());
                    exit(0);
                }
            }
            for (int j = 0; j < 3; j++)
                wait(0);
            exit(0);
        }
    }
    for (int i = 0; i < 3; i++)
        wait(0);

    return 0;
}
