//
// Created by patri manciu on 25.05.2024.
//

#include "service.h"
Service::Service() {

    this->read_equations();
}

Service::~Service() {

}

void Service::read_equations() {
    std::ifstream file("../equations.txt");
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file");
    }

    equations.clear(); // Clear any previous data

    double a, b, c;
    char comma; // To read the commas

    while (file >> a >> comma >> b >> comma >> c) {
        Equations eq(a, b, c);
        equations.push_back(eq);
    }

    file.close();
}

void Service::updateEquations(int row, Equations e) {
    std::vector<Equations> eq = this->getAllEq();
    eq[row] = e;
    this->set_equations(eq);
}

void Service::set_equations(std::vector<Equations> eq) {
    this->equations = eq;
}

