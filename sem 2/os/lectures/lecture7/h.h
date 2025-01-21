#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdlib.h>
#include <time.h>

struct absp {
    int a;
    int b;
    int s;
    int p;
};
