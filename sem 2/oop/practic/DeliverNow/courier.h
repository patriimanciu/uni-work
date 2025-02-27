//
// Created by patri manciu on 25.06.2024.
//

#ifndef DELIVERNOW_COURIER_H
#define DELIVERNOW_COURIER_H
#pragma once
#include <iostream>
#include <string>
#include <vector>


class Courier {
private:
    std::string name;
    typedef struct {
        int x, y, r;
    } Zone;
    Zone zone;
    std::vector<std::string> streets;
public:
    Courier(std::string name = "", int x = 0, int y = 0, int r = 0, std::vector<std::string> streets = {}) {
        this->name = name;
        this->zone.x = x;
        this->zone.y = y;
        this->zone.r = r;
        this->streets = streets;
    };

    std::string getName() {
        return this->name;
    };

    int getX() {
        return this->zone.x;
    };

    int getY() {
        return this->zone.y;
    };

    int getR() {
        return this->zone.r;
    };

    std::vector<std::string> getStreets() {
        return this->streets;
    };

    std::string toString() {
        return this->name + " (" + std::to_string(this->zone.x) + ", " + std::to_string(this->zone.y) + ") - " + std::to_string(this->zone.r);
    };

    std::string getZone() {
        return "(" + std::to_string(this->zone.x) + ", " + std::to_string(this->zone.y) + ") - " + std::to_string(this->zone.r);
    };

};


#endif //DELIVERNOW_COURIER_H
