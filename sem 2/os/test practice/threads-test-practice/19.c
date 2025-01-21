// 19. Create a C program that takes one integer N as a command line argument, and then reads N integers from the keyboard and stores them in an array. It then calculates the sum of all the read integers using threads that obey the hierarchy presented in the image below. For any given N, the array has to be padded with extra integers with value 0 to ensure that it always contains a number of elements equal to a power of 2 (let this number be M). The required number of threads will be M - 1, let each thread have and ID from 1 to M - 1. As per the image, threads with ID >= M / 2 will calculate the sum of 2 numbers on consecutive positions in the array. Threads with an ID < M / 2 must wait for 2 threads to finish and then they will add the results produced by those two threads.

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

int *numbers, N, M;
int *thrd_init;
pthread_t *threads;
pthread_cond_t *conds;
pthread_mutex_t *mutexes;

void signal_init_thrd(int index) {
    pthread_mutex_lock(&mutexes[index]);
    thrd_init[index] = 1;
    pthread_cond_signal(&conds[index]);
    pthread_mutex_unlock(&mutexes[index]);
}

void wait_for_init_thrd(int index) {
    pthread_mutex_lock(&mutexes[index]);
    while (thrd_init[index] != 1) {
        pthread_cond_wait(&conds[index], &mutexes[index]);
    }
    pthread_mutex_unlock(&mutexes[index]);
}

void *add(void *arg) {
    int idx = *(int*)arg;
    signal_init_thrd(idx);
    int l, r, i, j;
    if (idx < M/2) {
        l = 2 * idx;
        r = 2 * idx + 1;
        wait_for_init_thrd(l);
        wait_for_init_thrd(r);
        pthread_join(threads[l], NULL);
        pthread_join(threads[r], NULL);
    }

    j = M;
    while (j > idx && j > 1) {
        j /= 2;
    }
    i = j;
    l = 0;
    r = 0;
    while (i < idx) {
        i++;
        l+= M / j;
    } 
    r = l + M / j / 2;
    numbers[l] += numbers[r];
    return NULL;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        printf("Usage: %s <N>\n", argv[0]);
        return 1;
    }
    N = atoi(argv[1]);
    M = 1;
    while (M < N) {
        M *= 2;
    }
    numbers = (int*)malloc(M * sizeof(int));
    for (int i = 0; i < M; i++) {
        if (i < N) {
            scanf("%d", &numbers[i]);
        } else {
            numbers[i] = 0;
        }
    }
    mutexes = malloc(M * sizeof(pthread_mutex_t));
    conds = malloc(M * sizeof(pthread_cond_t));
    thrd_init = malloc(M * sizeof(int));
    threads = malloc((M) * sizeof(pthread_t));
    int *ids = malloc((M) * sizeof(int));
    for (int i = 0; i < M; i++) {
        pthread_mutex_init(&mutexes[i], NULL);
        pthread_cond_init(&conds[i], NULL);
        thrd_init[i] = 0;
        ids[i] = i;
    }
    for (int i = 1; i < M; i++) {
        pthread_create(&threads[i], NULL, add, &ids[i]);
    }
    if (0 > pthread_join(threads[1], NULL)) {
        perror("pthread_join");
        return 1;
    }
    printf("Sum: %d\n", numbers[0]);
    for (int i = 0; i < M; i++) {
        pthread_mutex_destroy(&mutexes[i]);
        pthread_cond_destroy(&conds[i]);
    }
    free(mutexes);
    free(conds);
    free(thrd_init);
    free(threads);
    free(numbers);
    free(ids);
    return 0;
}
