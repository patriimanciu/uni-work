#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <string.h>

// recieves SIGINT signal and asks user if they want to stop the program

void stop(int sgn) {
    char s[32];
    printf("Do you want to stop the program? (y/n): ");
    scanf("%s", s);
    if (strcmp(s, "y") == 0) {
        exit(0);
    }
}

int main() {
    signal(SIGINT, stop);
    while(1) {
        printf("Program is running\n");
        sleep(1);
    }
    return 0;
}

