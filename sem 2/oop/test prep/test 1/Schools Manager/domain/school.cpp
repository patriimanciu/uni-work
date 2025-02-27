//
// Created by patri manciu on 01.04.2024.
//

#include "school.h"

School::School(const std::string &name, float address_long, float address_lat, Date date, bool visited) {
    this->name = name;
    this->address_long = address_long;
    this->address_lat = address_lat;
    this->date = date;
    this->visited = visited;
}

School::School(const School &school) {
    this->name = school.name;
    this->address_long = school.address_long;
    this->address_lat = school.address_lat;
    this->date = school.date;
    this->visited = school.visited;
}

School &School::operator=(const School &school) {
    if (this == &school)
        return *this;

    this->name = school.name;
    this->address_long = school.address_long;
    this->address_lat = school.address_lat;
    this->date = school.date;
    this->visited = school.visited;
    return *this;
}

//bool &School::operator==(const School &school) {
//    return (this->name == school.name) && (this->address_long == school.address_long) && (this->address_lat == school.address_lat);
//}

std::string School::getName() {
    return this->name;
}

float School::getLongitude() {
    return this->address_long;
}

float School::getLatitude() {
    return this->address_lat;
}

int School::getDateDay() {
    return this->date.day;
}

int School::getDateMonth() {
    return this->date.month;
}

int School::getDateYear() {
    return this->date.year;
}

bool School::getVisited() {
    return this->visited;
}

void School::setVisited() {
    this->visited = true;
}
