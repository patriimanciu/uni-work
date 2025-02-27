//
// Created by patri manciu on 02.04.2024.
//

#ifndef TASK_MANAGER_SERVICE_H
#define TASK_MANAGER_SERVICE_H
#include "../repository/Repository.h"

class Service {
private:
    Repository repository;
    int checkUnique(Task task);
    void startUpData();
public:
    Service();
    ~Service();
    int addTaskService(std::string description, int duration, int priority);
    DynamicVector<Task> getAllService();
    DynamicVector<Task> getPriority(int priority);
};

#endif //TASK_MANAGER_SERVICE_H
