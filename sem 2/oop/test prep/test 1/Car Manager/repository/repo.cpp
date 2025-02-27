//
// Created by patri manciu on 01.04.2024.
//

#include "repo.h"

void Repo::addCar(const Car& car) {
    this->cars.addElementInDynamicVector(car);
}

DynamicVector<Car> Repo::getAll() {
    return this->cars;
}

int Repo::getCarPosition(std::string model, int year) {
    DynamicVector<Car> array = this->getAll();
    for (int i = 0 ; i < array.getSizeOfDynamicVector(); i++)
        if (array[i].getModel() == model && array[i].getYear() == year)
            return i;
    return -1;
}

void Repo::removeCar(int position) {
    this->cars.removeElementFromDynamicVector(position);
}


