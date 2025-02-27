//
// Created by patri manciu on 25.06.2024.
//

#ifndef DELIVERNOW_PACKAGE_H
#define DELIVERNOW_PACKAGE_H
#pragma once
#include <iostream>

class Package {
private:
    std::string recipient;
    typedef struct {
        std::string street;
        int number;
    } Address;
    Address address;
    typedef struct {
        int x, y;
    } Location;
    Location location;
    bool status;

public:
    Package(std::string recipient = "", std::string street = "", int number = 0, int x = 0, int y = 0, bool status = false) {
        this->recipient = recipient;
        this->address.street = street;
        this->address.number = number;
        this->location.x = x;
        this->location.y = y;
        this->status = status;
    };

    void setStatus(bool status) {
        this->status = status;
    };

    bool getStatus() {
        return this->status;
    };

    std::string getRecipient() {
        return this->recipient;
    };

    std::string getAddress() {
        return this->address.street + " " + std::to_string(this->address.number);
    };

    std::string getStreet() {
        return this->address.street;
    }

    int getX() {
        return this->location.x;
    };

    int getY() {
        return this->location.y;
    };

    std::string toString() {
        return this->recipient + " " + this->address.street + " " + std::to_string(this->address.number) + " (" + std::to_string(this->location.x) + ", " + std::to_string(this->location.y) + ")" + " " + std::to_string(this->status);
    };
};

#endif //DELIVERNOW_PACKAGE_H
