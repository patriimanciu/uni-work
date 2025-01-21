#pragma once
//DO NOT CHANGE THIS PART
typedef int TElem;
#define NULL_TELEM -111111
#define INITIAL_CAPACITY 10

class Stack
{
private:
    int capacity;
    int size;
    TElem* elements;
    void resize();
	
public:

	//constructor
	Stack();
	
	//pushes an element to the top of the Stack
	void push(TElem e);
	
	//returns the element from the top of the Stack
	//throws exception if the stack is empty
	TElem top() const;
	   
	//removes and returns the element from the top of the Stack
	//throws exception if the stack is empty
	TElem pop();
	   
	//checks if the stack is empty
	bool isEmpty() const;
	
	//destructor
	~Stack();

    bool search(TElem e) const;
};

