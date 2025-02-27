//
// Created by patri manciu on 02.04.2024.
//

#ifndef TASK_MANAGER_TASK_H
#define TASK_MANAGER_TASK_H
#include <iostream>

class Task{
private:
    std::string description;
    int duration;
    int priority;
public:
    Task(std::string description="", int duration=0, int priority=1);
    ~Task();
    std::string getDescription();
    int getDuration();
    int getPriority();
};

#endif //TASK_MANAGER_TASK_H
