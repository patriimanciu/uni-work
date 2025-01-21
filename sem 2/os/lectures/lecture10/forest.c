#include <stdio.h>
#include <pthread.h>
#include <seamaphore.h>
#define BEES 1
#define BEARS 5

int honey = 100;
pthread_mutex_t m;
pthread_cond_t c;
sem_t s;

void* bear(void* a) {
    while (1) {
        pthread_mutex_lock(&m);
        if (honey >= 10) {
            printf("-");
            honey -= 10;
        }
        else {
            printf("!");
            pthread_cond_signal(&c);
        }
        pthread_mutex_unlock(&m);
    }
    return NULL;
}

void* bee(void* a) {
    while (1) {
        pthread_mutex_lock(&m);
        printf("+");
        honey++;
        pthread_mutex_unlock(&m);
    }
    return NULL;
}

void* ranger(void* a) {
    while (1) {
        pthread_mutex_lock(&m);
        while (honey >= 10) {
            pthread_cond_wait(&c, &m); // wait -> unlock | waits for signal | lock
        }
        printf("H");
        honey += 100;
        pthread_mutex_unlock(&m);
    }
    return NULL;
}

int main(int argc, char** argv) {
    int i;
    pthread_t bees[BEES], bears[BEARS], rangert;
    pthread_mutex_init(&m, NULL);
    pthread_cond_init(&c, NULL);
    sem_init(&s, 0, 0);
    for (i = 0; i < BEES; i++) {
        pthread_create(&bees[i], NULL, bee, NULL);
    }
    for (i = 0; i < BEARS; i++) {
        pthread_create(&bears[i], NULL, bear, NULL);
    }
    pthread_create(&rangert, NULL, rangert, NULL);
    for (i = 0; i < BEES; i++) {
        pthread_join(bees[i], NULL);
    }
    for (i = 0; i < BEARS; i++) {
        pthread_join(bears[i], NULL);
    }
    pthread_join(rangert, NULL);
    
    pthread_mutex_destroy(&m);
    pthread_cond_destroy(&c);
    sem_destroy(&s);
    return 0;
}
