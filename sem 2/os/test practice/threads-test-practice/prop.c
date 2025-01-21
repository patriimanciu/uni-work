// an input proposition has at least 5 words, using threads reverse the order of the words
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

typedef struct {
    char** words;
    int from;
    int to;
    sem_t* sem;
} WordsSwapArgs;

void *wordsSwap(void *words) {
    WordsSwapArgs* args = (WordsSwapArgs*)words;
    //printf("Swapping %d and %d\n", args->from, args->to);
    printf("Waiting for semaphore %d\n", args->from);
    sem_wait(args->sem);
    printf("Semaphore acquired %d\n", args->from);
    char* temp = args->words[args->from];
    args->words[args->from] = args->words[args->to];
    args->words[args->to] = temp;
    printf("Swapped %d and %d\n", args->from, args->to);
    printf("Releasing semaphore %d\n", args->from);
    sem_post(args->sem);
    free(args);
}


int main(int argc, char** argv) {
    if (argc < 6) {
        printf("Usage: %s <word1> <word2> <word3> <word4> <word5>\n", argv[0]);
        return 1;
    }
    sem_t sem;
    int n = argc - 1; 
    char** words = (char**)malloc(n * sizeof(char*));
    for (int i = 0; i < n; i++) {
        words[i] = argv[i + 1];
    }
    pthread_t threads[n / 2];
    sem_init(&sem, 0, 5);
    for (int i = 0; i < n / 2; i++) {
        WordsSwapArgs* args = malloc(sizeof(WordsSwapArgs));
        args->words = words;
        args->from = i;
        args->to = n - i - 1;
        args->sem = &sem;
        pthread_create(&threads[i], NULL, wordsSwap, args);
    }
    for (int i = 0; i < n / 2; i++) {
        pthread_join(threads[i], NULL);
    }
    for (int i = 0; i < n; i++) {
        printf("%s ", words[i]);
    }
    sem_destroy(&sem);
    printf("\n");
    free(words);
    return 0;
}
