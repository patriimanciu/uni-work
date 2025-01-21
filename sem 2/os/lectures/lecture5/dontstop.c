#include <stdio.h>
#include <signal.h>

void f(int sgn) {
    printf("Nope\n");
}

int main(int agrc, char ** argv) {
    signal(SIGINT, f);
    while(1);
    return 0;
}
