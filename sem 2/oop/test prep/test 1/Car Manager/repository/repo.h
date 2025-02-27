//
// Created by patri manciu on 01.04.2024.
//

#ifndef CAR_MANAGER_REPO_H
#define CAR_MANAGER_REPO_H
#include "../DynamicVector.h"
#include "../domain/car.h"

class Repo {
private:
    DynamicVector<Car> cars;
public:
    void addCar(const Car& car);
    DynamicVector<Car> getAll();
    int getCarPosition(std::string model, int year);
    void removeCar(int position);
};

#endif //CAR_MANAGER_REPO_H
