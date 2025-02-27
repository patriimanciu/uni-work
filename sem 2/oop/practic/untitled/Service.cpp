//
// Created by patri manciu on 26.06.2024.
//

#include "Service.h"
#include <fstream>

void Service::readIdeas() {
    std::ifstream file("../ideas.txt");
    std::string name, description, status, researcherName;
    int years;
    this->ideas.clear();
    while (file >> name >> description >> status >> researcherName >> years) {
        Idea idea = Idea(name, description, status, researcherName, years);
        this->ideas.push_back(idea);
    }
    file.close();
}

void Service::readResearchers() {
    std::ifstream file("../researchers.txt");
    std::string name, position;
    this->researchers.clear();
    while (file >> name >> position) {
        auto researcher = Researcher(name, position);
        this->researchers.push_back(researcher);
    }
    file.close();
}

void Service::addIdea(Idea &i) {
    this->ideas.push_back(i);
    sort(this->ideas.begin(), this->ideas.end());
}

void Service::acceptIdea(int index) {
    this->ideas[index].setStatus("accepted");
}

std::vector<Idea> Service::getAcceptedIdeas(std::string name) {
    std::vector<Idea> acceptedIdeas;
    for (auto i : this->ideas)
        if (i.getName() == name && i.getStatus() == "accepted")
            acceptedIdeas.push_back(i);
    return acceptedIdeas;
}
