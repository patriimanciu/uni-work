//
// Created by patri manciu on 26.06.2024.
//

#ifndef RESEARCH2_IDEA_H
#define RESEARCH2_IDEA_H
#include <iostream>
#pragma once



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
    inline bool operator < (const Idea& i) const { return this->duration<i.duration; } ;

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

    void setDescription(std::string description) {
        this->description = description;
    };

    std::string getResearcher() {
        return this->researcherName;
    };

    int getDuration() {
        return this->duration;
    };
};


#endif //RESEARCH2_IDEA_H
