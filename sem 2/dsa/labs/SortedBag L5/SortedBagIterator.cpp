#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
    this->stackSize = b.sizeOfTree;
    this->stack = new int[this->stackSize];
    first();
}

TComp SortedBagIterator::getCurrent() {
	if (!this->valid()) {
        throw std::exception();
    }
    return this->bag.tree[this->current].info;
}

bool SortedBagIterator::valid() {
	    return this->current != -1;
}

void SortedBagIterator::next() {
    if (!this->valid()) {
        throw std::exception();
    }
    int node = this->stack[this->top--];
    int right = this->bag.tree[node].right;
    while (right != -1) {
        this->stack[++this->top] = right;
        right = this->bag.tree[right].left;
    }
    if (this->top != -1) {
        this->current = this->stack[this->top];
    }
    else {
        this->current = -1;
    }
}

void SortedBagIterator::first() {
    top = -1;
    current = bag.root;

    // clear the stack
    while (current != -1) {
        stack[++top] = current;
        current = bag.tree[current].left;
    }

    // check if we have elements in the stack
    if (top != -1) {
        current = stack[top];
    } else {
        current = -1;
    }
}

