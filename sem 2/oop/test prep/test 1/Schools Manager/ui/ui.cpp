//
// Created by patri manciu on 01.04.2024.
//

#include "ui.h"

UI::UI() {
    this->service = Service();
    this->startUpData();
}

UI::~UI() {
}

void UI::run() {
    std::cout << "Application start.\n";
    while (true) {
        this->printMenu();
        int option;
        std::cout << "> ";
        std::cin >> option;
        if (option == 1)
            this->removeSchoolUI();
        else if (option == 2)
            this->showAllUI();
        else if (option == 3)
            this->showSchoolsToBeVisited();
        else if (option == 0) {
            std::cout << "Bye\n";
            break;
        }
        else
            std::cout << "Invalid.\n";

    }

}

void UI::printMenu() {
    std::cout << "1. Remove school. \n";
    std::cout << "2. Show all schools, sorted by name. \n";
    std::cout << "3. Show schools that must be visited after the date.\n";
    std::cout << "0. Exit.\n";
}

void UI::removeSchoolUI() {
    std::string name;
    std::cout << "Please give the name and address of the school you want to remove. \n";
    std::cout << "Name: ";
    std::cin >> name;
    try {
        this->service.removeSchoolService(name);
        std::cout << "School removed successfully.\n";
    }
    catch (const std::exception &Exception) {
        std::cerr << "Error: " << Exception.what() << "\n";
        return;
    }

}

void UI::showAllUI() {
    DynamicVector<School> array = this->service.getAll();
    for (int i = 0; i < array.getSizeOfDynamicVector(); i++)
        std::cout << array[i].getName() << " | " << array[i].getLongitude() << ", " << array[i].getLatitude()  <<  " | "  << array[i].getDateDay() << "."<<  array[i].getDateMonth() << "."  << array[i].getDateYear() << " | "<< array[i].getVisited() <<'\n';
}

void UI::showSchoolsToBeVisited() {
    int day, month, year;
    std::cout << "Please enter data: \n";
    std::cout << "day: ";
    std::cin >> day;
    std::cout << "month: ";
    std::cin >> month;
    std::cout << "year: ";
    std::cin >> year;
    DynamicVector<School> array = this->service.getToBeVisited(day, month, year);
    for (int i = 0; i < array.getSizeOfDynamicVector(); i++)
        std::cout << array[i].getName() << " | " << array[i].getLongitude() << ", " << array[i].getLatitude()  <<  " | "  << array[i].getDateDay() << "."<<  array[i].getDateMonth() << "."  << array[i].getDateYear() <<'\n';
}

void UI::startUpData(){
    this->service.addSchoolService(School("Avram_Iancu", 46.77, 23.60, {15, 04, 2022}, true));
    this->service.addSchoolService(School("George_Cosbuc", 46.77, 23.58, {18, 04, 2022}, false));
    this->service.addSchoolService(School("Alexandru_Vaida_Voievod", 46.77, 23.63, {23, 04, 2022}, false));
    this->service.addSchoolService(School("Romulus_Guga", 46.53, 24.57, {04, 04, 2022}, false));
    this->service.addSchoolService(School("Colegiul_Transilvania", 46.54, 24.57, {03, 05, 2022}, false));
}

