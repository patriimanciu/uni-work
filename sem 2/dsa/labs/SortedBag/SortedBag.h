#pragma once
#include <iostream>
//DO NOT INCLUDE SORTEDBAGITERATOR

//DO NOT CHANGE THIS PART
typedef int TComp;
typedef TComp TElem;
typedef bool(*Relation)(TComp, TComp);
typedef std::pair<TElem, int> Pair;
#define NULL_TCOMP -11111;

class SortedBagIterator;

struct Node {
    Pair element;
    Node* next;
    Node* prev;
};

class SortedBag {
	friend class SortedBagIterator;

private:
	int sizeOfBag;
    Node* head;
    Relation rel;

public:
	//constructor
	SortedBag(Relation r);

	//adds an element to the sorted bag
	void add(TComp e);

	//removes one occurence of an element from a sorted bag
	//returns true if an eleent was removed, false otherwise (if e was not part of the sorted bag)
	bool remove(TComp e);

	//checks if an element appearch is the sorted bag
	bool search(TComp e) const;

	//returns the number of occurrences for an element in the sorted bag
	int nrOccurrences(TComp e) const;

	//returns the number of elements from the sorted bag
	int size() const;

	//returns an iterator for this sorted bag
	SortedBagIterator iterator() const;

    // removes nr occurances of elem. if the element appears less than nr times, it removes all occurances
    // returns the number of times the element was removed
    // throws an exception if nr is negative
    int removeOccurrences(int nr, TComp elem);

	//checks if the sorted bag is empty
	bool isEmpty() const;

	//destructor
	~SortedBag();
};