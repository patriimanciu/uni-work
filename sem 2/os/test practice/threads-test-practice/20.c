// 20. Write a C program that takes as command line arguments 2 numbers: N and M. The program will simulate a thread race that have to pass through M checkpoints. Through each checkpoint the threads must pass one at a time (no 2 threads can be inside the same checkpoint). Each thread that enters a checkpoint will wait between 100 and 200 milliseconds (usleep(100000) makes a thread or process wait for 100 milliseconds) and will print a message indicating the thread number and the checkpoint number, then it will exit the checkpoint. Ensure that no thread will try to pass through a checkpoint until all threads have been created.

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

typedef struct {
    int id, M;
    pthread_mutex_t *mutex;
    pthread_barrier_t *barrier;
} data;

void *func(void *a) {
    data d = *(data *) a;
    int i;
    printf("Thread %d is waiting...\n", d.id);
    pthread_barrier_wait(d.barrier);
    for (i = 0; i < d.M; i++) {
        pthread_mutex_lock(&d.mutex[i]);
        printf("Thread %d is passing through checkpoint %d\n", d.id, i);
        int n = (rand() % 101 + 100) * 1000;
        usleep(n);
        pthread_mutex_unlock(&d.mutex[i]);
    }
    printf("Thread %d has finished\n", d.id);
    return NULL;
}

void wait_threads(pthread_t *threads, int N) {
    int i;
    for (i = 0; i < N; i++) {
        pthread_join(threads[i], NULL);
    }
}


int main(int argc, char ** argv) {
    if (argc < 3) {
        printf("Usage: %s N M\n", argv[0]);
        return 1;
    }
    int N = atoi(argv[1]);
    int M = atoi(argv[2]);
    pthread_t *threads = malloc(N*sizeof(pthread_t));
    data *args = malloc(N*sizeof(data));
    pthread_barrier_t barrier;
    pthread_mutex_t mutex *mutexs = malloc(M*sizeof(pthread_mutex_t));
    if (0 > pthread_barrier_init(&barrier, NULL, N)) {
        free(threads);
        free(args);
        free(mutexs);
        return 2;
    }
    int i;
    for (i = 0; i < M; i++) {
        if (0 > pthread_mutex_init(&mutexs[i], NULL)) {
            free(threads);
            free(args);
            free(mutexs);
            pthread_barrier_destroy(&barrier);
            return 3;
        }
    }
    srand(time(NULL));
    for (i = 0; i < N; i++) {
        args[i].id = i;
        args[i].M = M;
        args[i].mutex = mutexs;
        args[i].barrier = &barrier;
        if (0 > pthread_create(&threads[i], NULL, func, &args[i])) {
            free(threads);
            free(args);
            free(mutexs);
            pthread_barrier_destroy(&barrier);
            return 4;
        }
    }
    wait_threads(threads, N);
    pthread_barrier_destroy(&barrier);
    free(threads);
    free(args);
    free(mutexs);
    return 0;
}
