//
// Created by patri manciu on 26.06.2024.
//

#ifndef RESEARCH2_SERVICE_H
#define RESEARCH2_SERVICE_H

#include "Idea.h"
#include "Researcher.h"
#include <vector>

class Service {
private:
    std::vector<Idea> ideas;
    std::vector<Researcher> researchers;
    void readData() {
        this->readIdeas();
        this->readResearchers();
    }
    void readIdeas();
    void readResearchers();
public:
    Service() { this->readData(); }
    std::vector<Idea> getIdeas() { return this->ideas; }
    std::vector<Researcher> getResearchers() { return this->researchers; }
    void addIdea(Idea& i);
    void acceptIdea(int index);
    std::vector<Idea> getAcceptedIdeas(std::string name);
    void setDescription(int index, std::string descr){ this->ideas[index].setDescription(descr); };
    ~Service() {}
};


#endif //RESEARCH2_SERVICE_H
