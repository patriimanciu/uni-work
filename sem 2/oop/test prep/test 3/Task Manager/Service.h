//
// Created by patri manciu on 28.05.2024.
//

#ifndef TASK_MANAGER_SERVICE_H
#define TASK_MANAGER_SERVICE_H
#include <iostream>
#include "Domain.h"
#include <vector>


class Service {
private:
    std::vector<Task> tasks;
public:
    Service();
    void read();
    std::vector<Task> getAll();
    ~Service();
};


#endif //TASK_MANAGER_SERVICE_H
