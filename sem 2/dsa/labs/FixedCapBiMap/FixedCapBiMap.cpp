#include "FixedCapBiMap.h"
#include "FixedCapBiMapIterator.h"

FixedCapBiMap::FixedCapBiMap(int capacity) {
	if (capacity <= 0) {
		throw exception();
	}
	this->capacity = capacity;
	this->mapSize = 0;
	this->elements = new TElem[this->capacity];
}
// BC = WC = TC: Theta(1)

FixedCapBiMap::~FixedCapBiMap() {
	delete[] this->elements;
}
// liniar, BC = WC = TC: Thera(1)

bool FixedCapBiMap::add(TKey c, TValue v){
	if (isFull()) {
		throw exception();
	}
	int count = 0, index = 0;
	while (count < 2 && index < this->mapSize) {
		if (this->elements[index].first == c)
			count++;
		index++;
	}
	if (count == 2) 
		return false;
	this->elements[this->mapSize].first = c;
	this->elements[this->mapSize].second = v;
	this->mapSize++;
	return true;
}
// BC: Theta(1)-when the first 2 keys from the map = c
// WC: Theta(mapSize)-when the key c appears once or 0 times in the map
// TC: O(mapSize)

ValuePair FixedCapBiMap::search(TKey c) const{
	ValuePair result;
	result.first = NULL_TVALUE;
	result.second = NULL_TVALUE;
	int nrFound = 0;
	int index = 0;
	while (nrFound < 2 && index < this->mapSize) {
		if (this->elements[index].first == c) {
            if (nrFound == 0) {
                result.first = this->elements[index].second;
                nrFound++;
            } else {
                result.second = this->elements[index].second;
                nrFound++;
            }
        }
        index++; 
	}
	return result;
}
// BC: Theta(1)-when the first 2 keys from the map = c
// WC: Theta(mapSize)-when the key c appears once or 0 times in the map
// TC: O(mapSize)

bool FixedCapBiMap::remove(TKey c, TValue v){
	int index = 0;
	while (index < this->mapSize) {
		if (this->elements[index].first == c && this->elements[index].second == v) {
            this->elements[index] = this->elements[this->mapSize-1];
            this->mapSize--;
            return true;
        }
        index++;
	}
	return false;
}
// BC: Theta(1)-when the first key is c with the value v
// WC: Theta(mapSize)-when the pair is not in the map or on last position
// TC: O(mapSize)

int FixedCapBiMap::size() const {
	return this->mapSize;
}
// BC = WC = TC: Theta(1)

bool FixedCapBiMap::isEmpty() const{
	return this->mapSize == 0;
}
// BC = WC = TC: Theta(1)

bool FixedCapBiMap::isFull() const {
	return this->mapSize == this->capacity;
}
// BC = WC = TC: Theta(1)

FixedCapBiMapIterator FixedCapBiMap::iterator() const {
	return FixedCapBiMapIterator(*this);
}
// BC = WC = TC: Theta(1)

ValuePair FixedCapBiMap::removeKey(TKey k) {
	ValuePair result;
	result.first = NULL_TVALUE;
	result.second = NULL_TVALUE;
	int index = 0;
	while (index < this->mapSize) {
		if (this->elements[index].first == k) {
			if (result.first == NULL_TVALUE)
				result.first = this->elements[index].second;
			else {
				result.second = this->elements[index].second;
				return result;
			}
			this->elements[index] = this->elements[this->mapSize-1];
            this->mapSize--;
		}
		else
			index++;
	}
	return result;
}