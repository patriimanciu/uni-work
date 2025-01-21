// increment using threads;
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct {
    int id;
    char *s;
} data;

int n = 0;
pthread_mutex_t m;
void *f(void *arg) {
    for (int i = 0; i < 1000; i++) {
        pthread_mutex_lock(&m);
        n++;
        pthread_mutex_unlock(&m);
    }
    return NULL;
}

int main(int argc, char **argv) {
    int size = 1000;
    pthread_t th[size];
    pthread_mutex_init(&m, NULL);
    for (int i = 0; i < size; i++) {
        if (pthread_create(&th[i], NULL, f, NULL)) {
            perror("Oh no");
        }
    }

    for (int i = 0; i < size; i++) {
        if (pthread_join(th[i], NULL)) {
            perror("Error on join");
        }
    }
    printf("n = %d\n", n);
    pthread_mutex_destroy(&m);
    return 0;
}
