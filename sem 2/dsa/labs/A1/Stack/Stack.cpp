#include "Stack.h"
#include <exception>


using namespace std;


Stack::Stack() {
	capacity = INITIAL_CAPACITY;
    size = 0;
    elements = new TElem[capacity];
}
// BC = WC = TC: Theta(1)


void Stack::push(TElem e) {
    if (capacity == size)
        resize();
    elements[size++] = e;
}
// BC = WC = TC: Theta(1)

TElem Stack::top() const {
    // throws exception if the stack is empty
    if (isEmpty())
        throw std::exception();
	return elements[size - 1];
}
// BC = WC = TC: Theta(1)

TElem Stack::pop() {
    if (isEmpty())
        throw std::exception();
    TElem popped = elements[size - 1];
    size--;
    return popped;
}
// BC = WC = TC: Theta(1)

bool Stack::isEmpty() const {
	return size == 0;
}
// BC = WC = TC: Theta(1)


Stack::~Stack() {
	delete [] elements;
}
// BC = WC = TC: Theta(1)

void Stack::resize() {
    TElem *newElems = new TElem [capacity * 2];
    for (int i = 0; i < size; i++)
        newElems[i] = elements[i];
    delete [] elements;
    elements = newElems;
    capacity = capacity * 2;
}

bool Stack::search(TElem e) const {
    for (int i = 0; i < size; i++)
        if (elements[i] == e)
            return true;
    return false;
}
// BC =
// WC = TC: O(size)