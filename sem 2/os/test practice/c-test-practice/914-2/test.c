//Copy this file to another file having a .c extension (eg a.c)
//ср <FILENAME>.txt <FILENAME>.c
//Program description:
//Read a matrix from a file, given as a command line argument.
//The file contains on it's first line the number of line and columns of the matrix //followed by the matrix itself - the elements of the matrix are alphabetic characters.
//Prints as output: the vowels found on each row

//Notes:
//>The memory space used to store the matrix must be dynamically allocated.
//>The source file must be compiled using gcc with -Wall -g options WITHOUT WARNINGS OR SYNTAX ERRORS!!!
//>The program should not have any memory leaks or indicate any errors while using valgrind (valgrind /executable argl arg2 arg3)

//ex:
//input
//3 4
//a b c d 
//e a a g
//v c i h
//output 
//a e a a i 

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    int n, m, i, j;
    char c;

    FILE* f = fopen(argv[1], "r");
    fscanf(f, "%d %d\n", &n, &m);
    char** matrix = (char **) malloc(n * sizeof(char*));

    for(i = 0; i < n; i++) {
        matrix[i] = (char*)malloc(m * sizeof(char));

        for(j = 0; j < m; j++) {
            fscanf(f, "%c", &c);

            while(c == ' ' || c == '\n')
                fscanf(f, "%c", &c);
            matrix[i][j] = c;
        }
    }
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            if (matrix[i][j] == 'a' || matrix[i][j] == 'e' || matrix[i][j] == 'i' || matrix[i][j] == 'o' || matrix[i][j] == 'u') {
                printf("%c ", matrix[i][j]);
            }
        }
    }
    printf("\n");

    for (i = 0; i < m; i++) {
        free(matrix[j]);
    }
    free(matrix);
    return 0;
}
