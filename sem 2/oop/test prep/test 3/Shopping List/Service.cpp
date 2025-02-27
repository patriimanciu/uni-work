//
// Created by patri manciu on 28.05.2024.
//

#include "Service.h"
#include <fstream>
#include <sstream>

std::vector<std::string> split(const std::string &line, char del) {
    std::vector<std::string> parts;
    std::stringstream ss(line);
    std::string part;
    while (std::getline(ss, part, del)) {
        parts.push_back(part);
    }
    return parts;
}

void Service::read() {
    std::ifstream file("../input.txt");
    shoopingList.clear();
    std::string line;
    while (std::getline(file, line)) {
        std::vector<std::string> fields = split(line, '|');
        if (fields.size() == 3) {
            std::string category = fields[0], name = fields[1];
            int quantity = std::stoi(fields[2]);
            Item i = Item(category, name, quantity);
            shoopingList.push_back(i);
        }
        else
            throw std::runtime_error("Incorrect format.");
    }
}

std::vector<Item> Service::getAll() {
    std::vector<Item> list = this->shoopingList;
    for (int i = 0 ; i < list.size(); i++)
        for (int j = 0; j < list.size() - i - 1; j++) {
            if (list[i].getCategory() < list[j].getCategory())
                std::swap(list[i], list[j]);
            else if (list[i].getCategory() == list[j].getCategory() && list[i].getName() < list[j].getName())
                std::swap(list[i], list[j]);
        }
    return list;
}