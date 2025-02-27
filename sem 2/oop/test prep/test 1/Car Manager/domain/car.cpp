//
// Created by patri manciu on 01.04.2024.
//

#include "car.h"

std::string Car::getManufacturer() {
    return this->manufacturer;
}

std::string Car::getModel() {
    return this->model;
}

int Car::getYear() {
    return this->year;
}

std::string Car::getColour() {
    return this->colour;
}

Car::Car(std::string manufacturer, const std::string model, int year, const std::string colour) {
    this->manufacturer = manufacturer;
    this->model = model;
    this->year = year;
    this->colour = colour;
}

Car::~Car() {
}
