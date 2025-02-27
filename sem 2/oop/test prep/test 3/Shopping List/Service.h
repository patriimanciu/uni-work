//
// Created by patri manciu on 28.05.2024.
//

#ifndef SHOPPING_LIST_SERVICE_H
#define SHOPPING_LIST_SERVICE_H
#include <iostream>
#include <vector>
#include "Domain.h"

class Service {
private:
    std::vector<Item> shoopingList;
public:
    void read();
    std::vector<Item> getAll();
};


#endif //SHOPPING_LIST_SERVICE_H
