//
// Created by patri manciu on 25.06.2024.
//

// You may need to build the project (run Qt uic code generator) to get "ui_MainWindow.h" resolved

#include "mainwindow.h"
#include "ui_MainWindow.h"
#include "map.h"


MainWindow::MainWindow(DataManager& dataManager, QWidget *parent) :
        QWidget(parent), ui(new Ui::MainWindow), dataManager(dataManager) {
    ui->setupUi(this);
    setWindowTitle("DeliverNow");
    this->dataManager.readData();
    this->populateCouriers();
    this->populatePackages();
    QObject::connect(ui->addDeliveryButton, &QPushButton::clicked, this, &MainWindow::addNewPackage);
    this->showMap();
}

void MainWindow::populateCouriers() {
    ui->couriersListWidget->clear();
    for (auto& courier : this->dataManager.getCouriers()) {
        ui->couriersListWidget->addItem(QString::fromStdString(courier.toString()));
    }
}

void MainWindow::populatePackages() {
    ui->packagesListWidget->clear();
    for (auto& package : this->dataManager.getPackages()) {
        if (package.getStatus()) {
            QListWidgetItem *item = new QListWidgetItem(QString::fromStdString(package.toString()));
            item->setBackground(Qt::green);
            ui->packagesListWidget->addItem(item);
        }
        else
            ui->packagesListWidget->addItem(QString::fromStdString(package.toString()));
    }
    this->addCourier();
}

MainWindow::~MainWindow() {
    delete ui;
}

void MainWindow::addCourier() {
    for (auto& courier : this->dataManager.getCouriers()) {
        CourierWindow *courierWindow = new CourierWindow(courier, this->dataManager);
        courierWindow->show();
        this->courierWindows.push_back(courierWindow);
    }
}

void MainWindow::addNewPackage() {
    std::string name = ui->Name->text().toStdString();
    std::string street = ui->street->text().toStdString();
    int nr = ui->Number->text().toInt();
    int x = ui->xLine->text().toInt();
    int y = ui->yLine->text().toInt();
    Package package{name, street, nr, x, y};
    this->dataManager.addPackage(package);
    for (auto& courierWindow : this->courierWindows) {
        courierWindow->close();
        delete courierWindow;
    }
    this->populatePackages();
}


void MainWindow::showMap() {
    map *mapWidget = new map(this->dataManager);
    mapWidget->show();
}