#include "ShortTest.h"
#include "Queue.h"
#include <assert.h>

void testAll() { 
	Queue q;
	assert(q.isEmpty() == true);
	q.push(5);
	q.push(1);
	q.push(10);
	assert(q.isEmpty() == false);
	assert(q.top() == 5);
	assert(q.pop() == 5);
	assert(q.top() == 1);
	assert(q.pop() == 1);
	assert(q.top() == 10);
	assert(q.pop() == 10);
	assert(q.isEmpty() == true);
}