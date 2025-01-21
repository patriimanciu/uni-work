#include "SortedBag.h"
#include "SortedBagIterator.h"

SortedBag::SortedBag(Relation r) {
	head = nullptr;
    rel = r;
    sizeOfBag = 0;
}

void SortedBag::add(TComp e) {
    if (head == nullptr) {
        Node *current = new Node;
        current->element.first = e;
        current->element.second = 1;
        head = current;
        sizeOfBag++;
    }
    else {
        Node *current = head;
        if (rel(e, head->element.first) && head->element.first != e) {
            Node *newNode = new Node;
            newNode->element.first = e;
            newNode->element.second = 1;
            newNode->next = head;
            newNode->prev = nullptr;
            head->prev = newNode;
            head = newNode;
            sizeOfBag++;
            return;
        }
        while (current != nullptr) {
            if (current->element.first == e) {
                current->element.second++;
                sizeOfBag++;
                return;
            }
            else if (current->next != nullptr && rel(current->element.first, e) && !rel(current->next->element.first, e))
            {
                Node *newNode = new Node;
                newNode->element.first = e;
                newNode->element.second = 1;
                newNode->next = current->next;
                newNode->prev = current;
                current->next->prev = newNode;
                current->next = newNode;
                sizeOfBag++;
                return;
            }
            else if (current->next == nullptr && rel(current->element.first, e)) {
                Node *newNode = new Node;
                newNode->element.first = e;
                newNode->element.second = 1;
                newNode->next = nullptr;
                newNode->prev = current;
                current->next = newNode;
                sizeOfBag++;
                return;
            }
            current = current->next;
        }
    }
}
// Best case: Theta(1)
// Worst case: Theta(n)
// O(n)


bool SortedBag::remove(TComp e) {
    Node *current = head;
    while (current != nullptr) {
        if (current->element.first == e) {
            if (current->element.second > 1) {
                current->element.second--;
            }
            else {
                if (current->prev != nullptr) {
                    current->prev->next = current->next;
                }
                if (current->next != nullptr) {
                    current->next->prev = current->prev;
                }
                if (current == head) {
                    head = current->next;
                }
                delete current;
            }
            sizeOfBag--;
            return true;
        }
        current = current->next;
    }
    return false;
}
// Overall complexity: O(n)


bool SortedBag::search(TComp elem) const {
	if (head == nullptr)
        return false;
    else {
        Node *current = head;
        while (current != nullptr && rel(current->element.first, elem)) {
            if (current->element.first == elem) {
                return true;
            }
            current = current->next;
        }
        return false;
    }
}
// Overall complexity: O(n)


int SortedBag::nrOccurrences(TComp elem) const {
    Node* current = head;
    while (current != nullptr) {
        if (current->element.first == elem) {
            return current->element.second;
        }
        current = current->next;
    }
    return 0;
}
// Overall complexity: O(n)


int SortedBag::size() const {
    if (head == nullptr)
        return 0;
    return sizeOfBag;

}
// Overall complexity: O(1)


bool SortedBag::isEmpty() const {
    return sizeOfBag == 0;
}
// Overall complexity: Theta(1)


SortedBagIterator SortedBag::iterator() const {
	return SortedBagIterator(*this);
}


SortedBag::~SortedBag() {
    if (head == nullptr)
        return;
	Node *current = head;
    while (current != nullptr) {
        Node *aux = current->next;
        delete current;
        current = aux;
    }
}
// Overall complexity: O(n)


int SortedBag::removeOccurrences(int nr, TComp elem) {
    if (nr < 0)
        throw std::invalid_argument("Number of occurrences to remove must be positive");
    Node* current = head;
    int removed = 0;
    while (current != nullptr) {
        if (current->element.first == elem) {
            if (current->element.second <= nr) {
                removed += current->element.second;
                sizeOfBag -= current->element.second;
                if (current == head) {
                    head = current->next;
                    delete current;
                    break;
                }
                else {
                    current->prev->next = current->next;
                    if (current->next != nullptr) {
                        current->next->prev = current->prev;
                    }
                    delete current;
                    break;
                }
            }
            else {
                current->element.second -= nr;
                removed += nr;
                sizeOfBag -= nr;
            }
        }
        current = current->next;
    }
    return removed;
}
// Overall complexity: O(n)
// Best case: Theta(1)
// Worst case: Theta(n)