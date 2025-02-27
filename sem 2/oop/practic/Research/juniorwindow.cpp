//
// Created by patri manciu on 26.06.2024.
//

// You may need to build the project (run Qt uic code generator) to get "ui_JuniorWindow.h" resolved

#include "juniorwindow.h"
#include "ui_JuniorWindow.h"


JuniorWindow::JuniorWindow(Data *data, Researcher *researcher, QWidget *parent) :
        QWidget(parent), ui(new Ui::JuniorWindow), data(data), researcher(researcher) {
    ui->setupUi(this);
    this->setWindowTitle(QString::fromStdString(researcher->getName()));
    this->ui->position->setText(QString::fromStdString(researcher->getPosition()));
    this->model = new ResearcherModel(data, researcher);
    ui->tableView->setModel(model);
    ui->tableView->setSelectionBehavior(QAbstractItemView::SelectRows);
    ui->tableView->resizeColumnsToContents();
    QHeaderView *header = ui->tableView->horizontalHeader();
    header->setSectionResizeMode(QHeaderView::Stretch);
    QObject::connect(ui->addButton, &QPushButton::clicked, this, &JuniorWindow::addIdea);
}

JuniorWindow::~JuniorWindow() {
    delete ui;
}

void JuniorWindow::addIdea() {
    QString name = ui->nameLine->text();
    QString description = ui->descLine->text();
    QString res = QString::fromStdString(this->researcher->getName());
    int duration = ui->durationLine->text().toInt();
    this->model->addIdea(new Idea(name.toStdString(), description.toStdString(),  "proposed", res.toStdString(), duration));
}
