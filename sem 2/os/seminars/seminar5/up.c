// create a thread for each argumentprintf("thrd %d - arg %s\n", d->id, d->s);
// each thread converts any lowercase letters in the argument to uppercase
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct {
    int id;
    char *s;
} data;

void* upcase(void *arg) {
    data *d = (data*)arg;
    char *copy = malloc(strlen(d->s) + 1);
    strcpy(copy, d->s);
    for (int i = 0; i < strlen(d->s); i++) {
        if (islower(d->s[i])) {
            copy[i] = toupper(copy[i]);
        }
    }
    printf("thrd %d - arg %s - copy %s\n", d->id, d->s, copy);
    return copy;
}

int main(int argc, char **argv) {
    int size = argc - 1;
    pthread_t th[size];
    data *args = malloc(size * sizeof(data));
    for (int i = 0; i < size; i++) {
        args[i].id = i;
        args[i].s = argv[i + 1];
        if (pthread_create(&th[i], NULL, upcase, &args[i])) {
            perror("Oh no");
        }
    }

    for (int i = 0; i < size; i++) {
        void *res;
        if (pthread_join(th[i], &res)) {
            perror("Error on join");
        }
        printf("Result from thread %d: %s\n", i, (char*)res);
        free(res);
    }
    free(args);
    printf("END: \n");
    for (int i = 0; i < size; i++) {
        printf("argv[%d] - %s\n", i+1, argv[i+1]);
    }
    return 0;
}
