//
// Created by patri manciu on 26.06.2024.
//

#ifndef ARTAUCTION_SESSION_H
#define ARTAUCTION_SESSION_H
#include <iostream>
#include <vector>
#include "Item.h"
#include "User.h"
#include "Subject.h"

class Session : public Subject {
private:
    std::vector<User> users;
    std::vector<Item> items;
    std::vector<std::string> categories;

    void readData() {
        readUsers();
        readItems();
    }

    void readUsers();

    void readItems();

public:
    Session() { readData(); };

    ~Session() {};

    std::vector<User> getUsers() { return this->users; }

    std::vector<Item> getItems() { return this->items; }

    std::vector<std::string> getCategories();

    void addItem(Item i) {
        this->items.push_back(i);
        this->notify();
    };

    void updateItem(Item i);
    void save();
};

#endif //ARTAUCTION_SESSION_H
