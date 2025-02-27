//
// Created by patri manciu on 01.04.2024.
//

#include "service.h"

int Service::addSchoolService(const School &school) {
    this->repo.addSchool(school);
    return 0;
}

int Service::removeSchoolService(std::string name) {
    int pos = this->repo.getPositionByName(name);
    this->repo.removeSchool(pos);
    return 0;
}

DynamicVector<School> Service::getAll() {
    return this->repo.getAll();
}

DynamicVector<School> Service::getToBeVisited(int day, int month, int year) {
    DynamicVector<School> array = this->repo.getAll();
    DynamicVector<School> newArray = DynamicVector<School>();
    for (int i = 0; i < array.getSizeOfDynamicVector(); i++)
        if (array[i].getDateYear() < year)
            this->repo.setVisited(i);
        else if (array[i].getDateYear() == year && array[i].getDateMonth() < month)
            this->repo.setVisited(i);
        else if (array[i].getDateYear() == year && array[i].getDateMonth() == month && array[i].getDateDay() <= day)
            this->repo.setVisited(i);
        else
            newArray.addElementInDynamicVector(array[i]);
    return newArray;
}
