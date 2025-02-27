//
// Created by patri manciu on 28.05.2024.
//

#ifndef TASK_MANAGER_DOMAIN_H
#define TASK_MANAGER_DOMAIN_H
#include <iostream>

class Task {
private:
    std::string description;
    int duration;
    int priority;
public:
    Task(std::string description, int duration, int priority);
    std::string getDescription();
    int getPriority();
    int getDuration();
    std::string toString();
    ~Task();

};


#endif //TASK_MANAGER_DOMAIN_H
