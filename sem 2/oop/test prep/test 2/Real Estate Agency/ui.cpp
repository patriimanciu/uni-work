//
// Created by patri manciu on 22.04.2024.
//

#include "ui.h"

UI::UI() {
}

void UI::run() {

    while (true) {
        printMenu();
        int command;
        std::cout << " > ";
        std::cin >> command;
        if (command == 0) {
            break;
        }
        else if (command == 1) {
            std::cout << "Name: ";
            std::string name;
            std::cin >> name;
            agency.removeClient(name);
        }
        else if (command == 2) {
            this->showAll();
        }
        else if (command == 3)
            this->addDwelling();
        else if (command == 4) {
            this->saveToFile();
        }
        else if (command == 0)
            break;
        else {
            std::cout << "Invalid input.\n";
        }
    }
}

void UI::printMenu() {
    std::cout << "1. Remove client\n";
    std::cout << "2. Show all clients and dwellings\n";
    std::cout << "3. Add dwelling\n";
    std::cout << "4. Save to file\n";
    std::cout << "0. Exit\n";
}

void UI::showAll() {
    for (Client *c : agency.getClients()) {
        if (c != nullptr) {
            std::cout << c->toString() << "\n";
        } else {
            std::cout << "Null pointer encountered.\n";
        }
    }
    for (const Dwelling& d : agency.getDwellings()) {
        std::cout << d.toString() << "\n";
    }
}

void UI::addDwelling() {
    double price;
    bool isProfitable;
    std::cout << "Price: ";
    std::cin >> price;
    std::cout << "Is profitable? (1/0): ";
    std::cin >> isProfitable;
    Dwelling d = Dwelling(price, isProfitable);
    agency.addDwelling(price, isProfitable);
    this->showInterested(this->agency.getInterestedClient(d));
}

void UI::showInterested(std::vector<Client *> vector1) {
    for (Client *c : vector1) {
        std::cout << c->toString() << "\n";
    }

}

void UI::saveToFile() {
    std::string filename;
    std::cout << "Filename: ";
    std::cin >> filename;
    this->agency.writeToFile(filename);
}

UI::~UI() = default;