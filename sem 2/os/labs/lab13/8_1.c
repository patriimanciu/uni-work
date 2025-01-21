#include <stdio.h>
#include <pthread.h>

int count = 0;
pthread_mutex_t mutex;

void *f(void *a) {
    int i;
    for (i = 0; i < *(int *)a; i++) {
        pthread_mutex_lock(&mutex);
        count++;
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main(int argc, char **argv) {
    int i, n = 10;
    pthread_t t[10];
    if (argc > 1) {
        sscanf(argv[1], "%d", &n);
    }
    pthread_mutex_init(&mutex, NULL);
    for (i = 0; i < n; i++) {
        pthread_create(&t[i], NULL, f, &n);
    }
    for (i = 0; i < n; i++) {
        pthread_join(t[i], NULL);
    }
    pthread_mutex_destroy(&mutex);
    printf("count = %d\n", count);
    return 0;
}
