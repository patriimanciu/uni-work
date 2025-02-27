//
// Created by patri manciu on 26.06.2024.
//

#ifndef ARTAUCTION_SUBJECT_H
#define ARTAUCTION_SUBJECT_H
#include <iostream>
#include <vector>
#include "Observer.h"

class Subject {
private:
    std::vector<Observer*> observers;
public:
    Subject(){};
    ~Subject(){ };
    void registerObserver(Observer* obs){
        observers.push_back(obs);
    };
    void notify(){
        for(auto obs: this->observers)
            obs->update();
    };

};


#endif //ARTAUCTION_SUBJECT_H
