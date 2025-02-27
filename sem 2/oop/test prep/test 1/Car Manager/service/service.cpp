//
// Created by patri manciu on 01.04.2024.
//

#include "service.h"

int Service::addCar(std::string manufacturer, std::string model, int year, std::string colour) {
    Car car = Car(manufacturer, model, year, colour);
    int unique = this->checkUnique(car);
    if (unique == 1)
        throw std::invalid_argument("The car already exists.");
    this->repository.addCar(car);
    return 0;
}

DynamicVector<Car> Service::getAll() {
    return this->repository.getAll();
}

int Service::checkUnique(Car &car) {
    DynamicVector<Car> array = this->getAll();
    for (int i = 0 ; i < array.getSizeOfDynamicVector(); i++)
        if (array[i].getModel() == car.getModel() && array[i].getYear() == car.getYear())
            return 1;
    return 0;
}

void Service::removeCar(std::string model, int year) {
    int i = this->repository.getCarPosition(model, year);
    if (i == -1)
        throw std::invalid_argument("The car doesn't exist.");
    this->repository.removeCar(i);
}

DynamicVector<Car> Service::getVintage() {
    DynamicVector<Car> array = this->getAll();
    DynamicVector<Car> newArray = DynamicVector<Car>();
    for (int i = 0 ; i < array.getSizeOfDynamicVector(); i++)
        if (array[i].getYear() <= 2023 - 45)
            newArray.addElementInDynamicVector(array[i]);
    return newArray;
}
