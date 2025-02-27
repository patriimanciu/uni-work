//
// Created by patri manciu on 28.05.2024.
//

#include "Domain.h"

Task::Task(std::string description, int duration, int priority) {
    this->description = description;
    this->duration = duration;
    this->priority = priority;
}

std::string Task::getDescription() {
    return this->description;
}

int Task::getPriority() {
    return this->priority;
}

int Task::getDuration() {
    return this->duration;
}

std::string Task::toString() {
    return this->description + " | " + std::to_string(this->duration) + " | " + std::to_string(this->priority);
}

Task::~Task() {
}