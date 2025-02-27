//
// Created by patri manciu on 28.05.2024.
//

#ifndef WEATHER_SERVICE_H
#define WEATHER_SERVICE_H
#include "Domain.h"
#include <vector>
#include <iostream>


class Service {
private:
    std::vector<Weather> weatherList;
public:
    Service();
    void read();
    std::vector<Weather> getAll();
    ~Service();

};


#endif //WEATHER_SERVICE_H
