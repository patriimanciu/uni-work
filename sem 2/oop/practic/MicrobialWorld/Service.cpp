//
// Created by patri manciu on 26.06.2024.
//

#include "Service.h"
#include <fstream>
#include <sstream>

void Service::readBiologists() {
    std::ifstream file("../biologists.txt");
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file");
    }
    this->biologists.clear();
    std::string name;
    std::vector<std::string> bacteriaRead;
    std::string line;
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        iss >> name;
        std::string bact;
        while (iss >> bact) {
            bacteriaRead.push_back(bact);
        }
        Biologist b(name, bacteriaRead);
        this->biologists.push_back(b);
    }

}

void Service::readBacteria() {
    std::ifstream file("../bacteria.txt");
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file");
    }
    this->bacteria.clear();
    std::string name, sp;
    int size;
    std::vector<std::string> diseases;
    std::string line;
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        iss >> name;
        iss >> sp;
        iss >> size;
        std::string d;
        while (iss >> d) {
            diseases.push_back(d);
        }
        Bacterium b(name, sp, size, diseases);
        this->bacteria.push_back(b);
    }
    file.close();
}


std::vector<Bacterium> Service::getBySpecies(std::string species) {
    std::vector<Bacterium> result;
    for (auto &bacterium : this->bacteria) {
        if (bacterium.getSpecies() == species) {
            result.push_back(bacterium);
        }
    }
    return result;
}
