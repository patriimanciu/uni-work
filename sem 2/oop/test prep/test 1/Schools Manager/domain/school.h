//
// Created by patri manciu on 01.04.2024.
//

#ifndef SCHOOLS_MANAGER_SCHOOL_H
#define SCHOOLS_MANAGER_SCHOOL_H

#pragma once
#include <iostream>

struct Date {
    int day = 1;
    int month = 1;
    int year = 2024;
};

class School {
    private:
        std::string name;
        float address_long, address_lat;
        Date date;
        bool visited;

    public:
        School(const std::string &name="", float address_long=0, float address_lat=0, Date date = {1, 1, 2024}, bool visited=false);
        ~School() = default;
        School(const School &school);
        School &operator=(const School &school);
        // bool &operator==(const School &school);
        std::string getName();
        float getLongitude();
        float getLatitude();
        int getDateDay();
        int getDateMonth();
        int getDateYear();
        bool getVisited();
        void setVisited();
};

#endif //SCHOOLS_MANAGER_SCHOOL_H
