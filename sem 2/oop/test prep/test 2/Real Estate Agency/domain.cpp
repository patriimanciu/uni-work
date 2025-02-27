//
// Created by patri manciu on 22.04.2024.
//

#include "domain.h"
#include <fstream>

// Dwelling

Dwelling::Dwelling(double price, bool isProfitable) {
    this->price = price;
    this->isProfitable = isProfitable;
}

std::string Dwelling::toString() const {
    return std::to_string(this->price) + " " + std::to_string(this->isProfitable);
}

double Dwelling::getPrice() {
    return this->price;
}

bool Dwelling::getIsProfitable() {
    return this->isProfitable;
}

Dwelling::~Dwelling() = default;

// Client

double Client::totalIncome() {
    return 0;
}

Client::Client(std::string name, double income) {
    this->name = name;
    this->income = income;
}

Client::~Client() = default;

std::string Client::getName() {
    return this->name;
}

// Person

bool Person::isInterested(Dwelling d) {
    return (d.getPrice() / 1000) <= this->income;
}

Person::Person(std::string name, double income) : Client(name, income) {
}

std::string Person::toString() {
    return this->name + " " + std::to_string(this->income);
}

double Person::totalIncome() {
    return 0;
}

Person::~Person() = default;

// Company

bool Company::isInterested(Dwelling d) {
    return (d.getPrice() / 100) < (this->income + this->moneyFromInvestments);
}

std::string Company::toString() {
    return this->name + " " + std::to_string(this->income) + " " + std::to_string(this->moneyFromInvestments);
}

double Company::totalIncome() {
    return 0;
}

Company::Company(std::string name, double income1, double moneyFromInvestments)
        : Client(name, income1) {
    this->moneyFromInvestments = moneyFromInvestments;
}

Company::~Company() = default;

// RealEstateAgency

void RealEstateAgency::removeClient(std::string name) {
    for (int i = 0; i < clients.size(); i++) {
        if (clients[i]->getName() == name) {
            clients.erase(clients.begin() + i);
            break;
        }
    }
}

//std::vector<Client *> RealEstateAgency::getInterestedClient(Dwelling d) {;
//}
RealEstateAgency::RealEstateAgency() {
    auto *p1 = new Person("John", 1000);
    auto *p2 = new Company("Company A", 1000, 1000);
    auto *p3 = new Person("Jane", 5000);
    auto *p4 = new Company("Company B", 5000, 5000);
//
//    std::cout << p1->toString() << "\n";
//    std::cout << p2->toString() << "\n";
//    std::cout << p3->toString() << "\n";
//    std::cout << p4->toString() << "\n";

    this->clients.push_back(p1);
    this->clients.push_back(p2);
    this->clients.push_back(p3);
    this->clients.push_back(p4);
    this->dwellings.push_back(Dwelling(1000, true));
    this->dwellings.push_back(Dwelling(2000, false));
    this->dwellings.push_back(Dwelling(3000, true));

}

RealEstateAgency::~RealEstateAgency() {
    for (Client *c : clients) {
        delete c;
    }
}

std::vector<Client *> &RealEstateAgency::getClients() {
    return this->clients;
}

std::vector<Dwelling> RealEstateAgency::getDwellings() {
    return this->dwellings;
}


Dwelling RealEstateAgency::addDwelling(double price, bool isProfitable) {
    Dwelling d = Dwelling(price, isProfitable);
    this->dwellings.push_back(d);
    return d;
}

std::vector<Client *> RealEstateAgency::getInterestedClient(Dwelling d) {
    std::vector<Client *> client = this->clients;
    std::vector<Client *> result;
    for (Client *c : client) {
        if (c->isInterested(d)) {
            result.push_back(c);
        }
    }
    return result;
}


void RealEstateAgency::writeToFile(std::string filename) {
    std::ofstream file(filename);
    if (!file.is_open())
        throw std::invalid_argument("The file could not be opened!");
    for (Client *c : this->clients) {
        file << c->toString() << "\n";
    }
}
