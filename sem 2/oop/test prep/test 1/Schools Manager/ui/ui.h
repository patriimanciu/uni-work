//
// Created by patri manciu on 01.04.2024.
//

#ifndef SCHOOLS_MANAGER_UI_H
#define SCHOOLS_MANAGER_UI_H
#include <iostream>
#pragma once
#include "../service/service.h"

class UI {
private:
    Service service;
    void startUpData();
public:
    UI();
    ~UI();
    void run();
    void removeSchoolUI();
    void showAllUI();
    void showSchoolsToBeVisited();
    static void printMenu();
};

#endif //SCHOOLS_MANAGER_UI_H
