#include <stdio.h>
#include <pthread.h>

int count = 0;

void *f(void *a) {
    int i;
    for (i = 0; i < *(int*)a; i++) {
        count++;
    }
    return NULL;
}

int main(int argc, char **argv) {
   int i, n = 1000;
   pthread_t t[n];
   if (argc > 1) {
       sscanf(argv[1], "%d", &n);
   }
   for (i = 0; i < 10; i++) {
       pthread_create(&t[i], NULL, f, &n);
   }
   for (i = 0; i < 10; i++) {
       pthread_join(t[i], NULL);
   }
   printf("count = %d\n", count);
   return 0;
}
