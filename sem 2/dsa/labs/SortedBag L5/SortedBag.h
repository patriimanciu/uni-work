#pragma once
//DO NOT INCLUDE SORTEDBAGITERATOR

//DO NOT CHANGE THIS PART
typedef int TComp;
typedef TComp TElem;
typedef bool(*Relation)(TComp, TComp);
#define NULL_TCOMP -11111;
#define MAX_FREQUENCY 1000

class SortedBagIterator;

class SortedBag {
	friend class SortedBagIterator;

private:
    struct TreeNode {
        TComp info;
        int left;
        int right;
    };

    TreeNode* tree; // an array of TreeNodes
    int capacity;
    int root;
    int firstEmpty;
    int* nextEmpty;
    int sizeOfTree;
    Relation relation;
    void resize();
    int createNode(TComp e);

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

	//checks if the sorted bag is empty
	bool isEmpty() const;

    // returns the number of elements with minimum frequency
    // if the sorted bag is empty, it returns 0
    int elementsWithMinimumFrequency() const;

	//destructor
	~SortedBag();
};