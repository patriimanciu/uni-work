#include <stdio.h>
#include <pthread.h>

void *f(void *a) {
    printf("%d\n", *((int *)a));
    return NULL;
}

int main(int argc, char ** argv) {
    int i, a[10];
    pthread_t t[10];
    for (i = 0; i < 10; i++) {
        a[i] = i;
        pthread_create(&t[i], NULL, f, &a[i]);
    }
    for (i = 0; i < 10; i++) {
        pthread_join(t[i], NULL);
    }
    return 0;
}
