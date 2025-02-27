//
// Created by patri manciu on 28.05.2024.
//

// You may need to build the project (run Qt uic code generator) to get "ui_GUI.h" resolved

#include "gui.h"
#include "ui_GUI.h"
#include <QErrorMessage>


GUI::GUI(Service &serv, QWidget *parent) :
        QWidget(parent), ui(new Ui::GUI) {
    this->service = serv;
    ui->setupUi(this);
    this->service.read();
    this->populate_list();
    QObject::connect(ui->precipitationLineEdit, &QLineEdit::textChanged, this, &GUI::filter);
    QObject::connect(this->ui->pushButton, &QPushButton::clicked, this, &GUI::filterDescription);
}

GUI::~GUI() {
    delete ui;
}

void GUI::populate_list() {
    this->ui->weatherListWidget->clear();
    for (auto w : this->service.getAll()) {
        QString wString = QString::fromStdString(w.toString());
        this->ui->weatherListWidget->addItem(wString);
    }
}

void GUI::filter() {
    this->ui->weatherListWidget->clear();
    for (auto w: this->service.getAll()) {
        if (w.getPrecipitation() < this->ui->precipitationLineEdit->text().toInt())
            this->ui->weatherListWidget->addItem(QString::fromStdString(w.toString()));
    }
}

void GUI::filterDescription() {
    int total = 0;
    this->ui->filteredListWidget->clear();
    for (auto w: this->service.getAll()) {
        if (w.getDescription().find(this->ui->descriptionLineEdit->text().toStdString()) != std::string::npos
        && w.getStart() >= this->ui->timeLineEdit->text().toInt()) {
            this->ui->filteredListWidget->addItem(QString::fromStdString(w.toString()));
            total += w.getEnd() - w.getStart();
        }
    }
    this->ui->totalLineEdit->setText(QString::fromStdString(std::to_string(total)));
    if (total == 0) {
        QErrorMessage* error = new QErrorMessage();
        error->showMessage("No items found");
    }
}