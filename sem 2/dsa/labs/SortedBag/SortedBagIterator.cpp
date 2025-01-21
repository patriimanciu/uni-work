#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
	if (bag.head == nullptr) {
        current = nullptr;
    }
    else {
        current = bag.head;
    }
}
// Theta(1)

TComp SortedBagIterator::getCurrent() {
    if (current == nullptr) {
        throw std::out_of_range("Iterator out of range");
    }
    return current->element.first;
}
// Theta(1)

bool SortedBagIterator::valid() {
    return current != nullptr;
}
// Theta(1)

void SortedBagIterator::next() {
    if (current == nullptr) {
        throw std::out_of_range("Iterator out of range");
    }
    current = current->next;
}
// Theta(1)

void SortedBagIterator::first() {
    current = bag.head;
}
// Theta(1)