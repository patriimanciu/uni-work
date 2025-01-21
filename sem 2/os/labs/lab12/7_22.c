#include <stdio.h>
#include <pthread.h>

struct arg_t {
    char *name;
    int count;
};

void *f(void* a) {
    int i;
    struct arg_t *x = (struct arg_t*)a;
    for (i = 0; i < x->count; i++) {
        printf("%s\n", x->name);
    }
    return NULL;
}

int main(int argc, char **argv) {
    int i, n = 1;
    pthread_t ta, tb;
    struct arg_t a = {"A", n}, b = {"B", n};
    if (argc > 1) {
        sscanf(argv[1], "%d", &n);
    }
    a.count = n;
    b.count = n;
    pthread_create(&ta, NULL, f, &a);
    pthread_create(&tb, NULL, f, &b);
    for (i = 0; i < n; i++)
        printf("Main\n");
    pthread_join(ta, NULL);
    pthread_join(tb, NULL);
    return 0;
}
