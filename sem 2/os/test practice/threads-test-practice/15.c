// Write a program that receives strings of characters as command line arguments. For each string the program creates a thread which calculates the number of digits, the number of leters and the number of special characters (anything other than a letter or digit). The main program waits for the threads to terminate and prints the total results (total number of digits, letters and special characters across all the received command line arguments) and terminates. Use efficient synchronization. Do not use global variables

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

typedef struct {
    char *str;
    int digits;
    int letters;
    int special;
} data;

pthread_mutex_t mutex;
int total_digits = 0, total_letters = 0, total_special = 0;

void *func(void *a) {
    data *d = (data *)a;
    d->digits = 0;
    d->letters = 0;
    d->special = 0;
    for (int i = 0; d->str[i] != '\0'; i++) {
        if (d->str[i] >= '0' && d->str[i] <= '9') {
            d->digits++;
        } else if ((d->str[i] >= 'a' && d->str[i] <= 'z') || (d->str[i] >= 'A' && d->str[i] <= 'Z')) {
            d->letters++;
        } else {
            d->special++;
        }
    }
    pthread_mutex_lock(&mutex);
    total_digits += d->digits;
    total_letters += d->letters;
    total_special += d->special;
    pthread_mutex_unlock(&mutex);
    return NULL;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Usage: %s <string1> <string2> ... <stringN>\n", argv[0]);
        return 1;
    }
    pthread_t threads[argc - 1];
    data *d[argc - 1];
    for (int i = 1; i < argc; i++) {
        d[i-1] = (data *)malloc(sizeof(data));
        d[i-1]->str = argv[i];
        pthread_create(&threads[i - 1], NULL, func, d[i-1]);
    }
    for (int i = 0; i < argc - 1; i++) {
        pthread_join(threads[i], NULL);
        free(d[i]);
    }
    printf("Total digits: %d\n", total_digits);
    printf("Total letters: %d\n", total_letters);
    printf("Total special characters: %d\n", total_special);
    return 0;
}
