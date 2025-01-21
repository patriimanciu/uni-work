#include <assert.h>
#include "Stack.h"
#include "ExtendedTest.h"
#include <vector>
#include <exception>
#include <iostream>
using namespace std;

void testCreate() {
	cout << "Test create" << endl;
	Stack s;
	assert(s.isEmpty() == true);
	try {
		s.top(); 
		assert(false); 
	}
	catch (exception&) {
		assert(true);
	}
	try {
		s.pop(); 
		assert(false); 
	}
	catch (exception&) {
		assert(true);
	}
}

void testPush() {
	cout << "Test push" << endl;
	Stack s;
	for (int i = 0; i < 10; i++) {
		s.push(i);
	}
	assert(s.isEmpty() == false);
	for (int i = -10; i < 20; i++) {
		s.push(i);
	}
	assert(s.isEmpty() == false);
	for (int i = -100; i < 100; i++) {
		s.push(i);
	}
	assert(s.isEmpty() == false);

	for (int i = 10000; i > -10000; i--) {
		s.push(i);
	}
	assert(s.isEmpty() == false);
	assert(s.top() == -9999);
	assert(s.top() != 0);

	assert(s.pop() == -9999);
	assert(s.top() == -9998);
}

void testPop() {
	cout << "Test pop" << endl;
	Stack s;
	for (int i = 0; i < 10; i++) {
		s.push(i);
	}
	assert(s.isEmpty() == false);
	for (int i = -10; i < 20; i++) {
		s.push(i);
	}
	assert(s.isEmpty() == false);
	for (int i = -100; i < 100; i++) {
		s.push(i);
	}
	assert(s.isEmpty() == false);

	for (int i = 10000; i > -10000; i--) {
		s.push(i);
	}
	assert(s.isEmpty() == false);

	
	for (int i = -9999; i <= 10000; i++) {
		assert(s.pop() == i);
	}
	assert(s.isEmpty() == false);
	for (int i = 99; i >= -100; i--) {
		assert(s.pop() == i);
	}
	assert(s.isEmpty() == false);
	for (int i = 19; i >=-10; i--) {
		assert(s.pop() == i);
	}
	assert(s.isEmpty() == false);
	
	for (int i = 9; i >= 0; i--) {
		assert(s.pop() == i);
	}
	assert(s.isEmpty() == true);
	
}

void testQuantity() {
	cout << "Test quantity" << endl;
	Stack s;
	for (int i = 1; i <= 10; i++) {
		for (int j = 30000; j >= -30000; j--) {
			s.push(i + j);
		}
	}

	for (int i = 10; i >= 1; i--) {
		for (int j = -30000; j <= 30000; j++) {			
			assert(s.pop() == i + j);
		}
	}
}

void testPushPop() {
	cout << "Test push pop" << endl;
	Stack s;
	assert(s.isEmpty());
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 100; j++) {
			s.push(j);
		}
		assert(s.isEmpty() == false);
		for (int j = 0; j < 50; j++) {
			assert(s.top() == 100 - j - 1);
			assert(s.pop() == 100 - j - 1);
		}
		assert(s.isEmpty() == false);
	}
	assert(s.isEmpty() == false);
	for (int i = 0; i < 10; i++) {
		for (int j = 50; j < 100; j++) {
			assert(s.top() == 100 - j - 1);
			assert(s.pop() == 100 - j - 1);
		}
	}
	assert(s.isEmpty());
	for (int i = 0; i < 10; i++) {
		s.push(111);
		assert(s.top() == 111);
		assert(s.pop() == 111);
		try {
			s.pop();
			assert(false);
		}
		catch (exception&) {
			assert(true);
		}
		try {
			s.top();
			assert(false);
		}
		catch (exception&) {
			assert(true);
		}
	}
}

void testAllExtended() {
	testCreate();
	testPush();
	testPop();
	testPushPop();
	testQuantity();
}