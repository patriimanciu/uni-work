//
// Created by patri manciu on 25.05.2024.
//

#include "domain.h"

Equations::Equations(int a, int b, int c) {
    this->a = a;
    this->b = b;
    this->c = c;
}

Equations::~Equations() {
}

std::string Equations::to_string() const {
    if (this->a == 0) {
        if (this->c == 0)
            return std::to_string(b) + "x = 0";
        else
            return std::to_string(b) + "x + " + std::to_string(c) + " = 0";
    }
    else {
        if (this->b == 0) {
            if (this->c == 0)
                return std::to_string(a) + "x^2 = 0";
            else
                return std::to_string(a) + "x^2 + " + std::to_string(c) + " = 0";

        }
        else {
            if (this->c == 0)
                return std::to_string(a) + "x^2 = 0";
            else
                return std::to_string(this->a) + "x^2 + " + std::to_string(this->b) + "x + " + std::to_string(this->c) + " = 0";

        }
    }
}

bool Equations::real_solutions() {
    double delta = this->b * this->b - 4 * this->a * this->c;
    return delta >= 0;
}

int Equations::getA() {
    return this->a;
}

int Equations::getB() {
    return this->b;
}

int Equations::getC() {
    return this->c;
}

std::string Equations::sol() {
    if (this->real_solutions()) {
        double delta = this->b * this->b - 4 * this->a * this->c;
        double x1 = (-this->b + sqrt(delta)) / (2 * this->a);
        double x2 = (-this->b - sqrt(delta)) / (2 * this->a);
        return "x1 = " + std::to_string(x1) + " | x2 = " + std::to_string(x2);
    }
    else {
        double delta = this->b * this->b - 4 * this->a * this->c;
        double realPart = - this->b / (2 * this->a);
        double imaginaryPart = std::sqrt(-delta) / (2 * a);
        return "x = " + std::to_string(realPart) + " ± i" + std::to_string(imaginaryPart);
    }
}