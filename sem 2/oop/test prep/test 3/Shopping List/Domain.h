//
// Created by patri manciu on 28.05.2024.
//

#ifndef SHOPPING_LIST_DOMAIN_H
#define SHOPPING_LIST_DOMAIN_H
#include <iostream>

class Item {
private:
    std::string category, name;
    int quantity;
public:
    Item(std::string category, std::string name, int quantity);
    std::string getCategory();
    std::string getName();
    int getQuantity();
    std::string toString();
    ~Item();
};


#endif //SHOPPING_LIST_DOMAIN_H
