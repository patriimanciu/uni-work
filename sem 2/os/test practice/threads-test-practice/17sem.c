#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

sem_t even_sem, odd_sem;
int n;
int i = 0;

void *even(void *a) {
    int *arr = (int *)a;
    while (i < n) {
        sem_wait(&even_sem);
        if (i % 2 == 0) {
            arr[i] = rand() * 2 % 100;
            i++;
        }
        sem_post(&odd_sem);
    }
    return NULL;
}

void *odd(void *a) {
    int *arr = (int *)a;
    while (i < n) {
        sem_wait(&odd_sem);
        if (i % 2 == 1) {
            arr[i] = rand() * 2 % 100 + 1;
            i++;
        }
        sem_post(&even_sem);
    }
    return NULL;
}

int main(int argc, char** argv) {
    pthread_t t1, t2;
    if (argc != 2) {
        printf("Usage: %s <n>\n", argv[0]);
        return 1;
    }
    n = atoi(argv[1]);
    sem_init(&even_sem, 0, 1);
    sem_init(&odd_sem, 0, 0);
    int *arr = (int *)malloc(n * sizeof(int));
    pthread_create(&t1, NULL, even, arr);
    pthread_create(&t2, NULL, odd, arr);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    sem_destroy(&even_sem);
    sem_destroy(&odd_sem);
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    free(arr);
    return 0;
}
