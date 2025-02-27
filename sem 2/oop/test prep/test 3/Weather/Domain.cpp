//
// Created by patri manciu on 28.05.2024.
//

#include "Domain.h"

Weather::Weather(int start, int end, int temperature, int precipitation, std::string description) {
    this->start = start;
    this->end = end;
    this->temperature = temperature;
    this->precipitation = precipitation;
    this->description = description;
}

int Weather::getPrecipitation() {
    return this->precipitation;
}

std::string Weather::toString() {
    return std::to_string(this->start) + " - " + std::to_string(this->end) + " | " + std::to_string(this->temperature) + " | " + std::to_string(this->precipitation) + " | " + this->description;
}


int Weather::getStart() {
    return this->start;
}

int Weather::getEnd() {
    return this->end;
}

Weather::~Weather() {
}

std::string Weather::getDescription() {
    return this->description;
}