//
// Created by patri manciu on 01.04.2024.
//

#ifndef T1_PATRIIMANCIU_1_DYNAMICVECTOR_H
#define T1_PATRIIMANCIU_1_DYNAMICVECTOR_H

#pragma once
#include <iostream>

template <typename T>
class DynamicVector {
private:
    T *elementsOfDynamicVector;
    int sizeOfDynamicVector, capacityOfDynamicVector;

    void resize(int factorOfResizing = 2);

public:
    DynamicVector(int initialCapacity = 10);

    DynamicVector(const DynamicVector &parameterVector);

    ~DynamicVector();

    DynamicVector &operator=(const DynamicVector &vector);

    void addElementInDynamicVector(const T &elementToBeAdded);

    void removeElementFromDynamicVector(int positionToBeRemoved);

    void updateElementInDynamicVector(int positionToBeUpdated, const T &updatedElement);

    int returnPosition(const T &elementToBeAdded) const;

    size_t getSizeOfDynamicVector() const;

    T &operator[](int indexOfElement);

    T getElement(int positionToGetElementBy) const;
};

template <typename T>
DynamicVector<T>::DynamicVector(int initialCapacity)
{
    this->sizeOfDynamicVector = 0;
    this->capacityOfDynamicVector = initialCapacity;
    this->elementsOfDynamicVector = new T[initialCapacity];
}

template <typename T>
DynamicVector<T>::DynamicVector(const DynamicVector &parameterVector)
{
    this->sizeOfDynamicVector = parameterVector.sizeOfDynamicVector;
    this->capacityOfDynamicVector = parameterVector.capacityOfDynamicVector;
    this->elementsOfDynamicVector = new T[this->capacityOfDynamicVector];
    for (int index = 0; index < this->sizeOfDynamicVector; ++index)
        this->elementsOfDynamicVector[index] = parameterVector.elementsOfDynamicVector[index];
}

template <typename T>
DynamicVector<T>::~DynamicVector()
{
    delete[] this->elementsOfDynamicVector;
}

template <typename T>
DynamicVector<T> &DynamicVector<T>::operator=(const DynamicVector &vector)
{
    if (this == &vector)
        return *this;
    this->sizeOfDynamicVector = vector.sizeOfDynamicVector;
    this->capacityOfDynamicVector = vector.capacityOfDynamicVector;
    delete[] this->elementsOfDynamicVector;
    this->elementsOfDynamicVector = new T[this->capacityOfDynamicVector];
    for (int index = 0; index < this->sizeOfDynamicVector; ++index)
        this->elementsOfDynamicVector[index] = vector.elementsOfDynamicVector[index];
    return *this;
}

template <typename T>
void DynamicVector<T>::addElementInDynamicVector(const T &elementToBeAddedToTheVector)
{
    if (this->sizeOfDynamicVector == this->capacityOfDynamicVector)
        this->resize();
    this->elementsOfDynamicVector[this->sizeOfDynamicVector] = elementToBeAddedToTheVector;
    ++this->sizeOfDynamicVector;
}

template <typename T>
int DynamicVector<T>::returnPosition(const T &elementToBeAddedToTheVector) const
{
    for (int index = 0; index < this->sizeOfDynamicVector; ++index)
        if (this->elementsOfDynamicVector[index] == elementToBeAddedToTheVector)
            return index;
    return -1;
}

template <typename T>
void DynamicVector<T>::removeElementFromDynamicVector(int positionToBeRemoved)
{
    if (positionToBeRemoved < 0 || positionToBeRemoved >= this->sizeOfDynamicVector)
        throw std::invalid_argument("Invalid position! ");
    for (int index = positionToBeRemoved; index < this->sizeOfDynamicVector - 1; ++index)
        this->elementsOfDynamicVector[index] = this->elementsOfDynamicVector[index + 1];
    --this->sizeOfDynamicVector;
}

template <typename T>
size_t DynamicVector<T>::getSizeOfDynamicVector() const
{
    return this->sizeOfDynamicVector;
}

template <typename T>
T &DynamicVector<T>::operator[](int indexOfElement)
{
    return this->elementsOfDynamicVector[indexOfElement];
}

template <typename T>
void DynamicVector<T>::resize(int factorOfResizing)
{
    this->capacityOfDynamicVector *= factorOfResizing;
    T *newResizedVector = new T[this->capacityOfDynamicVector];
    for (int index = 0; index < this->sizeOfDynamicVector; ++index)
        newResizedVector[index] = this->elementsOfDynamicVector[index];
    delete[] this->elementsOfDynamicVector;
    this->elementsOfDynamicVector = newResizedVector;
}

template <typename T>
void DynamicVector<T>::updateElementInDynamicVector(int positionToBeUpdated, const T &updatedElement)
{
    this->elementsOfDynamicVector[positionToBeUpdated] = updatedElement;
}

template <typename T>
T DynamicVector<T>::getElement(int positionToGetElementBy) const
{
    if (positionToGetElementBy < 0 || positionToGetElementBy >= this->sizeOfDynamicVector)
        throw std::invalid_argument("Invalid position! ");
    return this->elementsOfDynamicVector[positionToGetElementBy];
}

#endif //T1_PATRIIMANCIU_1_DYNAMICVECTOR_H
