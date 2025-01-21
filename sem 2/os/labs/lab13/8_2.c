#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

int x = 100;
pthread_rwlock_t rwl;

void *shopper(void *a) {
    long id = (long) a;
    srand(time(NULL) + id);
    if (id % 10 == 0) { // buyer
        pthread_rwlock_wrlock(&rwl);
        if (x > 0) {
            int n = rand() % 3 + 1;
            x = x - n;
            printf("Buyer %ld bought %d item, %d items left\n", id, n, x);
        } else {
            printf("Buyer %ld: out of stock\n", id);
        }
        pthread_rwlock_unlock(&rwl);
    }
    return NULL;    
}

int main(int argc, char **argv) {
    int i;
    pthread_t t[200];
    pthread_rwlock_init(&rwl, NULL);
    for (i = 0; i < 200; i++) {
        pthread_create(&t[i], NULL, shopper, (void *) (long) i);
    }
    for (i = 0; i < 200; i++) {
        pthread_join(t[i], NULL);
    }
    pthread_rwlock_destroy(&rwl);
    return 0;
}
