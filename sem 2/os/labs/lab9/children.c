#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// create n child processes using fork and print pid of each child
int main(int argc, char *argv[]) {
  int n = atoi(argv[1]);
  for (int i = 0; i < n; i++) {
    int f = fork();
    if (f == 0) {
      printf("Child %d - PID %d - Parent %d\n", i, getpid(), getppid());
      return 0;
    }
    else if (f < 0) {
      printf("Error creating child %d\n", i);
      return 1;
    }
  }
  return 0;
}
