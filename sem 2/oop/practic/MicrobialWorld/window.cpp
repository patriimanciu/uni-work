//
// Created by patri manciu on 26.06.2024.
//

// You may need to build the project (run Qt uic code generator) to get "ui_Window.h" resolved

#include "window.h"
#include "ui_Window.h"


Window::Window(QAbstractItemModel* model, Biologist b, QWidget *parent) :
        QWidget(parent), ui(new Ui::Window), model(model) {
    ui->setupUi(this);
    setWindowTitle(QString::fromStdString(b.getName()));
    this->ui->bacteriumTableView->setModel(model);
    this->ui->bacteriumTableView->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);
//    this->ui->comboBox->addItem(QString::fromStdString("All"));
//    for (auto& b : ) {
//        this->ui->comboBox->addItem(QString::fromStdString(b.getName()));
//    }
//    QObject::connect(this->ui->comboBox, &QComboBox::currentTextChanged, this, &Window::combo);
//    this->ui->comboBox->setCurrentText(QString::fromStdString("All"));
}

Window::~Window() {
    delete ui;
}

//void Window::combo() {
//    model->setBacteria(this->model->service.getBySpecies()getBacteriaBySpecies(species.toStdString()));
//}
