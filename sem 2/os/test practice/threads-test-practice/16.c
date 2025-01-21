// 16. Write a C program that receives integers as command line argument. The program will keep a frequency vector for all digits. The program will create a thread for each argument that counts the number of occurences of each digit and adds the result to the frequency vector. Use efficient synchronization.

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int freq[10] = {0};
pthread_mutex_t mutex;

void *func(void *a) {
    int num = atoi((char *) a);
    while (num) {
        pthread_mutex_lock(&mutex);
        freq[num % 10]++;
        pthread_mutex_unlock(&mutex);
        num /= 10;
    }
    return NULL;
}

int main(int argc, char ** argv) {
    if (argc < 2) {
        printf("Usage: %s <num1> <num2> ... <numN>\n", argv[0]);
        return 1;
    }
    pthread_t threads[argc - 1];
    for (int i = 1; i < argc; i++) {
        pthread_create(&threads[i - 1], NULL, func, (void *) argv[i]);
    }
    for (int i = 0; i < argc - 1; i++) {
        pthread_join(threads[i], NULL);
    }
    for (int i = 0; i < 10; i++) {
        printf("%d: %d\n", i, freq[i]);
    }
    return 0;
}
