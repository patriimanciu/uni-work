//
// Created by patri manciu on 22.04.2024.
//

#include "ui.h"

UI::UI() {
}

void UI::run() {
    BMI* a1 = new BMI{"2023.11.13", 78.2};
    BP* a2 = new BP{"2024.02.12", 65, 89};

    this->person.addAnalysis(a1);
    this->person.addAnalysis(a2);
    while (true) {
        menu();
        int option;
        std::cout << "> ";
        std::cin >> option;
        if (option == 1)
            this->addAnalysis();
        else if (option == 2)
            this->showAll();
        else if (option == 3)
            this->isIll();
        else if (option == 4)
            this->save();
        else if (option == 0){
            std::cout << "Bye\n";
            break;
        }
        else
            std::cout << "Invalid option.\n";
    }
}

UI::~UI() {

}

void UI::menu() {
    std::cout << "1. Add analysis.\n";
    std::cout << "2. Show all analyses.\n";
    std::cout << "3. Is ill? \n";
    std::cout << "4. Save to file.\n";
    std::cout << "0. Exit.\n";
}

void UI::addAnalysis() {
    std::string type, date;
    std::cout << "Analysis type (BMI/BP) > ";
    std::cin >> type;
    std::cout << "Date > ";
    std::cin >> date;
    if (type == "BMI") {
        double value;
        std::cout << "Value > ";
        std::cin >> value;
        BMI* a = new BMI(date, value);
        this->person.addAnalysis(a);
    }
    else if (type == "BP") {
        int systolic, diastolic;
        std::cout << "Systolic > ";
        std::cin >> systolic;
        std::cout << "Diastolic > ";
        std::cin >> diastolic;
        BP* a = new BP(date, systolic, diastolic);
        this->person.addAnalysis(a);
    }
    else
        std::cout << "Invalid type.\n";
}

void UI::showAll() {
    std::vector<MedicalAnalysis *> analysis = this->person.getAllAnalyses();
    for (int i = 0; i < analysis.size(); i++)
        std::cout << analysis[i]->toString() << "\n";
}

void UI::isIll() {
    std::cout << "What month should i look at? >";
    int month;
    std::cin >> month;
    if (this->person.isIll(month))
        std::cout << "The person is ill.\n";
    else
        std::cout << "The person is not ill.\n";

}

void UI::save() {
    std::string date1, date2;
    std::cout << "Date1 > ";
    std::cin >> date1;
    std::cout << "Date2 > ";
    std::cin >> date2;
//    std::vector<MedicalAnalysis *> analysis = this->person.getAnalysesBetweenDates(date1, date2);
    this->person.writeToFile("output.txt", date1, date2);
}