//
// Created by patri manciu on 01.04.2024.
//

#include "ui.h"

void UI::addCarUI() {
    std::cout << "Please provide the information for the car you want to add.\n";
    std::string man, model, colour;
    int year;
    std::cout << "Manufacturer: ";
    std::cin >> man;
    std::cout << "Model: ";
    std::cin >> model;
    std::cout << "Year: ";
    std::cin >> year;
    std::cout << "Colour: ";
    std::cin >> colour;
    try {
        this->service.addCar(man, model, year, colour);
        std::cout << "Car added successfully. \n";
    }
    catch (const std::exception &Exception) {
        std::cerr << "Error: " << Exception.what() << "\n";
        return;
    }

}

void UI::getAllUI() {
    DynamicVector<Car> array = this->service.getAll();
    for (int i = 0; i < array.getSizeOfDynamicVector(); i++)
        std::cout << array[i].getManufacturer() << " | " << array[i].getModel() << " | " << array[i].getYear() << " | " << array[i].getColour() << '\n';
}

void UI::run() {
    std::cout << "Welcome\n";
    while (true) {
        this->printMenu();
        int option;
        std::cout << "> ";
        std::cin >> option;
        if (option == 1)
            this->addCarUI();
        else if (option == 2)
            this->removeCarUI();
        else if (option == 3)
            this->getAllUI();
        else if (option == 4)
            this->getVintageUI();
        else if (option == 0)
            break;
        else
            std::cout << "Invalid.\n";
    }
}

void UI::printMenu() {
    std::cout << "1. Add a car.\n";
    std::cout << "2. Remove a car. \n";
    std::cout << "3. Show all cars. \n";
    std::cout << "4. Show vintage cars. \n";
    std::cout << "0. Exit.\n";
}

void UI::removeCarUI() {
    std::cout << "Please provide the car you want to remove.\n";
    std::string model;
    int year;
    std::cout << "Model: ";
    std::cin >> model;
    std::cout << "Year: ";
    std::cin >> year;
    try {
        this->service.removeCar(model, year);
        std::cout << "Car removed successfully.\n";
    }
    catch (const std::exception &Exception) {
        std::cerr << "Error: " << Exception.what() << "\n";
        return;
    }
}

void UI::getVintageUI() {
    DynamicVector<Car> array = this->service.getVintage();
    for (int i = 0; i < array.getSizeOfDynamicVector(); i++)
        std::cout << array[i].getManufacturer() << " | " << array[i].getModel() << " | " << array[i].getYear() << " | " << array[i].getColour() << '\n';
}

void UI::startUpData() {
    this->service.addCar("Fiat", "Bravo", 2007, "red");
    this->service.addCar("Fiat", "Idea", 2003, "black");
    this->service.addCar("Audi", "A5", 2007, "blue");
    this->service.addCar("BMW", "Coupe", 2013, "pink");
    this->service.addCar("Ford", "Fiesta", 1976, "yellow");
}

UI::UI() {
    this->service = Service();
    this->startUpData();
}

UI::~UI() {
}
