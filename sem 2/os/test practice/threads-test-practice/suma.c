#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int SUMA;
pthread_mutex_t mutex;
pthread_cond_t cond;
int global = 1;

int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n - 1);
}

void *func(void *arg) {
    int n = *(int *)arg;
    pthread_mutex_lock(&mutex);
    while (SUMA < n) {
        printf("Thread waiting...\n");
        global++;
        printf("Global: %d\n", global);
        int fact = factorial(global);
        printf("Factorial: %d\n", fact);
        SUMA += fact;
        pthread_cond_wait(&cond, &mutex);
        printf("Suma: %d\n", SUMA);
    }
    pthread_cond_signal(&cond);
    pthread_mutex_unlock(&mutex);
    return NULL;
}

int main(int argc, char **argv) {
    SUMA = 0;
    pthread_t threads[5];
    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&cond, NULL);
    for (int i = 0; i < 5; i++) {
        int n = atoi(argv[1]);
        pthread_create(&threads[i], NULL, func, &n);
    }
    for (int i = 0; i < 5; i++) {
        pthread_mutex_lock(&mutex);
        pthread_cond_signal(&cond);
        pthread_mutex_unlock(&mutex);
    }
    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL);
    }
    printf("Suma: %d\n", SUMA);
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&cond);
    return 0;
}
