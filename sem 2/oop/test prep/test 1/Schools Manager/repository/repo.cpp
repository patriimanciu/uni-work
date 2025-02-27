//
// Created by patri manciu on 01.04.2024.
//
#include "repo.h"

Repository::Repository() {
    this->schools = DynamicVector<School>();
}

Repository::~Repository() {
}

void Repository::addSchool(const School& school) {
    this->schools.addElementInDynamicVector(school);
}

void Repository::removeSchool(int position) {
    this->schools.removeElementFromDynamicVector(position);
}

int Repository::getPositionByName(std::string name) {
    for (int i = 0; i < this->schools.getSizeOfDynamicVector(); i++)
        if (this->schools.getElement(i).getName() == name)
            return i;
    return -1;
}

DynamicVector<School> Repository::getAll() {
    DynamicVector<School> array = this->schools;
    int n = array.getSizeOfDynamicVector();
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (array[j].getName() > array[j + 1].getName()) {
                School temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
    return array;
}

void Repository::setVisited(int position) {
    this->schools.operator[](position).setVisited();
}

