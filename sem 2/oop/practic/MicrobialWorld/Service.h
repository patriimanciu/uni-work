//
// Created by patri manciu on 26.06.2024.
//

#ifndef MICROBIALWORLD_SERVICE_H
#define MICROBIALWORLD_SERVICE_H
#include "Bacterium.h"
#include "Biologist.h"
#include <iostream>
#include <vector>

class Service {
private:
    std::vector<Bacterium> bacteria;
    std::vector<Biologist> biologists;
    void readBiologists();
    void readBacteria();
    void readData() {
        readBiologists();
        readBacteria();
    }
public:
    Service() { readData(); };
    ~Service() = default;
    std::vector<Bacterium> getBacteria() {
        std::vector<Bacterium> copy;
        for (auto &bacterium : this->bacteria) {
            copy.push_back(bacterium);
        }
        return copy;
    };
    std::vector<Bacterium> getBySpecies(std::string species);
    std::vector<Biologist> getBiologists() {
        std::vector<Biologist> copy;
        for (auto &biologist : this->biologists) {
            copy.push_back(biologist);
        }
        return copy;
    };

};


#endif //MICROBIALWORLD_SERVICE_H
