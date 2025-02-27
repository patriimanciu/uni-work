//
// Created by patri manciu on 02.04.2024.
//

#include "Task.h"

Task::Task(std::string description, int duration, int priority) {
    this->description = description;
    this->duration = duration;
    this->priority = priority;
}

Task::~Task() {
}

std::string Task::getDescription() {
    return this->description;
}

int Task::getDuration() {
    return this->duration;
}

int Task::getPriority() {
    return this->priority;
}
