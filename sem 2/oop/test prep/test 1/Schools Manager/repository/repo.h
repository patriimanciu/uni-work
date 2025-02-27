//
// Created by patri manciu on 01.04.2024.
//

#ifndef SCHOOLS_MANAGER_REPO_H
#define SCHOOLS_MANAGER_REPO_H
#pragma once
#include "DynamicVector.h"
#include "../domain/school.h"

class Repository{
private:
    DynamicVector<School> schools;

public:
    Repository();
    ~Repository();
    void addSchool(const School& school);
    void removeSchool(int position);
    DynamicVector<School> getAll();
    int getPositionByName(std::string name);
    void setVisited(int position);
};

#endif //SCHOOLS_MANAGER_REPO_H
