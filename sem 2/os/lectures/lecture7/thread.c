#include <stdio.h>
#include <pthread.h>

void* f(void* a) {
    printf("f\n");
    return NULL;
}

int main(int argc, char ** argv) {
    // threads will have a handler, but there's no child-parent relation here
    pthread_t t;
    pthread_create(&t, NULL, f, NULL);
    // now we have 2 threads, main and f that work in parallel
    printf("main\n");
    pthread_join(t, NULL);
    return 0;
}
