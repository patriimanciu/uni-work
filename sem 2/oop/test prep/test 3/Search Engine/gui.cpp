//
// Created by patri manciu on 27.05.2024.
//

// You may need to build the project (run Qt uic code generator) to get "ui_GUI.h" resolved

#include "gui.h"
#include "ui_GUI.h"


GUI::GUI(Service &service, QWidget *parent) :
        QWidget(parent), ui(new Ui::GUI) {
    this->service = service;
    ui->setupUi(this);
    this->service.read();
    this->populate_list();
    QObject::connect(this->ui->searchBar, &QLineEdit::textChanged, this, &GUI::search);
    QObject::connect(this->ui->bestMatchButton, &QPushButton::clicked, this, &GUI::best_matching);
}

GUI::~GUI() {
    delete ui;
}

void GUI::populate_list() {
    ui->documentList->clear();
    for (auto doc : this->service.getAllDoc()) {
        QString docString = QString::fromStdString(doc.to_string());
        ui->documentList->addItem(docString);
    }
}

void GUI::search() {
    this->ui->documentList->clear();
    std::string searchString = this->ui->searchBar->text().toStdString();
    for (auto doc : this->service.getAllDoc()) {
        if (doc.to_string().find(searchString) != std::string::npos) {
            QString docString = QString::fromStdString(doc.to_string());
            ui->documentList->addItem(docString);
        }
    }
}

void GUI::best_matching() {
    this->ui->documentList->clear();
    std::string searchString = this->ui->searchBar->text().toStdString();
    Document bestMatch = {"", "", ""};
    double score = 0.0;
    for (auto doc : this->service.getAllDoc()) {
        if (doc.to_string().find(searchString) != std::string::npos) {
            double s = doc.getMatchScore(searchString);
//            std::cout << s << '\n';
            if (s >= score) {
                score = s;
                bestMatch = doc;
            }
        }

    }
    QString best = QString::fromStdString(bestMatch.to_string());
    ui->documentList->addItem(best);
}

