#include <stdio.h>
#include <stdlib.h>
// read a matrix from a file and display it

int main(int argc, char ** argv){
	int ** m; // the matrix
	int row, col;
	FILE* f = fopen(argv[1], "r");
	fscanf(f, "%d %d", &row, &col);
	printf("r = %d; c = %d\n", row, col);
	
	m = (int **)malloc(sizeof(int *) * row);
	for (int i = 0; i < row; i++){
		m[i] = (int *)malloc(sizeof(int) * col);
		for (int j = 0; j < col; j++)
			fscanf(f, "%d", &m[i][j]);
	}
	for (int i = 0; i < row; i++){
		for (int j = 0; j < col; j++)
			printf("%d ", m[i][j]);
		printf("\n");
	}
	
	for (int i = 0; i < row; i++)
		free(m[i]);
	free(m);
	fclose(f);
	return 0;
}
