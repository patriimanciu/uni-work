#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#include <time.h>

#define THREADS_NUM 16

sem_t semaphore;

void *routine(void *arg) {
    printf("(%d) Waiting in the logging queue...\n", *(int *)arg);
    sem_wait(&semaphore);
    printf("(%d) Logged in. \n", *(int *)arg);
    usleep((rand() % 5 + 1) * 100000);
    printf("(%d) Logged out.\n", *(int *)arg);
    sem_post(&semaphore);
    free(arg);
}


int main(int argc, char** argv) {
    pthread_t th[THREADS_NUM];
    srand(time(NULL));
    sem_init(&semaphore, 0, 12); // like a mutex
    for (int i = 0; i < THREADS_NUM; i++) {
        int *a = malloc(sizeof(int));
        *a = i;
        pthread_create(&th[i], NULL, routine, a);
    }
    for (int i = 0; i < THREADS_NUM; i++) {
        pthread_join(th[i], NULL);
    }
    sem_destroy(&semaphore);

    return 0;
}
