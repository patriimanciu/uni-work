//
// Created by patri manciu on 28.05.2024.
//

#ifndef WEATHER_DOMAIN_H
#define WEATHER_DOMAIN_H
#include <iostream>

class Weather {
private:
    int start, end, temperature, precipitation;
    std::string description;
public:
    Weather(int start, int end, int temperature, int precipitation, std::string description);
    int getPrecipitation();
    std::string toString();
    int getStart();
    int getEnd();
    std::string getDescription();
    ~Weather();

};


#endif //WEATHER_DOMAIN_H
