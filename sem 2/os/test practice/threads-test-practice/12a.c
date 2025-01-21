// Write a C program that reads a matrix of integers from a file. It then creates as many threads as there are rows in the matrix, each thread calculates the sum of the numbers on a row. The main process waits for the threads to finish, then prints the sums.

#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <string.h>

int sum[100];

typedef struct {
       int *row;
       int n; // row number
       int m; // number of columns
} thread_data_t;

void* func(void *a) {
    thread_data_t *data = (thread_data_t*)a;
    int s = 0;
    for (int i = 0; i < data->m; i++) {
        s += data->row[i];
    }
    sum[data->n] = s;
    return NULL;
}

int main(int argc, char ** argv) {
    // read matrix from file
    if (argc != 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }
    FILE *f = fopen(argv[1], "r");
    if (f == NULL) {
        perror("Could not open file");
        return 2;
    }
    int n, m;
    fscanf(f, "%d %d", &n, &m);
    thread_data_t *data = (thread_data_t*)malloc(n * sizeof(thread_data_t));

    int **a = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        a[i] = (int*)malloc(m * sizeof(int));
        for (int j = 0; j < m; j++) {
            fscanf(f, "%d", &a[i][j]);
        }
        data[i].row = a[i];
        data[i].n = i;
        data[i].m = m;
    }
    fclose(f);

    pthread_t threads[n];
    for (int i = 0; i < n; i++) {
        // create threads
       if (pthread_create(&threads[i], NULL, func, &data[i]) != 0) {
           perror("Could not create thread");
           return 3;
       }
    }

    for (int i = 0; i < n; i++) {
        // wait for threads
        pthread_join(threads[i], NULL);
    }

    // print sums
    for (int i = 0; i < n; i++) {
        printf("Sum of row %d: %d\n", i, sum[i]);
    }
    for (int i = 0; i < n; i++) {
        free(a[i]);
    }
    free(a);
    return 0;
}
