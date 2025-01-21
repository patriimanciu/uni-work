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
pthread_rwlock_t rw;
void *r(void *arg) {
    for (int i = 0; i < 10; i++) {
        pthread_rwlock_rdlock(&rw);
        printf("%d\n", i);
        pthread_rwlock_unlock(&rw);
    }
    return NULL;
}

void *w(void *arg) {
    for (int i = 0; i < 1000; i++) {
        pthread_rwlock_wrlock(&rw);
        n++;
        pthread_rwlock_unlock(&rw);
    }
    return NULL;
}

int main(int argc, char **argv) {
    int r_size = 10;
    int w_size = 2;
    pthread_t r_th[r_size];
    pthread_t w_th[w_size];
    pthread_rwlock_init(&rw, NULL);
    for (int i = 0; i < w_size; i++) {
        if (pthread_create(&w_th[i], NULL, w, NULL)) {
            perror("Oh no");
        }
    }

    for (int i = 0; i < w_size; i++) {
        if (pthread_join(w_th[i], NULL)) {
            perror("Error on join");
        }
    }
    printf("n = %d\n", n);
    pthread_rwlock_destroy(&rw);
    return 0;
}
