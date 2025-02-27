//
// Created by patri manciu on 01.04.2024.
//

#ifndef CAR_MANAGER_CAR_H
#define CAR_MANAGER_CAR_H
#include <iostream>

class Car {
private:
    std::string manufacturer, model;
    int year;
    std::string colour;
public:
    Car(std::string manufacturer="", std::string model="", int year = 2023, std::string colour="");
    ~Car();
    std::string getManufacturer();
    std::string getModel();
    int getYear();
    std::string getColour();
};

#endif //CAR_MANAGER_CAR_H
