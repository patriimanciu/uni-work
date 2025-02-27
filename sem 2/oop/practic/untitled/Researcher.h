//
// Created by patri manciu on 26.06.2024.
//

#ifndef RESEARCH2_RESEARCHER_H
#define RESEARCH2_RESEARCHER_H
#include <iostream>

class Researcher {
private:
    std::string name, position;
public:
    Researcher(std::string name = "", std::string position = "") {
        this->name = name;
        this->position = position;
    };

    std::string getName() {
        return this->name;
    };

    std::string getPosition() {
        return this->position;
    };

};


#endif //RESEARCH2_RESEARCHER_H
