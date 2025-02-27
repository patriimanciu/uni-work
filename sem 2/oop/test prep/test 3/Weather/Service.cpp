//
// Created by patri manciu on 28.05.2024.
//

#include "Service.h"
#include <fstream>
#include <sstream>

Service::Service() {
}

std::vector<std::string> split(std::string line, char del) {
    std::vector<std::string> result;
    std::stringstream ss(line);
    std::string item;
    while (std::getline(ss, item, del)) {
        result.push_back(item);
    }
    return result;
}

void Service::read() {
    std::ifstream file("../input.txt");
    weatherList.clear();
    std::string line;
    while (std::getline(file, line)) {
        std::vector<std::string> fields = split(line, ';');
        if (fields.size() == 5) {
            int start = std::stoi(fields[0]);
            int end = std::stoi(fields[1]);
            int temperature = std::stoi(fields[2]);
            int precipitation = std::stoi(fields[3]);
            std::string description = fields[4];
            Weather w = Weather(start, end, temperature, precipitation, description);
            weatherList.push_back(w);
        }
    }
}

std::vector<Weather> Service::getAll() {
    std::vector<Weather> w = this->weatherList;
    for (int i = 0; i < w.size(); i++)
        for (int j = i; j < w.size(); ++j) {
            if (w[i].getStart() > w[j].getStart())
                std::swap(w[i], w[j]);
            else if (w[i].getStart() == w[j].getStart() && w[i].getEnd() > w[j].getEnd())
                std::swap(w[i], w[j]);
        }
    return this->weatherList;
}

Service::~Service() {
}