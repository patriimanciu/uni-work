//
// Created by patri manciu on 22.04.2024.
//
#include <iostream>

class MedicalAnalysis {
protected:
    std::string date;
public:
    std::string getDate() const;
    virtual bool isResultOK() =0;
    virtual std::string toString() =0;
};

// -------------------------------

class BMI: public MedicalAnalysis {
private:
    double value;
public:
    BMI(std::string date, double value);
    bool isResultOK();
    std::string toString();
    ~BMI();
};

// -------------------------------

class BP: public MedicalAnalysis {
private:
    int systolicValue;
    int diastolicValue;
public:
    BP(std::string date, int systolic, int diastolic);
    bool isResultOK();
    std::string toString();
    ~BP();
};

class Person {
private:
    std::string name;
    std::vector<MedicalAnalysis *> analyses;
public:
    Person(std::string name="");
    void addAnalysis(MedicalAnalysis *a);
    std::vector<MedicalAnalysis *> getAllAnalyses();
    std::vector<MedicalAnalysis *> getAnalysesByMonth(int month);
    bool isIll(int month);
    std::vector<MedicalAnalysis *> getAnalysesBetweenDates(std::string date1, std::string date2);
    void writeToFile(std::string filename, std::string date1, std::string date2);
    ~Person();
};