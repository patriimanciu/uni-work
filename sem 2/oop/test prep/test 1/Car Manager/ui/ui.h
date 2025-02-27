//
// Created by patri manciu on 01.04.2024.
//

#ifndef CAR_MANAGER_UI_H
#define CAR_MANAGER_UI_H
#include "../service/service.h"

class UI {
private:
    Service service = Service();
    void startUpData();

public:
    UI();
    ~UI();
    void run();
    void addCarUI();
    void getAllUI();
    void printMenu();
    void removeCarUI();
    void getVintageUI();
};

#endif //CAR_MANAGER_UI_H
