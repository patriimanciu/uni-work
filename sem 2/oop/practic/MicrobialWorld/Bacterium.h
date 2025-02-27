//
// Created by patri manciu on 26.06.2024.
//

#ifndef MICROBIALWORLD_BACTERIUM_H
#define MICROBIALWORLD_BACTERIUM_H
#include <iostream>
#include <vector>

class Bacterium {
private:
    std::string name, species;
    int size;
    std::vector<std::string> diseases;
public:
    Bacterium(std::string name = "", std::string species = "", int size = 0, std::vector<std::string> diseases = {}) {
        this->name = name;
        this->species = species;
        this->size = size;
        this->diseases = diseases;
    }
    ~Bacterium() {}
    std::string getName() {
        return this->name;
    }
    std::string getSpecies() {
        return this->species;
    }
    int getSize() {
        return this->size;
    }
    std::vector<std::string> getDiseases() {
        return this->diseases;
    }

    std::string getDiseasesStr() {
        std::string diseasesStr = "";
        for (auto &disease : this->diseases) {
            diseasesStr += disease + ", ";
        }
        return diseasesStr;
    }
};


#endif //MICROBIALWORLD_BACTERIUM_H
