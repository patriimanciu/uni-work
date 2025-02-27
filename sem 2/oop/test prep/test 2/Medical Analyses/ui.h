//
// Created by patri manciu on 22.04.2024.
//
#include "domain.h"

class UI {
private:
    Person person{"Ana"};
public:
    UI();
    void run();
    void menu();
    void addAnalysis();
    void showAll();
    void isIll();
    void save();
    ~UI();
};