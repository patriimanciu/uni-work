#include <stdio.h>

// print only odd numbers of a vector read from console
int main(int argc, char** argv){
	int n, v[100];
	printf("n = ");
	scanf("%d", &n);
	for(int i = 0; i < n; i++){
		scanf("%d", &v[i]);
	}
	for(int i = 0; i < n; i++){
                if (v[i] % 2 == 1)
			printf("%d ", v[i]);
	}
	printf("\n");
	return 0;
}
