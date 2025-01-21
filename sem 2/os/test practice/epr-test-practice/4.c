#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/wait.h>
#include <string.h>

int main(int argc, char **argv) {
    int status;
    for (int i = 0; i < argc; i++ ){
        int f = fork();
        if (f == 0) {
            if (execlp(argv[i], argv[i], NULL) == -1) {
                fprintf(stderr, "Error: Failed to execute \"%s\": %s\n", argv[i], strerror(errno));
                exit(0);
            }
        }
        wait(&status);
        if (WEXITSTATUS(status) != 0) {
            fprintf(stderr, "Error: \"%s\" failed with exit code %d\n", argv[i], WEXITSTATUS(status));
        }
    }

    return 0;
}
