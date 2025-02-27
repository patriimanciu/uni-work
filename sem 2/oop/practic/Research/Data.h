//
// Created by patri manciu on 26.06.2024.
//

#ifndef RESEARCH_DATA_H
#define RESEARCH_DATA_H
#include <iostream>
#include <vector>
#include "Observer.h"

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

    void update();
};

class Idea {
private:
    std::string name, description, status;
    std::string researcherName;
    int duration;
public:
    Idea(std::string name = "", std::string description = "", std::string status = "", std::string researcher = "", int duration = 0) {
        this->name = name;
        this->description = description;
        this->status = status;
        this->researcherName = researcher;
        this->duration = duration;
    };

    std::string getName() {
        return this->name;
    };

    std::string getDescription() {
        return this->description;
    };

    std::string getStatus() {
        return this->status;
    };

    void setStatus(std::string status) {
        this->status = status;
    };

    std::string getResearcher() {
        return this->researcherName;
    };

    int getDuration() {
        return this->duration;
    };
};

class Data {
private:
    std::vector<Idea*> ideas;
    std::vector<Researcher*> researchers;
public:
    Data() {
        this->readData();
    };
    ~Data() {};

    void addIdea(Idea* idea) {
        this->ideas.push_back(idea);
    };

    void addResearcher(Researcher* researcher) {
        this->researchers.push_back(researcher);
    };

    std::vector<Idea*> getIdeas() {
        return this->ideas;
    };

    std::vector<Researcher*> getResearchers() {
        return this->researchers;
    };

    void readData() {
        this->readIdeas();
        this->readResearchers();
    };
    void readIdeas();
    void readResearchers();
};


#endif //RESEARCH_DATA_H
