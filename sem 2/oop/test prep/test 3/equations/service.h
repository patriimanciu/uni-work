//
// Created by patri manciu on 25.05.2024.
//

#ifndef EQUATIONS_SERVICE_H
#define EQUATIONS_SERVICE_H

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include "domain.h"

class Service {
private:
    std::vector<Equations> equations;
public:
    Service();
    void read_equations();
    void set_equations(std::vector<Equations> eq);
    void updateEquations(int row, Equations e);
    std::vector<Equations> getAllEq() { return this->equations; }
    ~Service();
};


#endif //EQUATIONS_SERVICE_H
