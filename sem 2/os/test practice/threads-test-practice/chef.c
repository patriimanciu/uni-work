#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>

pthread_mutex_t stoveMutex[4];
int stoveFuel[4] = {100, 100, 100, 100};

void *routine(void* arg) {
    for (int i = 0; i < 4; i++) {
        if (pthread_mutex_trylock(&stoveMutex[i]) == 0) {
            usleep(50000);
            int need = rand() % 30;
            if (stoveFuel[i] < need) {
                printf("Need %d fuel, but only %d fuel left at stove %d\n", need, stoveFuel[i], i);
            } else {
                printf("Need %d fuel, and %d fuel left at stove %d\n", need, stoveFuel[i], i);
                stoveFuel[i] -= need;
            }
            pthread_mutex_unlock(&stoveMutex[i]);
            break;
        }
        else {
            if (i == 3) {
                printf("All stoves are busy, waiting...\n");
                usleep(500000);
                i = 0;
            }
        }
    }
}

int main(int argc, char**argv) {
    pthread_t t[10];
    srand(time(NULL));
    for (int i = 0; i < 4; i++)
        pthread_mutex_init(&stoveMutex[i], NULL);
    for (int i = 0; i < 10; i++ ) {
        if (pthread_create(&t[i], NULL, routine, NULL) != 0) {
            perror("Failed to create thread\n");
        }
    }
    for (int i = 0; i < 10; i++) {
        pthread_join(t[i], NULL);
    }
    for (int i = 0; i < 4; i++)
        pthread_mutex_destroy(&stoveMutex[i]);
    return 0;
}
