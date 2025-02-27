//
// Created by patri manciu on 26.06.2024.
//

// You may need to build the project (run Qt uic code generator) to get "ui_SeniorWindow.h" resolved

#include "seniorwindow.h"
#include "ui_SeniorWindow.h"


SeniorWindow::SeniorWindow(Data *data, Researcher *researcher, QWidget *parent) :
        QWidget(parent), ui(new Ui::SeniorWindow), data(data), researcher(researcher) {
    ui->setupUi(this);
    this->setWindowTitle(QString::fromStdString(researcher->getName()));
    this->ui->position->setText(QString::fromStdString(researcher->getPosition()));
    this->model = new ResearcherModel(data, researcher);
    ui->tableView->setModel(model);
    ui->tableView->setSelectionBehavior(QAbstractItemView::SelectRows);
    QHeaderView *header = ui->tableView->horizontalHeader();
    header->setSectionResizeMode(QHeaderView::Stretch);
    QObject::connect(ui->addButton, &QPushButton::clicked, this, &SeniorWindow::addIdea);
    QObject::connect(ui->approveButton, &QPushButton::clicked, this, &SeniorWindow::acceptIdea);
}

void SeniorWindow::addIdea() {
    QString name = ui->nameLine->text();
    QString description = ui->descLine->text();
    QString res = QString::fromStdString(this->researcher->getName());
    int duration = ui->durationLine->text().toInt();
    this->model->addIdea(new Idea(name.toStdString(), description.toStdString(),  "proposed", res.toStdString(), duration));
}

SeniorWindow::~SeniorWindow() {
    delete ui;
}

void SeniorWindow::acceptIdea() {
    if (ui->tableView->selectionModel()->selectedRows().size() == 0) {
        return;
    }
    QModelIndex index = ui->tableView->selectionModel()->currentIndex();
    int row = index.row();
    if (this->data->getIdeas()[row]->getStatus() == "proposed")
        this->data->getIdeas()[row]->setStatus("accepted");
    this->model->update();
}

ResearcherModel::ResearcherModel(Data *data, Researcher *researcher, QObject *parent) {
    this->dataList = data;
    this->researcher = researcher;
}

int ResearcherModel::rowCount(const QModelIndex &parent) const {
    return dataList->getIdeas().size();
}

QVariant ResearcherModel::data(const QModelIndex &index, int role) const {
    if (role == Qt::DisplayRole) {
        if (index.column() == 0) {
            return QString::fromStdString(dataList->getIdeas()[index.row()]->getName());
        }
        if (index.column() == 1) {
            return QString::fromStdString(dataList->getIdeas()[index.row()]->getDescription());
        }
        if (index.column() == 3) {
            return QString::fromStdString(dataList->getIdeas()[index.row()]->getResearcher());
        }
        if (index.column() == 4) {
            return QString::number(dataList->getIdeas()[index.row()]->getDuration());
        }
        if (index.column() == 2) {
            return QString::fromStdString(dataList->getIdeas()[index.row()]->getStatus());
        }
    }
    return QVariant();
}

QVariant ResearcherModel::headerData(int section, Qt::Orientation orientation, int role) const {
    if (role == Qt::DisplayRole && orientation == Qt::Horizontal) {
        switch (section) {
            case 0: return "Title";
            case 1: return "Description";
            case 2: return "Status";
            case 3: return "Researcher";
            case 4: return "Duration";
        }
    }
    return QVariant();
}

void ResearcherModel::addIdea(Idea *idea) {
    this->beginInsertRows(QModelIndex(), this->rowCount(), this->rowCount());
    this->dataList->addIdea(idea);
    this->endInsertRows();
}

void ResearcherModel::update() {
    this->beginResetModel();
    this->endResetModel();
}