//
// Created by patri manciu on 26.06.2024.
//

#ifndef ARTAUCTION_ITEM_H
#define ARTAUCTION_ITEM_H
#include <iostream>
#include <vector>
#include "User.h"

class Item {
private:
    std::string name;
    std::string category;
    int currentPrice;
    std::vector<Offer> offersList;
public:
    Item(std::string name = "", std::string category = "", int currentPrice = 0, std::vector<Offer> offersList = {}) {
        this->name = name;
        this->category = category;
        this->currentPrice = currentPrice;
        this->offersList = offersList;
    }

    ~Item() {}

    std::string getName() {
        return this->name;
    }

    std::string getCategory() {
        return this->category;
    }

    int getCurrentPrice() {
        return this->currentPrice;
    }

    std::vector<Offer> getOffersList() {
        return this->offersList;
    }

    std::vector<std::string> getOffersListString() {
        std::vector<std::string> offersListString = {};
        for(auto offer: this->offersList) {
            offersListString.push_back(toString(offer));
        }
        for (int i = 0; i < offersListString.size(); i++) {
            for (int j = i + 1; j < offersListString.size(); j++) {
                if (offersListString[i] < offersListString[j]) {
                    std::string aux = offersListString[i];
                    offersListString[i] = offersListString[j];
                    offersListString[j] = aux;
                }
            }
        }
        return offersListString;
    }

    std::string toString(Offer offer) {
        return std::to_string(offer.date.day) + "." + std::to_string(offer.date.month) + "." + std::to_string(offer.date.year) + " - " + std::to_string(offer.offeredSum) + " : " + std::to_string(offer.userId);
    }

    std::string itemToString() {
        return this->name + " " + this->category + " " + std::to_string(this->currentPrice);
    }

    void addOffer(Offer o) {
        this->offersList.push_back(o);
        this->currentPrice = o.offeredSum;
    }
};


#endif //ARTAUCTION_ITEM_H
