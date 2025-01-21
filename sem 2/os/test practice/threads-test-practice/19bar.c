#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

int N, M;
int *numbers;
pthread_t *tids;
pthread_barrier_t barrier;

void *func(void *a) {
    int idx = *(int *)a;
    pthread_barrier_wait(&barrier);
    int l, r, i ,j;
    if (idx < M / 2) {
        l = idx * 2;
        r = l + 1;
        pthread_join(tids[l], NULL);
        pthread_join(tids[r], NULL);
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
        l += M / j;
    }
    r = l + M / j / 2;
    numbers[l] += numbers[r];
    return NULL;
}

int main(int argc, char** argv) {
    int i;
    if (argc < 2) {
        printf("Usage: %s <number>\n", argv[0]);
        return 1;
    }
    M = 1;
    N = atoi(argv[1]);
    while (M < N) {
        M *= 2;
    }
    int a[M];
    for (i = 0; i < M; i++) {
        if (i < N)
            scanf("%d", &a[i]);
        else
            a[i] = 0;
    }
    pthread_barrier_init(&barrier, NULL, M - 1);
    tids = malloc(sizeof(pthread_t) * M);
    int *ids = malloc(sizeof(int) * M);
    for (i = 0; i < M; i++) {
        ids[i] = i;
    }
    for (i = 1; i < M; i++) {
        if (0 > pthread_create(&tids[i], NULL, func, &ids[i])) {
            perror("pthread_create");
            return 1;
        }
    }
    if (0 > pthread_join(tids[1], NULL)) {
        perror("pthread_join");
        return 1;
    }
    printf("%d\n", a[0]);
    pthread_barrier_destroy(&barrier);
    free(tids);
    free(ids);
    free(numbers);
    return 0;
}
