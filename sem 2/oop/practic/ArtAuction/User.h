//
// Created by patri manciu on 26.06.2024.
//

#ifndef ARTAUCTION_USER_H
#define ARTAUCTION_USER_H
#include <iostream>

typedef struct {
    int day, month, year;
} Date;
typedef struct {
    int userId;
    Date date;
    int offeredSum;
} Offer;

class User {
private:
    std::string name;
    int id;
    std::string type;
public:
    User(std::string name = "", int id = 0, std::string type ="") {
        this->name = name;
        this->id = id;
        this->type = type;
    }
    ~User() {}

    std::string getName() {
        return this->name;
    }

    int getId() {
        return this->id;
    }

    std::string getType() {
        return this->type;
    }


};


#endif //ARTAUCTION_USER_H
