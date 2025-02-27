//
// Created by patri manciu on 22.04.2024.
//
#include "domain.h"
class UI {
private:
    RealEstateAgency agency = RealEstateAgency();
public:
    UI();
    void run();
    void printMenu();
    void showAll();
    void addDwelling();
    ~UI();

    void showInterested(std::vector<Client *> vector1);

    void saveToFile();
};