//
// Created by patri manciu on 25.06.2024.
//

#include "DataManager.h"
#include <fstream>
#include <iostream>
#include <sstream>


std::istream& operator>>(std::ifstream& file, Courier& c) {
    std::string name;
    int x, y, r;
    std::string unparcedStreets;
    std::vector<std::string> streets;
    if (std::getline(file, name, ',') &&
    std::getline(file, unparcedStreets, ',') &&
    file >> x && file.ignore() && file >> y && file.ignore() && file >> r && file.ignore()) {
        std::string street;
        std::istringstream iss(unparcedStreets);
        while (std::getline(iss, street, ';')) {
            streets.push_back(street);
        }
        c = Courier(name, int(x), int(y), int(r), streets);
    }
    return file;
}

void DataManager::readData() {
    this->readCouriers();
    this->readPackages();
}

void DataManager::readCouriers() {
    std::ifstream file(this->couriersFile);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file");
    }
    this->couriers.clear();
    Courier c;
    while (file >> c) {
        this->couriers.push_back(c);
    }
    file.close();
}

std::istream& operator>>(std::ifstream& file, Package& p) {
    std::string recipient, street;
    int number, x, y;
    int status;
    if (std::getline(file, recipient, ',') &&
    std::getline(file, street, ',') &&
    file >> number && file.ignore() && file >> x && file.ignore() && file >> y && file.ignore() && file >> status && file.ignore() && file.ignore()) {
        if (status == 1)
            p = Package(recipient, street, int(number), int(x), int(y), true);
        else
            p = Package(recipient, street, int(number), int(x), int(y), false);
    }
    return file;
}

void DataManager::readPackages() {
    std::ifstream file(this->packagesFile);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file");
    }
    this->packages.clear();
    Package p;
    while (file >> p) {
        this->packages.push_back(p);
    }
    file.close();
}

void DataManager::addPackage(Package aPackage) {
    this->packages.push_back(aPackage);
}

void DataManager::updatePackage(Package aPackage) {
    for (auto it = this->packages.begin(); it != this->packages.end(); ++it) {
        if (it->getRecipient() == aPackage.getRecipient() && it->getAddress() == aPackage.getAddress()) {
            *it = aPackage;
            break;
        }
    }
}
