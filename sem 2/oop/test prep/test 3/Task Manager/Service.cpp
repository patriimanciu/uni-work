//
// Created by patri manciu on 28.05.2024.
//

#include "Service.h"
#include <fstream>
#include <sstream>

Service::Service() {
}

std::vector<Task> Service::getAll() {
    for (int i = 0; i < this->tasks.size(); i++) {
        for (int j = i + 1; j < this->tasks.size(); j++) {
            if (this->tasks[i].getPriority() > this->tasks[j].getPriority()) {
                Task aux = this->tasks[i];
                this->tasks[i] = this->tasks[j];
                this->tasks[j] = aux;
            }
            else if (this->tasks[i].getPriority() == this->tasks[j].getPriority() && this->tasks[i].getDuration() > this->tasks[j].getDuration()) {
                Task aux = this->tasks[i];
                this->tasks[i] = this->tasks[j];
                this->tasks[j] = aux;
            }
        }
    }
    return this->tasks;
}

Service::~Service() {
}

std::vector<std::string> parce(std::string line, char del) {
    std::vector<std::string> result;
    std::stringstream ss(line);
    std::string part;
    while (std::getline(ss, part, del)) {
        result.push_back(part);
    }
    return result;
}


void Service::read() {
    std::ifstream file("../input.txt");
    tasks.clear();
    std::string line;
    while (std::getline(file, line)) {
        std::vector<std::string> res = parce(line, '|');
        if (res.size() == 3) {
            std::string desc = res[0];
            int duration = std::stoi(res[1]);
            int priority = std::stoi(res[2]);
            Task t = Task(desc, duration, priority);
            tasks.push_back(t);
        }
    }
}
