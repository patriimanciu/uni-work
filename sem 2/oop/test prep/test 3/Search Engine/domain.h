//
// Created by patri manciu on 27.05.2024.
//

#ifndef SEARCH_ENGINE_DOMAIN_H
#define SEARCH_ENGINE_DOMAIN_H
#include <iostream>

class Document {
private:
    std::string name;
    std::string keywords;
    std::string content;
public:
    Document(std::string name, std::string keywords, std::string content);
    std::string to_string();
    std::string getName();
    double getMatchScore(std::string input);
    ~Document();
};


#endif //SEARCH_ENGINE_DOMAIN_H
