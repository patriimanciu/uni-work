//
// Created by patri manciu on 27.05.2024.
//

#ifndef SEARCH_ENGINE_SERVICE_H
#define SEARCH_ENGINE_SERVICE_H

#include <fstream>
#include <vector>
#include <iostream>
#include "domain.h"

class Service {
private:
    std::vector<Document> documents;
public:
    void read();
    std::vector<Document> getAllDoc();
};


#endif //SEARCH_ENGINE_SERVICE_H
