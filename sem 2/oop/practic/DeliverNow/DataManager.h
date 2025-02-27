//
// Created by patri manciu on 25.06.2024.
//

#ifndef DELIVERNOW_DATAMANAGER_H
#define DELIVERNOW_DATAMANAGER_H
#include <vector>
#include <iostream>
#include "package.h"
#include "courier.h"

class DataManager {
private:
    std::vector<Package> packages;
    std::vector<Courier> couriers;
    std::string couriersFile;
    std::string packagesFile;
public:
    DataManager(std::string couriersFile = "../couriers.txt", std::string packagesFile = "../packages.txt") {
        this->couriersFile = couriersFile;
        this->packagesFile = packagesFile;
    };
    void readCouriers();
    void readPackages();
    void readData();
    std::vector<Package> getPackages() {
        std::vector<Package> copy;
        for (auto &package : this->packages) {
            copy.push_back(package);
        }
        return copy;
    };
    std::vector<Courier> getCouriers() {
        return this->couriers;
    };
    ~DataManager() = default;

    void addPackage(Package aPackage);
    void updatePackage(Package aPackage);
};


#endif //DELIVERNOW_DATAMANAGER_H
