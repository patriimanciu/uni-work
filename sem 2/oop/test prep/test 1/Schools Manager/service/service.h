//
// Created by patri manciu on 01.04.2024.
//

#ifndef SCHOOLS_MANAGER_SERVICE_H
#define SCHOOLS_MANAGER_SERVICE_H
#pragma once
#include "../repository/repo.h"

class Service{
private:
    Repository repo;
public:
    int addSchoolService(const School &school);
    int removeSchoolService(std::string name);
    DynamicVector<School> getAll();
    DynamicVector<School> getToBeVisited(int day, int month, int year);
};

#endif //SCHOOLS_MANAGER_SERVICE_H
