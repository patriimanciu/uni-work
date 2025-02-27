//
// Created by patri manciu on 26.06.2024.
//

#include "Session.h"
#include <fstream>
#include <sstream>

void Session::readUsers() {
    std::ifstream file("../users.txt");
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file");
    }
    this->users.clear();
    std::string name;
    int id;
    std::string type;
    while (file >> name >> id >> type) {
        User u(name, id, type);
        this->users.push_back(u);
    }
    file.close();
}

void Session::readItems() {
    std::ifstream file("../items.txt");
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file");
    }
    this->items.clear();
    std::string name;
    std::string category;
    int currentPrice;
    std::vector<Offer> offersList;
    std::string line;
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        iss >> name >> category >> currentPrice;
        int id;
        int day;
        int month;
        int year;
        int sum;
        while (iss >> id >> day >> month >> year >> sum) {
            Offer o = {id, day, month, year, sum};
            offersList.push_back(o);
        }
        Item i(name, category, currentPrice, offersList);
        this->items.push_back(i);
    }
    file.close();
}

std::vector<std::string> Session::getCategories() {
    for (auto &item : this->items) {
        if (std::find(this->categories.begin(), this->categories.end(), item.getCategory()) == this->categories.end())
            this->categories.push_back(item.getCategory());
    }
    return this->categories;
}

void Session::updateItem(Item i) {
    for (int j = 0; j < this->items.size(); j++) {
        if (this->items[j].getName() == i.getName()) {
            this->items[j] = i;
            this->notify();
            return;
        }
    }
    throw std::runtime_error("Item not found");
}

void Session::save() {
    std::ofstream file("../items.txt");
    for (auto &item : this->getItems()) {
        file << item.itemToString() << "\n";
        for (auto offer : item.getOffersList()) {
            file << std::to_string(offer.userId) << " " << std::to_string(offer.date.day) << " " << std::to_string(offer.date.month) <<
            " " << std::to_string(offer.date.year) << std::to_string(offer.offeredSum) << "\n";
        }
    }
    file.close();

}