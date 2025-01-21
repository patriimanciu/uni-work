#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    int i;
    FILE* fp;
    fp = popen("less", "w");
    for(i=99; i>0; i--) {
        fprintf(fp, "%d bottles of beer on the wall,\n", i);
        fprintf(fp, " %d bottles of beer.\n", i);
        fprintf(fp, "If one of those bottles should happen to fall,\n");
        fprintf(fp, " %d bottles of beer on the wall.\n\n", i-1);
    }
    pclose(fp);
    return 0;
}
