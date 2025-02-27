//
// Created by patri manciu on 22.04.2024.
//
#include <iostream>
class Dwelling {
private:
    double price;
    bool isProfitable;
public:
    Dwelling(double price, bool isProfitable);
    std::string toString() const;
    double getPrice();
    bool getIsProfitable();
    ~Dwelling();
};

class Client {
protected:
    std::string name;
    double income;
public:
    Client(std::string name, double income);
    virtual bool isInterested(Dwelling d) = 0;

    virtual double totalIncome() =0;

    virtual std::string toString() =0;
    std::string getName();
    virtual ~Client() =0;
};

class Person : public Client {
public:
    Person(std::string name, double income);
    bool isInterested(Dwelling d);
    std::string toString();
    double totalIncome();
    ~Person();
};

class Company : public Client {
private:
    double moneyFromInvestments;
public:
    Company(std::string name, double income, double moneyFromInvestments);
    bool isInterested(Dwelling d);
    std::string toString();
    double totalIncome();
    ~Company();
};

class RealEstateAgency {
private:
    std::vector<Dwelling> dwellings;
    std::vector<Client *> clients;
public:
    RealEstateAgency();
    Dwelling addDwelling(double price, bool isProfitable);
    void removeClient(std::string name);
    std::vector<Client *> getInterestedClient(Dwelling d);
    void writeToFile(std::string filename);
    std::vector<Client *> &getClients();
    std::vector<Dwelling> getDwellings();
    ~RealEstateAgency();
};