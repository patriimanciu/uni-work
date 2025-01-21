#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

int n = 0;
pthread_mutex_t m;

void* f(void* a) {
    int i;
    for (i = 0; i<*(int*)a; i++) {
        pthread_mutex_lock(&m);
        n++;
        pthread_mutex_unlock(&m);
    }
    return NULL;
}

int main(int argc, char** argv) {
    int k, i;
    pthread_t t[10];

    sscanf(argv[1], "%d", &k);
    
    pthread_mutex_init(&m, NULL);

    for (i = 0; i<10; i++)
        pthread_create(&t[i], NULL, f, &k);

    for (i = 0; i<10; i++)
        pthread_join(t[i], NULL);
    pthread_mutex_destroy(&m);
    printf("%d\n", n);
    return 0;
}
