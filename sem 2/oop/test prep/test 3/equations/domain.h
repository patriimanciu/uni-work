//
// Created by patri manciu on 25.05.2024.
//

#ifndef EQUATIONS_DOMAIN_H
#define EQUATIONS_DOMAIN_H
#include <iostream>

class Equations {
private:
    int a, b, c;
public:
    Equations(int a, int b, int c);
    std::string to_string() const;
    bool real_solutions();
    int getA();
    int getB();
    int getC();
    std::string sol();
    ~Equations();
};


#endif //EQUATIONS_DOMAIN_H
