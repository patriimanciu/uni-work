//
// Created by patri manciu on 26.06.2024.
//

#ifndef MICROBIALWORLD_BIOLOGIST_H
#define MICROBIALWORLD_BIOLOGIST_H
#include <iostream>
#include <vector>

class Biologist {
private:
    std::string name;
    std::vector<std::string> speciesList;
public:
    Biologist(std::string name = "", std::vector<std::string> speciesList = {}) {
        this->name = name;
        this->speciesList = speciesList;
    }
    ~Biologist() {}
    std::string getName() {
        return this->name;
    }
    std::vector<std::string> getSpeciesList() {
        return this->speciesList;
    }
};


#endif //MICROBIALWORLD_BIOLOGIST_H
