//
// Created by patri manciu on 02.04.2024.
//

#ifndef TASK_MANAGER_REPOSITORY_H
#define TASK_MANAGER_REPOSITORY_H
#include "../DynamicVector.h"
#include "../domain/Task.h"

class Repository {
private:
    DynamicVector<Task> tasks;
    void sortTasks();
public:
    Repository();
    ~Repository();
    void addTaskRepo(const Task& task);
    DynamicVector<Task> getAll();
};

#endif //TASK_MANAGER_REPOSITORY_H
