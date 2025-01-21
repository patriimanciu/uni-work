#include <stdio.h>
#include <pthread.h>

int x = 100;
pthread_rwlock_t rwl;

void *shopper(void* a) {
    long id = (long) a;
    if (id % 10 == 0) {
        pthread_rwlock_wrlock(&rwl);
        if (x > 0) {
            x-=10;
            printf("Shopper %ld bought 1 item\n", id);
        }
        else {
            printf("Shopper %ld couldn't buy anything\n", id);
        }
        pthread_rwlock_unlock(&rwl);
    }
    else {
        pthread_rwlock_rdlock(&rwl);
        printf("Shopper %ld read x = %d\n", id, x);
        pthread_rwlock_unlock(&rwl);
    }
    return NULL;
}

int main(int argc, char ** argv) {
    int i;
    pthread_t threads[100];
    pthread_rwlock_init(&rwl, NULL);
    for (i = 0; i < 100; i++) {
        pthread_create(&threads[i], NULL, shopper, (void*) (long) i);
    }
    for (i = 0; i < 100; i++) {
        pthread_join(threads[i], NULL);
    }
    pthread_rwlock_destroy(&rwl);
    return 0;
}
