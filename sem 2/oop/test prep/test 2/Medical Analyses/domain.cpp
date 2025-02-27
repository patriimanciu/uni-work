//
// Created by patri manciu on 22.04.2024.
//

#include "domain.h"
#include <fstream>

std::string MedicalAnalysis::getDate() const {
    return this->date;
}

BMI::BMI(std::string date, double value) {
    this->value = value;
    this->date = date;
}

BMI::~BMI() {
}

bool BMI::isResultOK() {
    if (this->value >= 18.5 && this->value <= 25)
        return true;
    return false;
}

std::string BMI::toString() {
    return "BMI || Date: " + this->date + " | Value: " + std::to_string(value);
}

BP::BP(std::string date, int systolic, int diastolic) {
    this->date = date;
    this->diastolicValue = diastolic;
    this->systolicValue = systolic;
}

bool BP::isResultOK() {
    if (this->systolicValue >= 90 && this->systolicValue <= 119) {
        if (this->diastolicValue >= 60 && this->diastolicValue <= 79)
            return true;
        else
            return false;
    }
    else
        return false;
}

std::string BP::toString() {
    return "BP || Date: " + this->date + " | Systolic: " + std::to_string(this->systolicValue) + " Diastolic: " + std::to_string(
            this->diastolicValue);
}

BP::~BP() {
}

Person::Person(std::string name) {
    this->name = name;
}

Person::~Person() {
    delete []&this->analyses;
}

void Person::addAnalysis(MedicalAnalysis *a) {
    this->analyses.push_back(a);
}

std::vector<MedicalAnalysis *> Person::getAllAnalyses() {
    std::vector<MedicalAnalysis *> temp = this->analyses;
    return temp;
}

std::vector<MedicalAnalysis *> Person::getAnalysesByMonth(int month) {
    std::vector<MedicalAnalysis *> temp = this->analyses;
    std::vector<MedicalAnalysis *> result;
    for (int i = 0; i < temp.size(); i++) {
        if (std::stoi(temp[i]->getDate().substr(5, 2)) == month)
            result.push_back(temp[i]);
    }
    return result;
}

bool Person::isIll(int month) {
    std::vector<MedicalAnalysis *> temp = this->getAnalysesByMonth(month);
    for (int i = 0; i < temp.size(); i++) {
        if (temp[i]->isResultOK())
            return false;
    }
    return true;
}

std::vector<MedicalAnalysis *> Person::getAnalysesBetweenDates(std::string date1, std::string date2) {
    std::vector<MedicalAnalysis *> temp = this->analyses;
    std::vector<MedicalAnalysis *> result;
    for (MedicalAnalysis* elem : temp) {
        if (elem->getDate() >= date1 && elem->getDate() <= date2)
            result.push_back(elem);
    }
    return result;
}

void Person::writeToFile(std::string filename, std::string date1, std::string date2) {
//    std::ofstream file(filename);
//    if (!file.is_open())
//        throw std::invalid_argument("The file could not be opened!");
//    std::vector<MedicalAnalysis *> temp = this->analyses;
//    for (MedicalAnalysis* elem : temp) {
//        if (elem->getDate() >= date1 && elem->getDate() <= date2)
//            file << elem->toString() << "\n";
//    }
//    file.close();
    std::ofstream f(filename);
    for (MedicalAnalysis* elem : this->analyses)
        if (elem->getDate() >= date1 && elem->getDate() <= date2)
            f << elem->toString();
}
