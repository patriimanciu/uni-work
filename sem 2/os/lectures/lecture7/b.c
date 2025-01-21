   #include "h.h"
 
   int main(int argc, char ** argv) {
       int shmid;
       struct absp* x;
 
       shmid = shmget(1234, 0, 0);
       x = shmat(shmid, 0, 0); // pointer to that memory
       srand(time(NULL)); // current time in seconds since 1970 :)
       while (1) {
           x->p = x->a * x->b;
           x->s = x->a + x->b;
           if (x->p == x->s)
               break;
       }
 
       shmdt(x);
       return 0;
   }
