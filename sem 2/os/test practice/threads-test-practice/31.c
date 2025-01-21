// Write a C program that receives a number N as a command-line argument. The program creates N threads that will generate random numbers between 0 and 111111 (inclusive) until one thread generates a number divisible by 1001. The threads will display the generated numbers, but the final number that is displayed must be the one that is divisible by 1001. No thread will start generating random numbers until all threads have been created. Do not use global variables.
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

typedef struct {
    int id;
    int *found;
    pthread_mutex_t *m;
    pthread_barrier_t *b;
} data;

void *func(void *arg) {
    data d = *(data *)arg;
    pthread_barrier_wait(d.b);
    int nr;
    while (1) {
        nr  = rand() % 111112;
        pthread_mutex_lock(d.m);
        if (*(d.found) == 0) {
            printf("Thread %d generated %d\n", d.id, nr);
            if (nr % 1001 == 0) {
                *(d.found) = 1;
                break;
            }
        }
        else {
            break;
        }
        pthread_mutex_unlock(d.m);
        usleep(1000);
    }
    pthread_mutex_unlock(d.m);
}

int main(int argc, char** argv) {
    pthread_mutex_t *mutex = malloc(sizeof(pthread_mutex_t));
    pthread_cond_t *bar = malloc(sizeof(pthread_barrier_t));

    pthread_mutex_init(mutex, NULL);
    pthread_barrier_init(bar, NULL);
    
    int N = atoi(argv[1]);
    pthread_t *threads = malloc(sizeof(pthread_t) * N);
    data *d = malloc(sizeof(data) * N);
    srand(time(NULL));
    int *found = malloc(sizeof(int));
    for (int i = 0; i < N; i++) {
        d[i].id = i;
        d[i].m = mutex;
        d[i].c = cond;
        d[i].found = found;
        pthread_create(&threads[i], NULL, func, &d[i]);
    }
    for (int i = 0; i < N; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(mutex);
    pthread_barrier_destroy(bar);
    free(threads);
    free(d);
    free(mutex);
    free(bar);
    free(found);
    return 0;
} 
