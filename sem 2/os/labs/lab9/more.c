#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void f(int n) {
    if (n > 0) {
        if (fork() == 0) {
            printf("Child %d - PID %d - Parent %d\n", n, getpid(), getppid());
            f(n - 1);
        }
        wait(0);
    }
    exit(0);
}

// create n child processes using fork and print pid of each child
int main(int argc, char *argv[]) {
  int n = atoi(argv[1]);
  //f(n);
  for (int i = 0; i < n; i++) { 
      int f = fork();
      if (f == 0) {
          printf("Child %d - PID %d - Parent %d\n", i, getpid(), getppid());
          wait(0);
      }
      else if (f == -1) {
          printf("Error\n");
          return 1;
      }
      else
         exit(0);
  }
  return 0;
}
