// 17. Write a C program that reads a number N and creates 2 threads. One of the threads will generate an even number and will append it to an array that is passed as a parameter to the thread. The other thread will do the same, but using odd numbers. Implement a synchronization between the two threads so that they alternate in appending numbers to the array, until they reach the maximum length N.

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int n;
int i = 0;
pthread_mutex_t mutex;

void *func1(void *arg) {
    int *array = (int *)arg; 
    while (i < n) {
        pthread_mutex_lock(&mutex);
        if (i % 2 == 0) {
            array[i] = rand() * 2 % 100;
            i++;
        }
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

void *func2(void *arg) {
    int *array = (int *)arg;
    while (i < n) {
        pthread_mutex_lock(&mutex);
        if (i % 2 == 1) {
            array[i] = rand() * 2 % 100 + 1;
            i++;
        }
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main(int agrc, char **argv) {
    n = atoi(argv[1]);
    int arr[n];
    srand(time(NULL));
    pthread_mutex_init(&mutex, NULL);

    pthread_t t1, t2;
    pthread_create(&t1, NULL, func1, (void *)arr);
    pthread_create(&t2, NULL, func2, (void *)arr);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    pthread_mutex_destroy(&mutex);
    printf("Array: ");
    for (int j = 0; j < n; j++) {
        printf("%d ", arr[j]);
    }

    return 0;
}
