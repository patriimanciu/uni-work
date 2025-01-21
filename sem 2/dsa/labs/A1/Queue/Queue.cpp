#include "Queue.h"
#include <exception>
#include <iostream>

using namespace std;


Queue::Queue() {
    capacity = INITIAL_CAPACITY;
	elements = new TElem [capacity];
    size = 0;
    front = 0;
    rear = -1;
}
// BC = WC = TC: Theta(1)

void Queue::push(TElem elem) {
	if (capacity == size)
        resize();
    rear = (rear + 1) % capacity;
    elements[rear] = elem;
    size++;
}
// BC = WC = TC: Theta(1)

TElem Queue::top() const {
	if (isEmpty())
        throw std::exception();
    return elements[front];
}
// BC = WC = TC: Theta(1)

TElem Queue::pop() {
    if (isEmpty())
        throw std::exception();
    TElem frontElem = elements[front];
    front = (front + 1) % capacity;
    size--;
    return frontElem;
}
// BC = WC = TC: Theta(1)

bool Queue::isEmpty() const {
	return size == 0;
}
// BC = WC = TC: Theta(1)


Queue::~Queue() {
	delete []elements;
}
// BC = WC = TC: Theta(1)

void Queue::resize() {
    TElem *newArray = new TElem [capacity * 2];
    for (int i = 0; i < capacity; i++)
        newArray[i] = elements[(front + i) % capacity];
    delete []elements;
    elements = newArray;
    capacity = capacity * 2;
    front = 0;
    rear = size - 1;
}
// BC = WC = TC: Theta(capacity)

