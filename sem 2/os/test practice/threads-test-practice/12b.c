// same as 12a, but calculate the sum of all the elements of the matrix using as many threads as there are rows, each thread adds to the total the numbers on a row. Use the test matrix to check if the program is calculating the total sum correctly. The expected result is 1000000. Try with and without mutex.

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

typedef struct {
    int index;
    int col;
    int *row;
} thread_data;

int sum[10000];
int total_sum = 0;

void *func(void *a) {
    thread_data *data = (thread_data *)a;
    int currentSum = 0;
    for (int i = 0; i < data->col; i++) {
        currentSum += data->row[i];
    }
    sum[data->index] = currentSum;
    return NULL;
}

int main(int argc, char** argv) {
    int n, m;
    if (argc < 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }
    FILE *f = fopen(argv[1], "r");
    if (f == NULL) {
        printf("Could not open file\n");
        return 1;
    }
    fscanf(f, "%d %d", &n, &m);
    int **matrix = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++) {
        matrix[i] = (int *)malloc(m * sizeof(int));
        for (int j = 0; j < m; j++) {
            fscanf(f, "%d", &matrix[i][j]);
        }
    }
    fclose(f);
    thread_data *data = (thread_data *)malloc(n * sizeof(thread_data));
    pthread_t *threads = (pthread_t *)malloc(n * sizeof(pthread_t));
    for (int i = 0; i < n; i++) {
        data[i].index = i;
        data[i].col = m;
        data[i].row = matrix[i];
        pthread_create(&threads[i], NULL, func, &data[i]);
    }
    for (int i = 0; i < n; i++) {
        pthread_join(threads[i], NULL);
    }
    for (int i = 0; i < n; i++) {
        total_sum += sum[i];
    }
    printf("Total sum: %d\n", total_sum);
    return 0;
}
