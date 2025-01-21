#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

// Write a C program that will read from keyboard lowercased strings (until X is written).
// The main process will start two types of Child processes: A and B started every time a string is read from the keyboard
// Child processes A.
    // The parent will send the string to the created child process using pipes.
    // Each child process will initiate a vector V with 26 zeros and will iterate over the string character by character trying to compute an index considering the ASCII code of a character:
    // a (97) -> 0
    // b (98) -> 1
    // c (99) -> 2 

    // This index corresponds to a position in vector V that will have to be incremented during each character iteration.
    // This frequency vector for the characters found in the string will be send back:
        // - to the parent using pipes that will print it on the screen.
        // - to the process B
// Child processes B:
    // Will receive the frequency vector from the a child process A with a pipe and it will sum up all the values and print the result on the screen.
    // The parent will wait for the child processes to finish and will print the total sum of all the characters found in the strings.

int main(int argc, char** argv) {
    char string[100];
    while (1) {
        int p2a[2], a2p[2], p2b[2], b2p[2];
        pipe(p2a);
        pipe(a2p);
        pipe(p2b);
        pipe(b2p);
        scanf("%s", string);
        if (string[0] == 'X') {
            break;
        }
        int f = fork();
        if (f == 0) {
            // child A
            printf("Child A: %d\n", getpid());
            close(p2a[1]); close(a2p[0]); close(p2b[0]); close(p2b[1]);
            char v[26] = {0};
            char child_string[100];
            read(p2a[0], child_string, sizeof(child_string));
            for (int i = 0; child_string[i] != '\0'; i++) {
                v[child_string[i] - 'a']++;
            }
            write(a2p[1], v, sizeof(v));
            close(p2a[0]); close(a2p[1]);
            exit(0);
        }
        else {
            int f2 = fork();
            if (f2 == 0) {
                // child B
                printf("Child B: %d\n", getpid());
                close(p2b[1]); close(b2p[0]); close(a2p[1]); close(p2b[0]);
                char v[26] = {0};
            
                read(a2p[0], v, sizeof(v));
                int sum = 0;
                for (int i = 0; i < 26; i++) {
                    if (v[i] != 0){
                        printf("%c: %d\n", i + 'a', v[i]);
                    }
                    sum += v[i];
                }
                write(b2p[1], &sum, sizeof(sum));
                
                close(a2p[0]); close(b2p[1]);
                exit(0);
            }
            else {
                // parent
                close(p2a[0]); close(a2p[1]); close(a2p[0]); close(b2p[1]);
                write(p2a[1], string, strlen(string) + 1);
                wait(0);
                wait(0);

                int sum = 0;
                read(b2p[0], &sum, sizeof(sum));
                printf("Sum: %d\n", sum);
                close(p2a[1]); close(p2b[0]);
            }
        }
    }


    return 0;
}
