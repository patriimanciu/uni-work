//
// Created by patri manciu on 27.05.2024.
//

#include "domain.h"

Document::Document(std::string name, std::string keywords, std::string content) {
    this->name = name;
    this->keywords = keywords;
    this->content = content;
}

std::string Document::to_string() {
    return this->name + " | " + this->keywords + " | " + this->content;
}

std::string Document::getName() {
    return this->name;
}

double Document::getMatchScore(std::string input) {
    int input_length = input.length();
    int name_length = this->name.length();

    return (double) input_length / name_length;
}

Document::~Document(){
}