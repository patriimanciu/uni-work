#include <stdio.h>
#include <pthread.h>

int n = 1;

void *fa(void* a) {
    int i;
    for (i = 0; i < n; i++) {
        printf("A\n");
    }
    return NULL;
}

void *fb(void* a) {
    int i;
    for (i = 0; i < n; i++) {
        printf("B\n");
    }
    return NULL;
}

int main(int argc, char **argv) {
    int i;
    pthread_t ta, tb;
    if (argc > 1) {
        sscanf(argv[1], "%d", &n);
    }
    pthread_create(&ta, NULL, fa, NULL);
    pthread_create(&tb, NULL, fb, NULL);
    for (i = 0; i < n; i++) {
        printf("Main\n");
    }
    pthread_join(ta, NULL);
    pthread_join(tb, NULL);
    return 0;
}
