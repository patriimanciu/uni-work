#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 128

typedef struct {
    int id;
    char *buf;
    int *pos;
    int maxSize;
    int *repeats; // number of repetitions - make them pointers when they are shared variables
    pthread_mutex_t *m;
    pthread_cond_t *c;
} data;

void *print(void *arg) {
    data d = *(data *)arg;
    while(1) {
        pthread_mutex_lock(d.m);
        if (*(d.repeats) == 0) {
            pthread_cond_broadcast(d.c);
            pthread_mutex_unlock(d.m);
            break;
        }
    
        while(*(d.pos) < d.maxSize) {
            pthread_cond_broadcast(d.c);
            pthread_cond_wait(d.c, d.m);
        }
        printf("%s\n", d.buf);
        memset(d.buf, 0, sizeof(char) * d.maxSize);
        *(d.pos) = 0;
        *(d.repeats) -= 1;
        pthread_mutex_unlock(d.m);    
    }
    return NULL;    
}

void *gen(void *arg) {
    data d = *(data *)arg;
    while (1) {
        pthread_mutex_lock(d.m); // lock it since repeats is shared
        if (*(d.repeats) == 0) {
            pthread_cond_broadcast(d.c);
            pthread_mutex_unlock(d.m);
            break;
        }
        while (*(d.pos) == d.maxSize) {
            pthread_cond_broadcast(d.c); // wake up all threads, signal only wakes up one
            pthread_cond_wait(d.c, d.m);
        }
        char c = rand() % 26 + 'a';
        d.buf[*(d.pos)] = c;
        *(d.pos) += 1;
        pthread_mutex_unlock(d.m);
    }
    return NULL;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        printf("Usage: %s <size> <repeats>\n", argv[0]);
        return 1;
    }
    int n = atoi(argv[1]);
    int m = atoi(argv[2]);
    int pos = 0;
    pthread_mutex_t mtx;
    pthread_cond_t cond;
    pthread_mutex_init(&mtx, NULL);
    pthread_cond_init(&cond, NULL);
    pthread_t th[n];
    data args[n + 1];
    char *buf = (char *)malloc(sizeof(char) * (SIZE + 1));
    for (int i = 0; i < n; i++) {
        args[i].id = i;
        args[i].m = &mtx;
        args[i].c = &cond;
        args[i].repeats = &m;
        args[i].pos = &pos;
        args[i].maxSize = SIZE;
        args[i].buf = buf;
        if (0 != pthread_create(&th[i], NULL, gen, &args[i])) {
            perror("pthread_create");
            exit(1);
        }
    }
    args[n].id = n;
    args[n].m = &mtx;
    args[n].c = &cond;
    args[n].repeats = &m;
    args[n].pos = &pos;
    args[n].maxSize = SIZE;
    args[n].buf = buf;
    if (0 != pthread_create(&th[n], NULL, print, &args[n])) {
        perror("pthread_create");
        exit(1);
    }
    for (int i = 0; i < n; i++) {
        if (0 != pthread_join(th[i], NULL)) {
            perror("pthread_join");
            exit(1);
        }
    }
    pthread_mutex_destroy(&mtx);
    pthread_cond_destroy(&cond);
    free(buf);
    return 0;
}
