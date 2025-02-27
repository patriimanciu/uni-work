//
// Created by patri manciu on 26.06.2024.
//

#include "Data.h"
#include <fstream>

void Data::readIdeas() {
    std::ifstream file("../ideas.txt");
    std::string name, description, status, researcherName;
    int years;
    this->ideas.clear();
    while (file >> name >> description >> status >> researcherName >> years) {
        Idea *idea = new Idea(name, description, status, researcherName, years);
        this->ideas.push_back(idea);
    }
    file.close();
}

void Data::readResearchers() {
    std::ifstream file("../researchers.txt");
    std::string name, position;
    this->researchers.clear();
    while (file >> name >> position) {
        auto *researcher = new Researcher(name, position);
        this->researchers.push_back(researcher);
    }
    file.close();
}

void Researcher::update() {
}
