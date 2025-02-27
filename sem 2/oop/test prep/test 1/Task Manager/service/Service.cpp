//
// Created by patri manciu on 02.04.2024.
//

#include "Service.h"

Service::Service() {
    this->repository = Repository();
    this->startUpData();
}

Service::~Service() {
}

int Service::addTaskService(std::string description, int duration, int priority) {
    Task task = Task(description, duration, priority);
    if (this->checkUnique(task) == 1)
        return 1;
    this->repository.addTaskRepo(task);
    return 0;
}

int Service::checkUnique(Task task) {
    DynamicVector<Task> array = this->repository.getAll();
    for (int i = 0; i < array.getSizeOfDynamicVector(); i++)
        if (array[i].getDescription() == task.getDescription())
            return 1;
    return 0;
}

DynamicVector<Task> Service::getAllService() {
    return this->repository.getAll();
}

DynamicVector<Task> Service::getPriority(int priority) {
    DynamicVector<Task> array = this->getAllService();
    DynamicVector<Task> newArray = DynamicVector<Task>();
    for (int i = 0; i < array.getSizeOfDynamicVector(); i++)
        if (array[i].getPriority() < priority)
            newArray.addElementInDynamicVector(array[i]);
    return newArray;
}

void Service::startUpData() {
    this->repository.addTaskRepo(Task("Solve_OOP_assignment", 120, 1));
    this->repository.addTaskRepo(Task("Respond_to_emails", 45, 2));
    this->repository.addTaskRepo(Task("Eat_sushi", 30, 3));
    this->repository.addTaskRepo(Task("Visit_dad", 240, 1));
    this->repository.addTaskRepo(Task("Buy_jacket", 120, 2));
}
