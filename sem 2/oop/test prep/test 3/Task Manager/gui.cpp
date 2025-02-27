//
// Created by patri manciu on 28.05.2024.
//

// You may need to build the project (run Qt uic code generator) to get "ui_GUI.h" resolved

#include "gui.h"
#include "ui_GUI.h"
#include <QFont>
#include <QErrorMessage>

GUI::GUI(Service &service, QWidget *parent) :
        QWidget(parent), ui(new Ui::GUI) {
    ui->setupUi(this);
    this->service = service;
    this->service.read();
    this->populate_list();
    QObject::connect(ui->pushButton, &QPushButton::clicked, this, &GUI::populate_by_priority);
}

GUI::~GUI() {
    delete ui;
}


void GUI::populate_list() {
    ui->taskListWidget->clear();
    for (auto it : this->service.getAll()) {
        QString itemStr = QString::fromStdString(it.toString());
        QListWidgetItem* item = new QListWidgetItem(itemStr);
        if (it.getPriority() == 1) {
            QFont font = item->font();
            font.setBold(true);
            item->setFont(font);
        }

        ui->taskListWidget->addItem(item);
    }
}

void GUI::populate_by_priority() {
    ui->priorityListWidget->clear();
    int priority = std::stoi(ui->priorityLineEdit->text().toStdString());
    int total = 0;
    for (auto it : this->service.getAll()) {
        if (it.getPriority() == priority) {
            QString itemStr = QString::fromStdString(it.toString());
            ui->priorityListWidget->addItem(itemStr);
            total += it.getDuration();
        }
    }

    ui->taskListWidget->clear();
    for (auto it : this->service.getAll()) {
        QString itemStr = QString::fromStdString(it.toString());
        QListWidgetItem* item = new QListWidgetItem(itemStr);
        if (it.getPriority() == priority) {
            item->setBackground(Qt::blue);
        }
        ui->taskListWidget->addItem(item);
    }
    if (total == 0) {
        QErrorMessage *err = new QErrorMessage();
        err->showMessage("No tasks with this priority");
    }
    ui->totalLineEdit->setText(QString::fromStdString(std::to_string(total)));
}
