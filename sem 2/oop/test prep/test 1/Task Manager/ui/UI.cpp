//
// Created by patri manciu on 02.04.2024.
//

#include "UI.h"

UI::UI() {
    this->service = Service();
}

UI::~UI() {
}

void UI::run() {
    std::cout << "Welcome.\n";
    while (true) {
        this->printMenu();
        int option;
        std::cout << "> ";
        std::cin >> option;
        if (option == 1)
            this->addTaskUI();
        else if (option == 2)
            this->showAllUI();
        else if (option == 3)
            this->showPriority();
        else if (option == 0) {
            std::cout << "Bye\n";
            break;
        }
        else
            std::cout << "Invalid\n";
    }
}

void UI::printMenu() {
    std::cout << "1. Add a task.\n";
    std::cout << "2. Show all.\n";
    std::cout << "3. Show all less than a given priority.\n";
    std::cout << "0. Exit.\n";
}

void UI::addTaskUI() {
    std::string description;
    int duration;
    int priority;
    std::cout << "Please give information about the task.\n";
    std::cout << "Description: ";
    std::cin >> description;
    std::cout << "Duration: ";
    std::cin >> duration;
    std::cout << "Priority: ";
    std::cin >> priority;
    int add = this->service.addTaskService(description, duration, priority);
    if (add == 1)
        std::cout << "Task already exists.\n";
    else
        std::cout << "Task added successfully.\n";
}

void UI::showAllUI() {
    DynamicVector<Task> array = this->service.getAllService();
    for (int i = 0; i < array.getSizeOfDynamicVector(); i++)
        std::cout << array[i].getDescription() << " | " << array[i].getDuration() << " | " << array[i].getPriority() << '\n';
}

void UI::showPriority() {
    int priority;
    std::cout << "The task with a priority less than the given one will be shown.\n";
    std::cout << "Priority: ";
    std::cin >> priority;
    DynamicVector<Task> array = this->service.getPriority(priority);
    for (int i = 0; i < array.getSizeOfDynamicVector(); i++)
        std::cout << array[i].getDescription() << " | " << array[i].getDuration() << " | " << array[i].getPriority() << '\n';
}
