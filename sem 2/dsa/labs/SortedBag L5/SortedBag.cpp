#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <iostream>

SortedBag::SortedBag(Relation r) {
	this->relation = r;
    this->capacity = 10;
    this->tree = new TreeNode[this->capacity];
    this->nextEmpty = new int[this->capacity];
    this->root = -1;
    this->firstEmpty = 0;
    this->sizeOfTree = 0;
    for (int i = 0; i < this->capacity; i++) {
        this->tree[i].left = -1;
        this->tree[i].right = -1;
        this->tree[i].info = NULL_TCOMP;
        this->nextEmpty[i] = i + 1;
    }
    this->nextEmpty[this->capacity - 1] = -1;
}

void SortedBag::add(TComp e) {
	if (this->sizeOfTree == this->capacity)
        this->resize();
    int newNode = this->createNode(e);
    if (root == -1) {
        this->root = newNode;
    }
    else {
        int currentNode = this->root;
        int parent = -1;
        while (currentNode != -1) {
            parent = currentNode;
            if (this->relation(e, this->tree[currentNode].info)) {
                currentNode = this->tree[currentNode].left;
            }
            else {
                currentNode = this->tree[currentNode].right;
            }
        }
        if (this->relation(e, this->tree[parent].info)) {
            if (this->tree[parent].left != -1) {
                this->tree[newNode].left = this->tree[parent].left;
            }
            this->tree[parent].left = newNode;
//            std::cout << "added " << e << " left \n";
        }
        else {
            this->tree[parent].right = newNode;
//            std::cout << "added " << e << " right of " << parent << "\n";
        }
    }
    this->sizeOfTree++;
//    std::cout << "added " << e << "\n";
}


bool SortedBag::remove(TComp e) {
	int current = root;
    int parent = -1;
    while (current != -1 && this->tree[current].info != e) {
        parent = current;
        if (this->relation(e, this->tree[current].info)) {
            current = this->tree[current].left;
        } else {
            current = this->tree[current].right;
        }
    }
    if (current == -1) {
        return false;
    }

    if (this->tree[current].left == -1 || this->tree[current].right == -1) {
        int child;
        if (this->tree[current].left == -1) {
            child = this->tree[current].right;
        } else {
            child = this->tree[current].left;
        }
        if (parent == -1) {
            root = child;
        } else {
            if (this->tree[parent].left == current) {
                this->tree[parent].left = child;
            } else {
                this->tree[parent].right = child;
            }
        }
        this->nextEmpty[current] = this->firstEmpty;
        this->firstEmpty = current;
    } else {
        int mostLeft = this->tree[current].right;
        int mostLeftParent = current;
        while (this->tree[mostLeft].left != -1) {
            mostLeftParent = mostLeft;
            mostLeft = this->tree[mostLeft].left;
        }
        this->tree[current].info = this->tree[mostLeft].info;
        if (mostLeftParent == current) {
            this->tree[current].right = this->tree[mostLeft].right;
        } else {
            this->tree[mostLeftParent].left = this->tree[mostLeft].right;
        }
        this->nextEmpty[mostLeft] = this->firstEmpty;
        this->firstEmpty = mostLeft;
    }
    this->sizeOfTree--;
//    std::cout << "removed " << e << '\n';
    return true;
}


bool SortedBag::search(TComp elem) const {
	int current = root;
    while (current != -1) {
        if (this->tree[current].info == elem) {
            return true;
        } else if (this->relation(elem, this->tree[current].info)) {
            current = this->tree[current].left;
        } else {
            current = this->tree[current].right;
        }
    }
    return false;
}


int SortedBag::nrOccurrences(TComp elem) const {
    int current = root;
    int count = 0;

    while (current != -1) {
        if (this->tree[current].info == elem) {
            count++;
            // Continue to the left subtree to check for duplicates
            current = this->tree[current].left;
        } else if (this->relation(elem, this->tree[current].info)) {
            current = this->tree[current].left;
        } else {
            current = this->tree[current].right;
        }
    }
    return count;
}


int SortedBag::size() const {
    return this->sizeOfTree;
}


bool SortedBag::isEmpty() const {
	return this->sizeOfTree == 0;
}


SortedBagIterator SortedBag::iterator() const {
	return SortedBagIterator(*this);
}


SortedBag::~SortedBag() {
	delete[] this->tree;
    delete[] this->nextEmpty;
}

void SortedBag::resize() {
    int oldCapacity = capacity;
    capacity *= 2;
    auto* newTree = new TreeNode[capacity];
    int* newNextEmpty = new int[capacity];
    for (int i = 0; i < capacity; ++i) {
        if (i < this->sizeOfTree) {
            newTree[i] = tree[i];
        } else {
            newTree[i].left = -1;
            newTree[i].right = -1;
        }
        if (i < oldCapacity) {
            newNextEmpty[i] = nextEmpty[i];
        } else {
            newNextEmpty[i] = i + 1;
        }
    }
    newNextEmpty[capacity - 1] = -1;
    delete[] tree;
    delete[] nextEmpty;
    tree = newTree;
    nextEmpty = newNextEmpty;
    firstEmpty = oldCapacity;
}

int SortedBag::createNode(TComp e) {
    int newNode = this->firstEmpty;
    this->tree[newNode].info = e;
    this->tree[newNode].left = -1;
    this->tree[newNode].right = -1;
    this->firstEmpty = this->nextEmpty[this->firstEmpty];
    return newNode;
}

int SortedBag::elementsWithMinimumFrequency() const {
    if (this->sizeOfTree == 0) {
        return 0;
    }
    int minFrequency = MAX_FREQUENCY;
    int *elements = new int[this->sizeOfTree], noElements = 0;
    int index = 0, passed = 0;
    while (passed < this->sizeOfTree) {
        int frequency = this->nrOccurrences(this->tree[elements[passed]].info);
        if (frequency < minFrequency) {
            minFrequency = frequency;
            noElements = 1;
        }
        else if (frequency == minFrequency) {
            noElements++;
        }
        if (this->tree[passed].left != -1) {
            index++;
            elements[index] = this->tree[passed].left;
        }
        if (this->tree[passed].right != -1) {
            index++;
            elements[index] = this->tree[passed].right;
        }
        passed++;
    }
    return noElements;
}

