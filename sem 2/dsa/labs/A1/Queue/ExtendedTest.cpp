#include <assert.h>
#include "Queue.h"
#include "ExtendedTest.h"
#include <vector>
#include <exception>
#include <iostream>

using namespace std;

void testCreate() {
	cout << "Test create" << endl;
	Queue q;
	assert(q.isEmpty() == true);
	try {
		q.top(); 
		assert(false); 
	}
	catch (exception&) {
		assert(true);
	}
	try {
		q.pop(); 
		assert(false); 
	}
	catch (exception&) {
		assert(true);
	}
}

void testPush() {
	cout << "Test push" << endl;
	Queue q;
	for (int i = 0; i < 10; i++) {
		q.push(i);
	}
	assert(q.isEmpty() == false);
	for (int i = -10; i < 20; i++) {
		q.push(i);
	}
	assert(q.isEmpty() == false);
	for (int i = -100; i < 100; i++) {
		q.push(i);
	}
	assert(q.isEmpty() == false);

	for (int i = 10000; i > -10000; i--) {
		q.push(i);
	}
	assert(q.isEmpty() == false);
	assert(q.top() != -9999);
	assert(q.top() == 0);

	assert(q.pop() == 0);
	assert(q.top() == 1);
}

void testPop() {
	cout << "Test pop" << endl;
	Queue q;
	for (int i = 0; i < 10; i++) {
		q.push(i);
	}
	assert(q.isEmpty() == false);
	for (int i = -10; i < 20; i++) {
		q.push(i);
	}
	assert(q.isEmpty() == false);
	for (int i = -100; i < 100; i++) {
		q.push(i);
	}
	assert(q.isEmpty() == false);

	for (int i = 10000; i > -10000; i--) {
		q.push(i);
	}
	assert(q.isEmpty() == false);

	
	for (int i = 0; i < 10; i++) {
		assert(q.pop() == i);
	}
	assert(q.isEmpty() == false);
	for (int i = -10; i < 20; i++) {
		assert(q.pop() == i);
	}
	assert(q.isEmpty() == false);
	for (int i = -100; i < 100; i++) {
		assert(q.pop() == i);
	}
	assert(q.isEmpty() == false);

	for (int i = 10000; i > -10000; i--) {
		assert(q.pop() == i);
	}
	assert(q.isEmpty() == true);
}

void testMix() {
	cout << "Test mix" << endl;
	Queue q;
	int first = 7;
	int last = 7;
	int limit = 2;
	for (int i = 0; i < 400; i++) {
		for (int j = 0; j < limit; j++) {
			q.push(last);
			last = (last + 7) % 111111;			
		}
		assert(q.pop() == first);
		first = (first + 7) % 111111;
		if (i % 30 == 0) {
			limit++;
		}
	}
	while (!q.isEmpty()) {
		assert(q.pop() == first);
		first = (first + 7) % 111111;
	}
}

void testQuantity() {
	cout << "Test quantity" << endl;
	Queue q;
	for (int i = 1; i <= 6; i++) {
		for (int j = 30000; j >= -3000; j--) {
			q.push(i + j);
		}
	}

	for (int i = 1; i <= 6; i++) {
		for (int j = 30000; j >= -3000; j--) {
			assert(q.pop() == i + j);
		}
	}
}

void testAllExtended() {
	testCreate();
	testPush();
	testPop();
	testMix();
	testQuantity();
}