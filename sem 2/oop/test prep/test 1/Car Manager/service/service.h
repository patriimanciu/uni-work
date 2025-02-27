//
// Created by patri manciu on 01.04.2024.
//

#ifndef CAR_MANAGER_SERVICE_H
#define CAR_MANAGER_SERVICE_H
#include "../repository/repo.h"

class Service {
private:
    Repo repository;
    int checkUnique(Car &car);
public:
    int addCar(std::string manufacturer, std::string model, int year, std::string colour);
    DynamicVector<Car> getAll();
    void removeCar(std::string model, int year);

    DynamicVector<Car> getVintage();
};

#endif //CAR_MANAGER_SERVICE_H
