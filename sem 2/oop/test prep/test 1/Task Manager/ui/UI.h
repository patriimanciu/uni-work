//
// Created by patri manciu on 02.04.2024.
//

#ifndef TASK_MANAGER_UI_H
#define TASK_MANAGER_UI_H
#include "../service/Service.h"

class UI {
private:
    Service service;
public:
    UI();
    ~UI();
    void run();
    void printMenu();
    void addTaskUI();
    void showAllUI();
    void showPriority();

};

#endif //TASK_MANAGER_UI_H
