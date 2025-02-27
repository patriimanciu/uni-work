//
// Created by patri manciu on 27.05.2024.
//

#include "service.h"
#include <sstream>

std::vector<std::string> split(const std::string &line, char delimiter) {
    std::vector<std::string> parts;
    std::stringstream ss(line);
    std::string part;
    while (std::getline(ss, part, delimiter)) {
        parts.push_back(part);
    }
    return parts;
}

void Service::read() {
    std::ifstream file("../input.txt");
    if (!file.is_open()) {
        throw std::runtime_error("File could not be opened");
    }
    documents.clear();

    std::string line;
    while (std::getline(file, line)) {
        std::vector<std::string> fields = split(line, '|');
        if (fields.size() == 3) {
            std::string name = fields[0];
            std::string keywords = fields[1];
            std::string content = fields[2];

            Document doc = Document(name, keywords, content);
            documents.push_back(doc);
        }
        else
            throw std::runtime_error("Incorrect format.");
    }
}

std::vector<Document> Service::getAllDoc() {
    std::vector<Document> oldDoc = this->documents;

    for (int i = 0; i < documents.size(); i++) {
        for (int j = 0; j < documents.size() - i - 1; j++)
            if (oldDoc[j].getName() > oldDoc[j + 1].getName())
                std::swap(oldDoc[j], oldDoc[j + 1]);
    }

    return oldDoc;
}
