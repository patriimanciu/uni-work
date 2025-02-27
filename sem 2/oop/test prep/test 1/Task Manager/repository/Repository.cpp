//
// Created by patri manciu on 02.04.2024.
//

#include "Repository.h"

Repository::Repository() {
    this->tasks = DynamicVector<Task>();
}

Repository::~Repository() {
}

void Repository::addTaskRepo(const Task& task) {
    this->tasks.addElementInDynamicVector(task);
    this->sortTasks();
}

DynamicVector<Task> Repository::getAll() {
    return this->tasks;
}

void Repository::sortTasks() {
    for (int i = 0; i < this->tasks.getSizeOfDynamicVector(); i++)
        for (int j = 0; j < this->tasks.getSizeOfDynamicVector(); j++)
            if (this->tasks[i].getDuration() > this->tasks[j].getDuration()) {
                Task temp = this->tasks[i];
                this->tasks[i] = this->tasks[j];
                this->tasks[j] = temp;
            }
}
