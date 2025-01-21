#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// 3. Să se scrie un program C care creează un proces copil cu care comunică prin pipe.
// Procesul părinte citeşte de la tastatură un caracter c şi un şir s şi le trimite prin pipe procesului copil,
// iar procesul copil verifică şi afişează numărul de apariţii ale caracterului c în şirul s.

int main(int argc, char** argv) {
    int p2c[2], c2p[2];
    pipe(p2c);
    pipe(c2p);
    int f = fork();
    if (f == 0) {
        // child
        close(p2c[1]); close(c2p[0]);
        char c;
        char s[100];
        read(p2c[0], &c, sizeof(char));
        read(p2c[0], s, 100);
        int count = 0;
        for (int i = 0; i < strlen(s); i++) {
            if (s[i] == c) {
                count++;
            }
        }
        write(c2p[1], &count, sizeof(int));
        close(p2c[0]); close(c2p[1]);
        exit(0);
    }
    // parent
    close(p2c[0]); close(c2p[1]);
    char c;
    char s[100];
    printf("c = "); scanf("%c", &c);
    printf("s = "); scanf("%s", s);
    write(p2c[1], &c, sizeof(char));
    write(p2c[1], s, 100);
    int count;
    wait(0);
    read(c2p[0], &count, sizeof(int));
    printf("count = %d\n", count);
    close(p2c[1]); close(c2p[0]);

    return 0;
}
